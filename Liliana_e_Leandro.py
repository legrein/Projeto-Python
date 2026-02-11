from file_utils import load, save
from datetime import datetime
import beaupy

# =====================
# Funções de utilidade
# =====================

def generateSequentialId(lista):
    if not lista:
        return 1
    try:
        last_id = max(int(item["id"]) for item in lista)
        return last_id + 1
    except:
        return 1


def ageCalculator(born_date_str):
    formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]
    for fmt in formats:
        try:
            born_date = datetime.strptime(born_date_str, fmt)
            today = datetime.today()
            if born_date > today:
                return "date no futuro"
            age = today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))
            return age
        except ValueError:
            continue
    return "date inválida"


def bornDateRequest():
    while True:
        date = input("Data de Nascimento (DD/MM/AAAA): ")
        result = ageCalculator(date)
        if isinstance(result, int):
            return date
        elif result == "date no futuro":
            print("❌ Verifique o ano de nascimento inserido.")
        else:
            print("❌ Data inválida. Tente novamente.")


def findById(lista, id_):
    try:
        id_ = int(id_)
    except:
        return None

    for item in lista:
        if int(item.get("id")) == id_:
            return item
    return None


def findByContribuinte(lista, nif):
    for item in lista:
        if item.get("contribuinte") == nif:
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
        attribute = input("Atributo a editar (ou 'sair'): ").strip()
        if attribute.lower() == "sair":
            break

        if attribute not in allowed_attributes:
            print("Atributo inválido.")
            continue

        new_value = input(f"Novo valor para {attribute}: ")

        if attribute in ("salario", "preco", "price"):
            try:
                item[attribute] = float(new_value)
            except:
                print("Valor inválido.")
        elif attribute == "dataNascimento":
            item[attribute] = bornDateRequest()
        else:
            item[attribute] = new_value

        print(f"Atributo '{attribute}' atualizado.")
    return item

# =====================
# Funções de adição
# =====================

def addPediatrician():
    print("\nNovo pediatra\n")
    pediatrician_id = generateSequentialId(pediatricianList)
    nome = input("Nome: ")
    contribuinte = input("Contribuinte (NIF): ")

    while True:
        try:
            salario = float(input("Salário: "))
            break
        except ValueError:
            print("Valor inválido.")

    return {"id": pediatrician_id, "nome": nome, "contribuinte": contribuinte, "salario": salario}


def addChild():
    print("\nNova Criança\n")
    id_child = generateSequentialId(childList)
    nome = input("Nome: ")
    contribuinte = input("Contribuinte (NIF): ")
    dataNascimento = bornDateRequest()

    return {"id": id_child, "nome": nome, "contribuinte": contribuinte, "dataNascimento": dataNascimento}


def addConsultation():
    print("\nNova consulta\n")
    id_consultation = generateSequentialId(appointmentList)

    formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]

    while True:
        data_input = input("Data (DD/MM/AAAA): ")
        valid = False
        for fmt in formats:
            try:
                datetime.strptime(data_input, fmt)
                valid = True
                break
            except:
                pass
        if valid:
            break
        print("❌ Data inválida.")

    # Seleção por contribuinte
    while True:
        nif_child = input("Contribuinte da Criança: ")
        child = findByContribuinte(childList, nif_child)
        if child:
            break
        print("❌ Criança não encontrada. Verifique o NIF.")

    while True:
        nif_ped = input("Contribuinte do Pediatra: ")
        pediatra = findByContribuinte(pediatricianList, nif_ped)
        if pediatra:
            break
        print("❌ Pediatra não encontrado. Verifique o NIF.")

    while True:
        try:
            preco = float(input("Preço: "))
            break
        except:
            print("Valor inválido.")

    return {
        "id": id_consultation,
        "date": data_input,
        "nif_child": nif_child,
        "nif_pediatrician": nif_ped,
        "price": preco
    }

# =====================
# Impressão
# =====================

def printPediatrician(p):
    print(f"ID: {p['id']}\tNome: {p['nome']}\tNIF: {p['contribuinte']}\tSalário: {p['salario']}€")


def printChild(c):
    age = ageCalculator(c["dataNascimento"])
    print(f"ID: {c['id']}\tNome: {c['nome']}\tNIF: {c['contribuinte']}\tData Nasc: {c['dataNascimento']}\tIdade: {age} anos")


def printAppointment(a):
    child = findByContribuinte(childList, a["nif_child"])
    pediatra = findByContribuinte(pediatricianList, a["nif_pediatrician"])
    nome_crianca = child["nome"] if child else "Desconhecida"
    nome_pediatra = pediatra["nome"] if pediatra else "Desconhecido"

    print(
        "Consulta\n"
        f" Data: {a['date']}\n"
        f" Pediatra: {nome_pediatra}\n"
        f" Criança: {nome_crianca}\n"
        f" Preço: {a['price']}€"
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
    nif = input("Contribuinte (NIF) do pediatra: ")
    pediatra = findByContribuinte(pediatricianList, nif)
    if pediatra:
        print("\n--- Dados do Pediatra ---")
        printPediatrician(pediatra)
    else:
        print("Nenhum pediatra encontrado com esse contribuinte.")


def seePediatricianData():
    nif = input("Contribuinte (NIF) do pediatra: ")
    pediatra = findByContribuinte(pediatricianList, nif)
    if pediatra:
        print("\n--- Dados do Pediatra ---")
        printPediatrician(pediatra)
    else:
        print("Pediatra não encontrado.")


def editPediatrician():
    nif = input("Contribuinte (NIF) do pediatra: ")
    pediatra = findByContribuinte(pediatricianList, nif)
    if pediatra:
        editItem(pediatra, ["nome", "contribuinte", "salario"])
        save(file_pediatrician, pediatricianList)
        print("Dados do pediatra atualizados com sucesso.")
    else:
        print("Pediatra não encontrado.")


def removePediatrician():
    nif = input("Contribuinte (NIF) do pediatra: ")
    pediatra = findByContribuinte(pediatricianList, nif)
    if pediatra:
        pediatricianList.remove(pediatra)
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
    nif = input("Contribuinte (NIF) da criança: ")
    child = findByContribuinte(childList, nif)
    if child:
        print("\n--- Dados da Criança ---")
        printChild(child)
    else:
        print("Nenhuma criança encontrada com esse contribuinte.")


def seeChildData():
    nif = input("Contribuinte (NIF) da criança: ")
    child = findByContribuinte(childList, nif)
    if child:
        print("\n--- Dados da Criança ---")
        printChild(child)
    else:
        print("Criança não encontrada.")


def editChild():
    nif = input("Contribuinte (NIF) da criança: ")
    child = findByContribuinte(childList, nif)
    if child:
        editItem(child, ["nome", "contribuinte", "dataNascimento"])
        save(file_children, childList)
        print("Dados atualizados com sucesso.")
    else:
        print("Criança não encontrada.")


def removeChild():
    nif = input("Contribuinte (NIF) da criança: ")
    child = findByContribuinte(childList, nif)
    if child:
        childList.remove(child)
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
    search_date_input = input("Indique a data para a qual pretende pesquisar consultas (DD/MM/AAAA): ").strip()

    formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]

    search_date = None
    for fmt in formats:
        try:
            search_date = datetime.strptime(search_date_input, fmt)
            break
        except ValueError:
            pass

    if search_date is None:
        print("Formato de data inválido.")
        return

    queries_on_date = []

    for appoint in appointmentList:
        appoint_date_str = appoint["date"]
        appoint_date = None

        for fmt in formats:
            try:
                appoint_date = datetime.strptime(appoint_date_str, fmt)
                break
            except ValueError:
                pass

        if appoint_date and appoint_date.date() == search_date.date():
            queries_on_date.append(appoint)

    if queries_on_date:
        print(f"\n--- Consultas em {search_date_input} ---")
        for appoint in queries_on_date:
            printAppointment(appoint)
    else:
        print(f"Nenhuma consulta agendada para {search_date_input}.")


def childAppointmentHistory():
    nif = input("Contribuinte da Criança: ")
    child = findByContribuinte(childList, nif)

    if not child:
        print("Criança não encontrada.")
        return

    child_appointment = [
        appoint for appoint in appointmentList if appoint["nif_child"] == nif
    ]

    if child_appointment:
        print(f"\n--- Histórico de Consultas da Criança (NIF: {nif}) ---")
        for appoint in child_appointment:
            printAppointment(appoint)
    else:
        print(f"Nenhum histórico de consultas encontrado para a criança com NIF {nif}.")


def nextPediatricianAppointment():
    nif = input("Contribuinte do Pediatra: ")
    pediatra = findByContribuinte(pediatricianList, nif)

    if not pediatra:
        print("Pediatra não encontrado.")
        return

    formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]

    today = datetime.now()
    nextAppointment = []

    for appoint in appointmentList:
        data_str = appoint["date"]
        appointment_date = None

        for fmt in formats:
            try:
                appointment_date = datetime.strptime(data_str, fmt)
                break
            except ValueError:
                pass

        if appointment_date and appoint["nif_pediatrician"] == nif and appointment_date >= today:
            nextAppointment.append((appointment_date, appoint))

    if nextAppointment:
        print(f"\n--- Próximas Marcações do Pediatra (NIF: {nif}) ---")
        nextAppointment.sort(key=lambda x: x[0])
        for _, appoint in nextAppointment:
            printAppointment(appoint)
    else:
        print(f"Não existem marcações próximas para o pediatra com o NIF {nif}.")


def countRecords():
    print("\n--- Contagem de Registos ---")
    print(f"Pediatras: {len(pediatricianList)}")
    print(f"Crianças: {len(childList)}")
    print(f"Consultas: {len(appointmentList)}")


def totalInvoicedBetweenDates():
    start_date_str = input("Data de início (DD/MM/AAAA): ")
    end_date_str = input("Data de fim (DD/MM/AAAA): ")

    formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]

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
        print("Formato de data inválido.")
        return

    total_invoiced = 0

    for consulta in appointmentList:
        consulta_date = None

        for fmt in formats:
            try:
                consulta_date = datetime.strptime(consulta["date"], fmt)
                break
            except ValueError:
                pass

        if consulta_date and start_date <= consulta_date <= end_date:
            total_invoiced += consulta["price"]

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
