from file_utils import load, save


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
    print(
        f"ID: {pediatra['id']}\tNome: {pediatra['nome']}\tSalário: {pediatra['salario']}€"
    )


def printCrianca(crianca):
    print(
        f"ID: {crianca['id']}\tNome: {crianca['nome']}\tData Nasc.: {crianca['dataNascimento']}"
    )


def printConsulta(consulta):
    print(
        f"ID: {consulta['id']}\tData: {consulta['data']}\tCriança ID: {consulta['crianca_id']}\tPediatra ID: {consulta['pediatra_id']}\tPreço: {consulta['preco']}€"
    )


def listarTudo():
    print("\n--- Listagem de Pediatras ---")
    for p in listPediatras:
        printPediatra(p)

    print("\n--- Listagem de Crianças ---")
    for c in listCriancas:
        printCrianca(c)

    print("\n--- Listagem de Consultas ---")
    for con in listConsultas:
        printConsulta(con)


def gerirSistema():
    while True:
        print("\n1. Inserir Pediatra")
        print("2. Inserir Criança")
        print("3. Inserir Consulta")
        print("4. Listar Tudo")
        print("0. Sair")

        op = input("\nOpção: ")

        if op == "1":
            listPediatras.append(adicionarPediatra())
            save(file_pediatras, listPediatras)
        elif op == "2":
            listCriancas.append(adicionarCrianca())
            save(file_criancas, listCriancas)
        elif op == "3":
            listConsultas.append(adicionarConsulta())
            save(file_consultas, listConsultas)
        elif op == "4":
            listarTudo()
        elif op == "0":
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
