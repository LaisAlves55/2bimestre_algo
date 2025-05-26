compras = []

while True:
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        produto = input("Digite o produto: ")
        compras.append(produto)
    elif opcao == 2:
        produto = input("Digite o produto: ")
        if produto in compras:
            compras.remove(produto)
        else:
            print("Produto nao encontrado")
    elif opcao == 3:
        print(compras)
    elif opcao == 4:
        break
    
