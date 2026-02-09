from file_utils import load, save
from datetime import datetime
import beaupy
import re


# =====================
# Funções de utilidade
# =====================


def ageCalculator(born_date_str):
    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y-%m-%d",
    ]
    for format in formats:
        try:
            born_date = datetime.strptime(born_date_str, format)
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
        date = input("date de Nascimento (DD/MM/AAAA ou AAAA-MM-DD): ")
        result = ageCalculator(date)
        if isinstance(result, int):
            return date
        elif result == "date no futuro":
            print("❌ Verifique o ano de nascimento inserido.")
        else:
            print("❌ data  inválida. Tente novamente.")


def findById(list, id):
    for item in list:
        if item.get("id") == id:
            return item
    return None


def removeById(list, id):
    item = findById(list, id)
    if item:
        list.remove(item)
        return True
    return False


def editItem(item, attribute):
    print("\n--- Editar Item ---")
    for key, value in item.items():
        print(f"{key}: {value}")
    while True:
        attribute_tobe_edited = input(
            "Qual o atributo que deseja editar (ou 'sair' para terminar)? "
        ).lower()
        if attribute_tobe_edited == "sair":
            break
        if attribute_tobe_edited in attribute:
            new_value = input(f"Novo valor para {attribute_tobe_edited}: ")
            if attribute_tobe_edited in ("wage", "price"):
                try:
                    item[attribute_tobe_edited] = float(new_value)
                except ValueError:
                    print(
                        "Valor inválido para este atributo. Por favor, insira um número."
                    )
            elif attribute_tobe_edited == "bornDate":
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
    name = input("nome: ")
    wage = float(input("Salário: "))
    return {"id": pediatrician_id, "nome": name, "salário": wage}


def addChild():
    print("\nNova Criança\n")
    id_child = input("ID: ")
    name = input("nome: ")
    bornDate = bornDateRequest()
    return {"Id": id_child, "Nome": name, "Data de Nascimento": bornDate}


def addConsultation():
    print("\nNova consulta \n")
    id_consultation = input("ID: ")
    date = input("date (DD/MM/AAAA): ")
    child_id = input("ID da Criança: ")
    pediatrician_id = input("ID do pediatra: ")
    price = float(input("Preço: "))
    return {
        "Id": id_consultation,
        "Data": date,
        "ID da Criança": child_id,
        "ID do pediatra": pediatrician_id,
        "Preço": price,
    }


# =====================
# Funções de impressão/Print
# =====================


def printPediatrician(pediatrician):
    print(
        f"ID: {pediatrician['id']}\tNome: {pediatrician['name']}\tSalário: {pediatrician['wage']}€"
    )


def printChild(child):
    age = ageCalculator(child["bornDate"])
    print(
        f"ID: {child['id']}\tNome: {child['name']}\tData Nascimento: {child['bornDate']}\tIdade: {age} anos"
    )


def printAppointment(appointment):
    child = findById(childList, consulta["child_id"])
    pediatra = findById(pediatricianList, consulta["pediatrician_id"])
    name_child = child["name"] if child else "Desconhecida"
    name_pediatrician = pediatra["name"] if pediatra else "Desconhecido"
    print(
        "appointment\n"
        f" data : {appointment['date']}\n"
        f" Pediatra: {name_pediatrician}\n"
        f" Criança: {name_child}\n"
        f" Preço: {appointment['price']}€"
    )


# =====================
# Funções de listagem, pesquisa e edição
# =====================


def pediatricianList():
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
        if term.lower() in p["name"].lower() or term == p["id"]
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
        printPediatrician(pediatrician)
    else:
        print("Pediatra não encontrado.")


def editPediatrician():
    pediatrician_id = input(
        "Indique o ID do pediatra do qual pretende editar algum dado: "
    )
    pediatra = findById(pediatricianList, pediatrician_id)
    if pediatra:
        editItem(pediatrician, ["name", "wage"])
        save(file_pediatrician, pediatricianList)
        print("Dado do pediatra atualizado com sucesso.")
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
    term = input("Indique o ID ou nome da criança que pretende pesquisar: ")
    results = [
        c for c in childList if term.lower() in c["name"].lower() or term == c["id"]
    ]
    if results:
        print("\n--- Resultados da Pesquisa de Crianças ---")
        for c in results:
            printChild(c)
    else:
        print("O ID ou nome fornecido não corresponde a Nenhuma criança.")


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
        editItem(child, ["name", "bornDate"])
        save(file_children, childList)
        print("Dado atualiada com sucesso.")
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
        save(file_appointiments, appointmentList)
        print("Consulta desmarcada com sucesso.")
    else:
        print("Consulta não encontrada.")


def appointmentList():
    print("\n--- Listagem de Consultas ---")
    if appointmentList:
        for appoint in appointmentList:
            printAppointment(appoint)
    else:
        print("Nenhuma consulta registada.")


def searchQueriesByDate():
    search_date = input(
        "Indique a data para qual pretende pesquisar consultas (DD/MM/AAAA): "
    )
    queries_on_date = [
        appoint for appoint in appointmentList if appoint["date"] == search_date
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
        appoint for appoint in appointmentList if appoint["child_id"] == id_child
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
        "Indique o ID do pediatria para visualizar as próximas marcações: "
    )
    today = datetime.now().strftime("%d/%m/%Y")
    nextAppointment = []
    for appoint in appointmentList:
        try:
            appointment_date = datetime.strptime(appoint["date"], "%d/%m/%Y")
            today_date = datetime.strptime(today, "%d/%m/%Y")
            if (
                appoint["pediatrician_id"] == pediatrician_id
                and appointment_date >= today_date
            ):
                nextAppointment.append(appoint)
        except ValueError:
            continue

    if nextAppointment:
        print(f"\n--- Próximas Marcações do Pediatra (ID: {pediatrician_id}) ---")
        nextAppointment.sort(key=lambda x: datetime.strptime(x["date"], "%d/%m/%Y"))
        for appoint in nextAppointment:
            printAppointment(appoint)
    else:
        print(
            f"Não existe marcações próxima para o pediatra com o ID {pediatrician_id}."
        )


def countRecords():
    print("\n--- Contagem de Registos ---")
    print(f"Pediatras: {len(pediatricianList)}")
    print(f"Crianças: {len(childList)}")
    print(f"Consultas: {len(appointmentList)}")


def totalInvoicedBetweenDates():
    start_date_str = input("Data de início (DD/MM/AAAA): ")
    end_date_str = input("Data de fim (DD/MM/AAAA): ")

    try:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de data inválido. Use DD/MM/AAAA.")
        return

    total_invoiced = 0
    for consulta in appointmentList:
        try:
            appointment_date = datetime.strptime(appointment["date"], "%d/%m/%Y")
            if start_date <= appointment_date <= end_date:
                total_invoiced += consulta["price"]
        except ValueError:
            continue

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
            pediatricianList()
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
        "Marcar consulta ",
        "Desmarcar consulta ",
        "Listar consultas",
        "Pesquisar Consultas por data ",
        "Histórico de consultas da criança",
        "Próximas marcações do pediatra",
        "Voltar",
    ]

    while True:
        idx = select_option("Gestão de Consultas", options)
        if idx == 0:
            appointmentList.append(addConsultation())
            save(file_appointiments, appointmentList)
        elif idx == 1:
            cancelAppointment()
        elif idx == 2:
            appointmentList()
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
file_appointiments = "json/consultas.json"

# Carregamento inicial das listas
pediatricianList = load(file_pediatrician)
childList = load(file_children)
appointmentList = load(file_appointiments)

if __name__ == "__main__":
    systemManage()
