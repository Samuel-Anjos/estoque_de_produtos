import pandas as pd

estoque = []
sair = 2

def cadastrar_produto():
    while True:
        print("Cadastro de Produto:")
        
        codigo = input("Código do produto: ")
        descricao = input("Descrição do produto: ")
        categoria = input("Categoria (matéria-prima / produto final): ").lower()
        unidade = input("Unidade (kg, L, un, etc.): ")

        produto = {
            "codigo": codigo,
            "descricao": descricao,
            "categoria": categoria,
            "unidade": unidade
        }

        estoque.append(produto)
        print(f"\nProduto '{descricao}' cadastrado com sucesso!\n")
        print("estoque:\n")
        print(estoque)

        continuar = input("\nDeseja cadastrar outro produto? 1 - Sim; 2 - Não, Sair!\n").lower()
        if continuar != 1:
            break


print("Bem vindo ao estoque\n")

while sair != 1:

    print("Deseja cadastrar um novo produto? 1 - Sim; 2 - Não, sair!")
    escolha = int(input())

    while escolha < 1 or escolha > 2:
            print("Escolha inválida, digite um número de 1 a 2!")
            escolha = int(input())

    if escolha == 1:
        cadastrar_produto()

        print("\nDeseja exportar os dados em excel ou CSV? 1 - Sim; 2 - Não, sair!")
        escolha = int(input())
        while escolha < 1 or escolha > 2:
            print("Escolha inválida, digite um número de 1 a 2!")
            escolha = int(input())

        if escolha == 1:
            df = pd.DataFrame(estoque)

            print("Qual opção deseja exportar? 1 - CSV; 2 - Excel")
            escolha = int(input())
            while escolha < 1 or escolha > 2:
                print("Escolha inválida, digite um número de 1 a 2!")
                escolha = int(input())

            if escolha == 1:
                nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip() + ".csv"
                df.to_csv(nome_arquivo, index=False, encoding="utf-8")
                print(f"\n Dados exportados com sucesso para '{nome_arquivo}'")

            elif escolha == 2:
                nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip() + ".xlsx"
                df.to_excel(nome_arquivo, index=False)
                print(f"\n Dados exportados com sucesso para '{nome_arquivo}'")

            else:
                print("\n Opção inválida. Nenhum arquivo foi criado.")

            
        else:
            print("Saindo...")
            break
    else:
        print("Saindo...")
        break

input("")