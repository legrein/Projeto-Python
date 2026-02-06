from file_utils import load, save
from datetime import datetime


def beupy(data_nascimento_str):
    """
    Calcula a idade a partir de uma data de nascimento no formato DD/MM/AAAA.
    """
    try:
        data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
        data_atual = datetime.now()
        idade = (
            data_atual.year
            - data_nascimento.year
            - (
                (data_atual.month, data_atual.day)
                < (data_nascimento.month, data_nascimento.day)
            )
        )
        return idade
    except ValueError:
        return "Data inválida"


def encontrarPorId(lista, id_procurado):
    """
    Encontra um item numa lista pelo seu ID.
    """
    for item in lista:
        if item.get("id") == id_procurado:
            return item
    return None


def removerPorId(lista, id_remover):
    """
    Remove um item de uma lista pelo seu ID.
    Retorna True se removido, False caso contrário.
    """
    item = encontrarPorId(lista, id_remover)
    if item:
        lista.remove(item)
        return True
    return False


def editarItem(item, atributos_permitidos):
    """
    Permite ao utilizador editar os atributos de um item.
    """
    print("\n--- Editar Item ---")
    for chave, valor in item.items():
        print(f"{chave}: {valor}")

    while True:
        atributo_a_editar = input(
            "Qual atributo deseja editar (ou 'sair' para terminar)? "
        ).lower()
        if atributo_a_editar == "sair":
            break
        if atributo_a_editar in atributos_permitidos:
            novo_valor = input(f"Novo valor para {atributo_a_editar}: ")
            if atributo_a_editar == "salario" or atributo_a_editar == "preco":
                try:
                    item[atributo_a_editar] = float(novo_valor)
                except ValueError:
                    print(
                        "Valor inválido para este atributo. Por favor, insira um número."
                    )
            else:
                item[atributo_a_editar] = novo_valor
            print(f"Atributo '{atributo_a_editar}' atualizado para '{novo_valor}'.")
        else:
            print("Atributo inválido ou não permitido para edição.")
    return item


def adicionarPediatra():
    print("\nNovo Pediatra\n")
    id_pediatra = input("ID: ")
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    return {"id": id_pediatra, "nome": nome, "salario": salario}


def adicionarCrianca():
    print("\nNova Criança\n")
    id_crianca = input("ID: ")
    nome = input("Nome: ")
    dataNascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    return {"id": id_crianca, "nome": nome, "dataNascimento": dataNascimento}


def adicionarConsulta():
    print("\nNova Consulta\n")
    id_consulta = input("ID: ")
    data = input("Data (DD/MM/AAAA): ")
    crianca_id = input("ID da Criança: ")
    pediatra_id = input("ID do Pediatra: ")
    preco = float(input("Preço: "))
    return {
        "id": id_consulta,
        "data": data,
        "crianca_id": crianca_id,
        "pediatra_id": pediatra_id,
        "preco": preco,
    }


def printPediatra(pediatra):
    """
    Imprime os dados de um pediatra.
    """
    print(
        f"ID: {pediatra["id"]}\tNome: {pediatra["nome"]}\tSalário: {pediatra["salario"]}€"
    )


def listarPediatras():
    """
    Lista todos os pediatras registados.
    """
    print("\n--- Listagem de Pediatras ---")
    if listPediatras:
        for p in listPediatras:
            printPediatra(p)
    else:
        print("Nenhum pediatra registado.")


def pesquisarPediatra():
    """
    Pesquisa um pediatra pelo ID ou nome.
    """
    termo = input("Pesquisar pediatra por ID ou Nome: ")
    resultados = [
        p
        for p in listPediatras
        if termo.lower() in p["nome"].lower() or termo == p["id"]
    ]
    if resultados:
        print("\n--- Resultados da Pesquisa de Pediatras ---")
        for p in resultados:
            printPediatra(p)
    else:
        print("Nenhum pediatra encontrado com o termo fornecido.")


def verDadosPediatra():
    """
    Permite visualizar os dados de um pediatra específico pelo ID.
    """
    id_pediatra = input("ID do Pediatra para ver dados: ")
    pediatra = encontrarPorId(listPediatras, id_pediatra)
    if pediatra:
        print("\n--- Dados do Pediatra ---")
        printPediatra(pediatra)
    else:
        print("Pediatra não encontrado.")


def editarPediatra():
    """
    Permite editar os dados de um pediatra existente.
    """
    id_pediatra = input("ID do Pediatra para editar: ")
    pediatra = encontrarPorId(listPediatras, id_pediatra)
    if pediatra:
        editarItem(pediatra, ["nome", "salario"])
        save(file_pediatras, listPediatras)
        print("Pediatra atualizado com sucesso.")
    else:
        print("Pediatra não encontrado.")


def removerPediatra():
    """
    Remove um pediatra pelo ID.
    """
    id_pediatra = input("ID do Pediatra para remover: ")
    if removerPorId(listPediatras, id_pediatra):
        save(file_pediatras, listPediatras)
        print("Pediatra removido com sucesso.")
    else:
        print("Pediatra não encontrado.")


def printCrianca(crianca):
    """
    Imprime os dados de uma criança, incluindo a idade.
    """
    idade = beupy(crianca["dataNascimento"])
    print(
        f"ID: {crianca['id']}\tNome: {crianca['nome']}\tData Nasc.: {crianca['dataNascimento']}\tIdade: {idade} anos"
    )


def listarCriancas():
    """
    Lista todas as crianças registadas.
    """
    print("\n--- Listagem de Crianças ---")
    if listCriancas:
        for c in listCriancas:
            printCrianca(c)
    else:
        print("Nenhuma criança registada.")


def pesquisarCrianca():
    """
    Pesquisa uma criança pelo ID ou nome.
    """
    termo = input("Pesquisar criança por ID ou Nome: ")
    resultados = [
        c
        for c in listCriancas
        if termo.lower() in c["nome"].lower() or termo == c["id"]
    ]
    if resultados:
        print("\n--- Resultados da Pesquisa de Crianças ---")
        for c in resultados:
            printCrianca(c)
    else:
        print("Nenhuma criança encontrada com o termo fornecido.")


def verDadosCrianca():
    """
    Permite visualizar os dados de uma criança específica pelo ID.
    """
    id_crianca = input("ID da Criança para ver dados: ")
    crianca = encontrarPorId(listCriancas, id_crianca)
    if crianca:
        print("\n--- Dados da Criança ---")
        printCrianca(crianca)
    else:
        print("Criança não encontrada.")


def editarCrianca():
    """
    Permite editar os dados de uma criança existente.
    """
    id_crianca = input("ID da Criança para editar: ")
    crianca = encontrarPorId(listCriancas, id_crianca)
    if crianca:
        editarItem(crianca, ["nome", "dataNascimento"])
        save(file_criancas, listCriancas)
        print("Criança atualizada com sucesso.")
    else:
        print("Criança não encontrada.")


def removerCrianca():
    """
    Remove uma criança pelo ID.
    """
    id_crianca = input("ID da Criança para remover: ")
    if removerPorId(listCriancas, id_crianca):
        save(file_criancas, listCriancas)
        print("Criança removida com sucesso.")
    else:
        print("Criança não encontrada.")


def printConsulta(consulta):
    """
    Imprime os dados de uma consulta, incluindo nomes do pediatra e da criança.
    """
    crianca = encontrarPorId(listCriancas, consulta["crianca_id"])
    pediatra = encontrarPorId(listPediatras, consulta["pediatra_id"])
    nome_crianca = crianca["nome"] if crianca else "Desconhecida"
    nome_pediatra = pediatra["nome"] if pediatra else "Desconhecido"

    print(
        f"Consulta\n Data : {consulta["data"]} \n Pediatra: {nome_pediatra} \n Criança: {nome_crianca} \n Preço: {consulta["preco"]}€"
    )


def desmarcarConsulta():
    """
    Desmarca uma consulta pelo ID.
    """
    id_consulta = input("ID da Consulta para desmarcar: ")
    if removerPorId(listConsultas, id_consulta):
        save(file_consultas, listConsultas)
        print("Consulta desmarcada com sucesso.")
    else:
        print("Consulta não encontrada.")


def listarConsultas():
    """
    Lista todas as consultas registadas.
    """
    print("\n--- Listagem de Consultas ---")
    if listConsultas:
        for con in listConsultas:
            printConsulta(con)
    else:
        print("Nenhuma consulta registada.")


def pesquisarConsultasPorData():
    """
    Lista consultas que se irão realizar numa data específica.
    """
    data_pesquisa = input("Data para pesquisar consultas (DD/MM/AAAA): ")
    consultas_na_data = [con for con in listConsultas if con["data"] == data_pesquisa]
    if consultas_na_data:
        print(f"\n--- Consultas em {data_pesquisa} ---")
        for con in consultas_na_data:
            printConsulta(con)
    else:
        print(f"Nenhuma consulta agendada para {data_pesquisa}.")


def historicoConsultasCrianca():
    """
    Mostra o histórico de consultas de uma criança específica.
    """
    id_crianca = input("ID da Criança para ver histórico de consultas: ")
    consultas_crianca = [
        con for con in listConsultas if con["crianca_id"] == id_crianca
    ]
    if consultas_crianca:
        print(f"\n--- Histórico de Consultas da Criança (ID: {id_crianca}) ---")
        for con in consultas_crianca:
            printConsulta(con)
    else:
        print(
            f"Nenhum histórico de consultas encontrado para a criança com ID {id_crianca}."
        )


def proximasMarcacoesPediatra():
    """
    Mostra as próximas marcações de um pediatra específico.
    """
    id_pediatra = input("ID do Pediatra para ver próximas marcações: ")
    hoje = datetime.now().strftime("%d/%m/%Y")

    proximas_consultas = []
    for con in listConsultas:
        try:
            data_consulta = datetime.strptime(con["data"], "%d/%m/%Y")
            data_hoje = datetime.strptime(hoje, "%d/%m/%Y")
            if con["pediatra_id"] == id_pediatra and data_consulta >= data_hoje:
                proximas_consultas.append(con)
        except ValueError:
            continue  # Ignora consultas com datas inválidas

    if proximas_consultas:
        print(f"\n--- Próximas Marcações do Pediatra (ID: {id_pediatra}) ---")
        # Ordenar por data para melhor visualização
        proximas_consultas.sort(key=lambda x: datetime.strptime(x["data"], "%d/%m/%Y"))
        for con in proximas_consultas:
            printConsulta(con)
    else:
        print(
            f"Nenhuma próxima marcação encontrada para o pediatra com ID {id_pediatra}."
        )


def contarRegistos():
    """
    Conta e exibe o número de registos para Pediatras, Crianças e Consultas.
    """
    print("\n--- Contagem de Registos ---")
    print(f"Pediatras: {len(listPediatras)}")
    print(f"Crianças: {len(listCriancas)}")
    print(f"Consultas: {len(listConsultas)}")


def totalFaturadoEntreDatas():
    """
    Calcula o total faturado de consultas entre duas datas especificadas.
    """
    data_inicio_str = input("Data de início (DD/MM/AAAA): ")
    data_fim_str = input("Data de fim (DD/MM/AAAA): ")

    try:
        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de data inválido. Use DD/MM/AAAA.")
        return

    total_faturado = 0.0
    for consulta in listConsultas:
        try:
            data_consulta = datetime.strptime(consulta["data"], "%d/%m/%Y")
            if data_inicio <= data_consulta <= data_fim:
                total_faturado += consulta["preco"]
        except ValueError:
            continue  # Ignora consultas com datas inválidas

    print(f"\n--- Total Faturado entre {data_inicio_str} e {data_fim_str} ---")
    print(f"Total: {total_faturado:.2f}€")


def menuGestaoPediatras():
    """
    Menu de gestão de pediatras.
    """
    while True:
        print("\n--- Gestão de Pediatras ---")
        print("1. Inserir Pediatra")
        print("2. Listar Pediatras")
        print("3. Pesquisar Pediatra")
        print("4. Ver Dados de Pediatra")
        print("5. Editar Pediatra")
        print("6. Remover Pediatra")
        print("0. Voltar")

        op = input("\nOpção: ")

        if op == "1":
            listPediatras.append(adicionarPediatra())
            save(file_pediatras, listPediatras)
        elif op == "2":
            listarPediatras()
        elif op == "3":
            pesquisarPediatra()
        elif op == "4":
            verDadosPediatra()
        elif op == "5":
            editarPediatra()
        elif op == "6":
            removerPediatra()
        elif op == "0":
            break
        else:
            print("\nErro: operação inválida!\n")


def menuGestaoCriancas():
    """
    Menu de gestão de crianças.
    """
    while True:
        print("\n--- Gestão de Crianças ---")
        print("1. Inserir Criança")
        print("2. Listar Crianças")
        print("3. Pesquisar Criança")
        print("4. Ver Dados de Criança")
        print("5. Editar Criança")
        print("6. Remover Criança")
        print("0. Voltar")

        op = input("\nOpção: ")

        if op == "1":
            listCriancas.append(adicionarCrianca())
            save(file_criancas, listCriancas)
        elif op == "2":
            listarCriancas()
        elif op == "3":
            pesquisarCrianca()
        elif op == "4":
            verDadosCrianca()
        elif op == "5":
            editarCrianca()
        elif op == "6":
            removerCrianca()
        elif op == "0":
            break
        else:
            print("\nErro: operação inválida!\n")


def menuGestaoConsultas():
    """
    Menu de gestão de consultas.
    """
    while True:
        print("\n--- Gestão de Consultas ---")
        print("1. Marcar Consulta")
        print("2. Desmarcar Consulta")
        print("3. Listar Consultas")
        print("4. Pesquisar Consultas por Data")
        print("5. Histórico de Consultas de uma Criança")
        print("6. Próximas Marcações do Pediatra")
        print("0. Voltar")

        op = input("\nOpção: ")

        if op == "1":
            listConsultas.append(adicionarConsulta())
            save(file_consultas, listConsultas)
        elif op == "2":
            desmarcarConsulta()
        elif op == "3":
            listarConsultas()
        elif op == "4":
            pesquisarConsultasPorData()
        elif op == "5":
            historicoConsultasCrianca()
        elif op == "6":
            proximasMarcacoesPediatra()
        elif op == "0":
            break
        else:
            print("\nErro: operação inválida!\n")


def menuEstatisticas():
    """
    Menu de estatísticas.
    """
    while True:
        print("\n--- Estatísticas ---")
        print("1. Contagem de Registos")
        print("2. Total Faturado entre Datas")
        print("0. Voltar")

        op = input("\nOpção: ")

        if op == "1":
            contarRegistos()
        elif op == "2":
            totalFaturadoEntreDatas()
        elif op == "0":
            break
        else:
            print("\nErro: operação inválida!\n")


def gerirSistema():
    """
    Menu principal do sistema de consultoria pediátrica.
    """
    while True:
        print("\n--- Sistema de Consultoria Pediátrica ---")
        print("1. Gestão de Pediatras")
        print("2. Gestão de Crianças")
        print("3. Gestão de Consultas")
        print("4. Estatísticas")
        print("5. Sair")

        op = input("\nOpção: ")

        if op == "1":
            menuGestaoPediatras()
        elif op == "2":
            menuGestaoCriancas()
        elif op == "3":
            menuGestaoConsultas()
        elif op == "4":
            menuEstatisticas()
        elif op == "5":
            print("A sair do sistema. Até breve!")
            break
        else:
            print("\nErro: operação inválida!\n")


# Configuração de ficheiros
file_pediatras = "json/pediatras.json"
file_criancas = "json/criancas.json"
file_consultas = "json/consultas.json"

# Carregamento inicial das listas
listPediatras = load(file_pediatras)
listCriancas = load(file_criancas)
listConsultas = load(file_consultas)

if __name__ == "__main__":
    gerirSistema()
