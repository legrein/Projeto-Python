from file_utils import load, save
from datetime import datetime
import beaupy


# =====================
# Funções de utilidade
# =====================


def ageCalculator(born_date_str):
    # Datas no JSON vêm no formato "DD/MM/AAAA", ex: "15/05/2018"
    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y-%m-%d",
    ]
    for fmt in formats:
        try:
            born_date = datetime.strptime(born_date_str, fmt)
            today = datetime.today()
            if born_date > today:
                return "date no futuro"
            age = (
                today.year
                - born_date.year
                - ((today.month, today.day) < (born_date.month, born_date.day))
            )
            return age
        except ValueError:
            continue
    return "date inválida"


def bornDateRequest():
    while True:
        date = input("Data de Nascimento (DD/MM/AAAA ou AAAA-MM-DD): ")
        result = ageCalculator(date)
        if isinstance(result, int):
            return date
        elif result == "date no futuro":
            print("❌ Verifique o ano de nascimento inserido.")
        else:
            print("❌ Data inválida. Tente novamente.")


def findById(lista, id_):
    for item in lista:
        if item.get("id") == id_:
            return item
    return None


def removeById(lista, id_):
    item = findById(lista, id_)
    if item:
        lista.remove(item)
        return True
    return False


def editItem(item, allowed_attributes):
    print("\n--- Editar Registo ---")
    for key, value in item.items():
        print(f"{key}: {value}")
    while True:
        attribute_tobe_edited = input(
            "Qual o atributo que deseja editar (ou 'sair' para terminar)? "
        ).strip()
        if attribute_tobe_edited.lower() == "sair":
            break
        if attribute_tobe_edited in allowed_attributes:
            new_value = input(f"Novo valor para {attribute_tobe_edited}: ")
            if attribute_tobe_edited in ("salario", "preco"):
                try:
                    item[attribute_tobe_edited] = float(new_value)
                except ValueError:
                    print(
                        "Valor inválido para este atributo. Por favor, insira um número."
                    )
            elif attribute_tobe_edited == "dataNascimento":
                item[attribute_tobe_edited] = bornDateRequest()
            else:
                item[attribute_tobe_edited] = new_value
            print(
                f"Atributo '{attribute_tobe_edited}' foi atualizado para '{item[attribute_tobe_edited]}'."
            )
        else:
            print("Atenção! Atributo inválido ou não permitido para edição.")
    return item


# =====================
# Funções de adição
# =====================


def addPediatrician():
    print("\nNovo pediatra\n")
    pediatrician_id = input("ID: ")
    nome = input("Nome: ")
    while True:
        try:
            salario = float(input("Salário: "))
            break
        except ValueError:
            print("Valor inválido. Introduza um número.")
    return {"id": pediatrician_id, "nome": nome, "salario": salario}


def addChild():
    print("\nNova Criança\n")
    id_child = input("ID: ")
    nome = input("Nome: ")
    dataNascimento = bornDateRequest()
    return {"id": id_child, "nome": nome, "dataNascimento": dataNascimento}


def addConsultation():
    print("\nNova consulta\n")
    id_consultation = input("ID: ")

    # Aceitar vários formatos de data
    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y-%m-%d",
    ]

    while True:
        data_input = input("Data (DD/MM/AAAA): ")
        valid = False

        for fmt in formats:
            try:
                # Apenas validar — não converter permanentemente
                datetime.strptime(data_input, fmt)
                valid = True
                break
            except ValueError:
                pass

        if valid:
            break
        else:
            print("❌ Formato de data inválido. Tente novamente.")

    crianca_id = input("ID da Criança: ")
    pediatra_id = input("ID do pediatra: ")

    while True:
        try:
            preco = float(input("Preço: "))
            break
        except ValueError:
            print("Valor inválido. Introduza um número.")

    return {
        "id": id_consultation,
        "data": data_input,  # Mantém o formato original
        "crianca_id": crianca_id,
        "pediatra_id": pediatra_id,
        "preco": preco,
    }

# =====================
# Funções de impressão
# =====================


def printPediatrician(pediatrician):
    print(
        f"ID: {pediatrician['id']}\tNome: {pediatrician['nome']}\tSalário: {pediatrician['salario']}€"
    )


def printChild(child):
    age = ageCalculator(child["dataNascimento"])
    print(
        f"ID: {child['id']}\tNome: {child['nome']}\tData Nascimento: {child['dataNascimento']}\tIdade: {age} anos"
    )


def printAppointment(appointment):
    child = findById(childList, appointment["crianca_id"])
    pediatra = findById(pediatricianList, appointment["pediatra_id"])
    nome_crianca = child["nome"] if child else "Desconhecida"
    nome_pediatra = pediatra["nome"] if pediatra else "Desconhecido"
    print(
        "Consulta\n"
        f" Data: {appointment['data']}\n"
        f" Pediatra: {nome_pediatra}\n"
        f" Criança: {nome_crianca}\n"
        f" Preço: {appointment['preco']}€"
    )


# =====================
# Listagem, pesquisa e edição
# =====================


def listPediatricians():
    print("\n--- Listagem de Pediatras ---")
    if pediatricianList:
        for p in pediatricianList:
            printPediatrician(p)
    else:
        print("Nenhum pediatra registado.")


def pediatricianSearch():
    term = input("Indique o ID ou nome do pediatra que pretende procurar: ")
    results = [
        p
        for p in pediatricianList
        if term.lower() in p["nome"].lower() or term.lower() == p["id"].lower()
    ]
    if results:
        print("\n--- Resultados da Pesquisa de Pediatras ---")
        for p in results:
            printPediatrician(p)
    else:
        print("Nenhum pediatra encontrado com o ID ou nome fornecido.")


def seePediatricianData():
    pediatrician_id = input(
        "Indique o ID do pediatra do qual pretende visualizar os dados: "
    )
    pediatra = findById(pediatricianList, pediatrician_id)
    if pediatra:
        print("\n--- Dados do Pediatra ---")
        printPediatrician(pediatra)
    else:
        print("Pediatra não encontrado.")


def editPediatrician():
    pediatrician_id = input(
        "Indique o ID do pediatra do qual pretende editar algum dado: "
    )
    pediatra = findById(pediatricianList, pediatrician_id)
    if pediatra:
        editItem(pediatra, ["nome", "salario"])
        save(file_pediatrician, pediatricianList)
        print("Dados do pediatra atualizados com sucesso.")
    else:
        print("Pediatra não encontrado.")


def removePediatrician():
    pediatrician_id = input("Indique o ID do pediatra que pretende remover: ")
    if removeById(pediatricianList, pediatrician_id):
        save(file_pediatrician, pediatricianList)
        print("Pediatra removido com sucesso.")
    else:
        print("Pediatra não encontrado.")


def listChildren():
    print("\n--- Listagem de Crianças ---")
    if childList:
        for c in childList:
            printChild(c)
    else:
        print("Nenhuma criança registada.")


def childSearch():
    term = input("Indique o ID ou nome da criança que pretende pesquisar: ").lower()
    results = [
        c for c in childList if term.lower() in c["nome"].lower() or term.lower() == c["id"].lower()
    ]
    if results:
        print("\n--- Resultados da Pesquisa de Crianças ---")
        for c in results:
            printChild(c)
    else:
        print("O ID ou nome fornecido não corresponde a nenhuma criança.")


def seeChildData():
    id_child = input("Indique o ID da Criança da qual pretende visualizar os dados: ")
    child = findById(childList, id_child)
    if child:
        print("\n--- Dados da Criança ---")
        printChild(child)
    else:
        print("Criança não encontrada.")


def editChild():
    id_child = input("Indique o ID da Criança da qual pretende editar algum elemento: ")
    child = findById(childList, id_child)
    if child:
        editItem(child, ["nome", "dataNascimento"])
        save(file_children, childList)
        print("Dados atualizados com sucesso.")
    else:
        print("Criança não encontrada.")


def removeChild():
    id_child = input("Indique o ID da Criança que pretende remover: ")
    if removeById(childList, id_child):
        save(file_children, childList)
        print("Criança removida com sucesso.")
    else:
        print("Criança não encontrada.")


def cancelAppointment():
    id_consultation = input("Indique o ID da consulta que pretende desmarcar: ")
    if removeById(appointmentList, id_consultation):
        save(file_appointments, appointmentList)
        print("Consulta desmarcada com sucesso.")
    else:
        print("Consulta não encontrada.")


def listAppointments():
    print("\n--- Listagem de Consultas ---")
    if appointmentList:
        for appoint in appointmentList:
            printAppointment(appoint)
    else:
        print("Nenhuma consulta registada.")


def searchQueriesByDate():
    search_date = input(
        "Indique a data para a qual pretende pesquisar consultas (DD/MM/AAAA): "
    )
    queries_on_date = [
        appoint for appoint in appointmentList if appoint["data"] == search_date
    ]
    if queries_on_date:
        print(f"\n--- Consultas em {search_date} ---")
        for appoint in queries_on_date:
            printAppointment(appoint)
    else:
        print(f"Nenhuma consulta agendada para {search_date}.")


def childAppointmentHistory():
    id_child = input(
        "Indique o ID da Criança da qual pretende visualizar o histórico de consultas: "
    )
    child_appointment = [
        appoint for appoint in appointmentList if appoint["crianca_id"].lower() == id_child.lower()
    ]
    if child_appointment:
        print(f"\n--- Histórico de Consultas da Criança (ID: {id_child}) ---")
        for appoint in child_appointment:
            printAppointment(appoint)
    else:
        print(
            f"Nenhum histórico de consultas encontrado para a criança com ID {id_child}."
        )


def nextPediatricianAppointment():
    pediatrician_id = input(
        "Indique o ID do pediatra para visualizar as próximas marcações: "
    )

    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y-%m-%d",
    ]

    # Data atual
    today = datetime.now()

    nextAppointment = []

    for appoint in appointmentList:
        data_str = appoint["data"]
        appointment_date = None

        # Tentar todos os formatos possíveis
        for fmt in formats:
            try:
                appointment_date = datetime.strptime(data_str, fmt)
                break
            except ValueError:
                pass

        # Se não conseguiu converter a data, ignora
        if appointment_date is None:
            continue

        # Verificar se pertence ao pediatra e é futura
        if appoint["pediatra_id"].lower() == pediatrician_id.lower() and appointment_date >= today:
            nextAppointment.append((appointment_date, appoint))

    if nextAppointment:
        print(f"\n--- Próximas Marcações do Pediatra (ID: {pediatrician_id}) ---")

        # Ordenar pela data convertida
        nextAppointment.sort(key=lambda x: x[0])

        for _, appoint in nextAppointment:
            printAppointment(appoint)
    else:
        print(
            f"Não existem marcações próximas para o pediatra com o ID {pediatrician_id}."
        )

def countRecords():
    print("\n--- Contagem de Registos ---")
    print(f"Pediatras: {len(pediatricianList)}")
    print(f"Crianças: {len(childList)}")
    print(f"Consultas: {len(appointmentList)}")


def totalInvoicedBetweenDates():
    start_date_str = input("Data de início (DD/MM/AAAA): ")
    end_date_str = input("Data de fim (DD/MM/AAAA): ")

    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y-%m-%d",
    ]

    # Converter datas de início e fim
    start_date = None
    end_date = None

    for fmt in formats:
        try:
            start_date = datetime.strptime(start_date_str, fmt)
            break
        except ValueError:
            pass

    for fmt in formats:
        try:
            end_date = datetime.strptime(end_date_str, fmt)
            break
        except ValueError:
            pass

    if start_date is None or end_date is None:
        print("Formato de data inválido. Utilize um dos formatos suportados.")
        return

    total_invoiced = 0

    for consulta in appointmentList:
        consulta_date = None

        for fmt in formats:
            try:
                consulta_date = datetime.strptime(consulta["data"], fmt)
                break
            except ValueError:
                pass

        if consulta_date is None:
            continue  # ignora datas inválidas no ficheiro

        if start_date <= consulta_date <= end_date:
            total_invoiced += consulta["preco"]

    print(f"\n--- Total Faturado entre {start_date_str} e {end_date_str} ---")
    print(f"Total: {total_invoiced:.2f}€")

# =========================
# Helpers de Menu com Beaupy
# =========================

def select_option(title, options, cursor="⇒", cursor_style="yellow"):
    print(f"\n--- {title} ---")
    idx = beaupy.select(
        options, cursor=cursor, cursor_style=cursor_style, return_index=True
    )
    return idx


def pediatricianManagementMenu():
    options = [
        "Inserir pediatra",
        "Listar pediatras",
        "Pesquisar pediatra",
        "Ver Dados do pediatra",
        "Editar pediatra",
        "Remover pediatra",
        "Voltar",
    ]

    while True:
        idx = select_option("Gestão de Pediatras", options)
        if idx == 0:
            pediatricianList.append(addPediatrician())
            save(file_pediatrician, pediatricianList)
        elif idx == 1:
            listPediatricians()
        elif idx == 2:
            pediatricianSearch()
        elif idx == 3:
            seePediatricianData()
        elif idx == 4:
            editPediatrician()
        elif idx == 5:
            removePediatrician()
        elif idx == 6:
            break


def childrenManagementMenu():
    options = [
        "Inserir Criança",
        "Listar Crianças",
        "Pesquisar Criança",
        "Ver Dados de Criança",
        "Editar Criança",
        "Remover Criança",
        "Voltar",
    ]

    while True:
        idx = select_option("Gestão de Crianças", options)
        if idx == 0:
            childList.append(addChild())
            save(file_children, childList)
        elif idx == 1:
            listChildren()
        elif idx == 2:
            childSearch()
        elif idx == 3:
            seeChildData()
        elif idx == 4:
            editChild()
        elif idx == 5:
            removeChild()
        elif idx == 6:
            break


def appointmentsManagementMenu():
    options = [
        "Marcar consulta",
        "Desmarcar consulta",
        "Listar consultas",
        "Pesquisar Consultas por data",
        "Histórico de consultas da criança",
        "Próximas marcações do pediatra",
        "Voltar",
    ]

    while True:
        idx = select_option("Gestão de Consultas", options)
        if idx == 0:
            appointmentList.append(addConsultation())
            save(file_appointments, appointmentList)
        elif idx == 1:
            cancelAppointment()
        elif idx == 2:
            listAppointments()
        elif idx == 3:
            searchQueriesByDate()
        elif idx == 4:
            childAppointmentHistory()
        elif idx == 5:
            nextPediatricianAppointment()
        elif idx == 6:
            break


def statisticsMenu():
    options = ["Contagem de Registos", "Total Faturado entre Datas", "Voltar"]

    while True:
        idx = select_option("Estatísticas", options)
        if idx == 0:
            countRecords()
        elif idx == 1:
            totalInvoicedBetweenDates()
        elif idx == 2:
            break


def systemManage():
    options = [
        "Gestão de Pediatras",
        "Gestão de Crianças",
        "Gestão de Consultas",
        "Estatísticas",
        "Sair",
    ]

    while True:
        idx = select_option("Sistema de Consultoria Pediátrica", options)
        if idx == 0:
            pediatricianManagementMenu()
        elif idx == 1:
            childrenManagementMenu()
        elif idx == 2:
            appointmentsManagementMenu()
        elif idx == 3:
            statisticsMenu()
        elif idx == 4:
            print("A sair do sistema. Até breve!")
            break


# =========================
# Configuração de ficheiros
# =========================

file_pediatrician = "json/pediatras.json"
file_children = "json/criancas.json"
file_appointments = "json/consultas.json"

# Carregamento inicial das listas
pediatricianList = load(file_pediatrician)
childList = load(file_children)
appointmentList = load(file_appointments)

if __name__ == "__main__":
    systemManage()
