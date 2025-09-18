# CONTROLE DE ESTOQUE

# dois itens iniciais como exemplo para facilitar os testes
lista_produtos = [["arroz", 15, 15.00, 225], ["óleo", 10, 8.00, 80]]
sair = 5

def exibir_lista(lista_produtos):
    print(f"{'ID':<3} {'Produto':<15} {'Qtd':<5} {'Preço Uni(R$)':<15} {'Preço total (R$)'}")
    for i, p in enumerate(lista_produtos):
        print(f"{i:<3} {p[0]:<15} {p[1]:<5} R${p[2]:<13.2f} R${p[3]}")

print("Bem vindo ao controle de estoque!!!")

while sair != 1:
    print("1 - Cadastrar novo produto;\n 2 - excluir produto;\n 3 - Lançar/baixa;\n 4 - visualizar estoque;\n 5 - Sair")
    escolha = int(input())

    while escolha < 1 or escolha > 5:
        print("Escolha inválida, digite um número de 1 a 5!")
        escolha = int(input())

    # Cadastro de produto
    if escolha == 1:
        item = []

        print("Escreva o nome do produto:")
        nome_item = str(input())
        item.append(nome_item)

        print("Escreva a quantidade")
        qntd_item = int(input())
        item.append(qntd_item)

        print("Escreva o valor (Unidade):")
        valor_item = float(input())
        item.append(valor_item)

        valor_total = qntd_item * valor_item
        item.append(valor_total)

        lista_produtos.append(item)

        exibir_lista(lista_produtos)

    # Excluir um produto
    elif escolha == 2:
        print("Escolha um produto para excluir. OBS: 0 é o primeiro item")
        escolha = lista_produtos.pop(int(input()))

        print("\nProduto excluido, tabela atualizada!\n")

        exibir_lista(lista_produtos)

    # Lançar ou dar baixa no sistema
    elif escolha == 3:
        print("Deseja lançar ou dar baixa no sistema? 1 - Lançar; 2 - Baixa")
        escolha = int(input())

        while escolha < 1 or escolha > 2:
            print("Escolha inválida, digite um número de 1 a 2!")
            escolha = int(input())

        # lançamento no sistema
        if escolha == 1:
            nome = input("Qual produto deseja lançar? ")
            qntd = int(input("Quantidade a adicionar: "))
            for produto in lista_produtos:
                if produto[0] == nome:
                    produto[1] += qntd
                    print("Quantidade atualizada!\n")
                    exibir_lista(lista_produtos)
                    break
            else:
                print("Produto não encontrado.")
        # baixa no sistema
        elif escolha == 2:
            nome = input("Qual produto deseja dar baixa (vender)? ")
            qntd = int(input("Quantidade vendida: "))
            for produto in lista_produtos:
                if produto[0] == nome:
                    if produto[1] >= qntd:
                        produto[1] -= qntd
                        print("Venda registrada!\n")
                        exibir_lista(lista_produtos)
                    else:
                        print("Quantidade insuficiente em estoque!")
                    break
            else:
                print("Produto não encontrado.")

    # Visualizar estoque atual
    elif escolha == 4:
        print("Estoque atual")
        exibir_lista(lista_produtos)
        
        print()
        

        for p in lista_produtos:
            if p[1] < 5:
                print("produtos com menos de 5 itens: ")
                print(f"{p[0]:<15} {p[1]:<5} R${p[2]:<10.2f}")
        
    
    # Sair
    elif escolha == 5:
        print("Saindo...")
        break