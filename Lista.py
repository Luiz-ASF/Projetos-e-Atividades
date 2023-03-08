produtos = []

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    valor = float(input("Digite o valor do produto: "))
    disponivel = input("O produto está disponível para venda? (sim/não): ")
    produtos.append({
        "nome": nome,
        "descricao": descricao,
        "valor": valor,
        "disponivel": disponivel.lower() == "sim"
    })
    listar_produtos()

def listar_produtos():
    produtos_ordenados = sorted(produtos, key=lambda produto: produto["valor"])
    print("\nLista de Produtos:\n")
    print("Nome\tValor")
    for produto in produtos_ordenados:
        if produto["disponivel"]:
            print("{}\tR${:.2f}".format(produto['nome'], produto['valor']))
    print("\n")
    menu()

def menu():
    opcao = input("Selecione uma opção:\n1 - Cadastrar Produto\n2 - Listar Produtos\n3 - Sair\n")
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        print("Obrigado por utilizar nosso programa!")
    else:
        print("Opção inválida!")
        menu()

menu()

