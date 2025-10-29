import pandas as pd
from openpyxl import load_workbook

estoque = []
sair = 2

def cadastrar_produto():
    while True:
        print("Cadastro de Produto:")
        
        codigo = str(input("Código do produto: "))
        descricao = str(input("Descrição do produto: ").strip().capitalize())

        for item in estoque:
            if item["Descrição do Item"].lower() == descricao.lower():
                print("Produto já cadastrado no sistema.")
                return


        print("\nSelecione a categoria do produto:")
        print("1 - Matéria-prima (ingredientes para produção)")
        print("2 - Produto acabado (doces prontos para venda)")

        categoria_opcao = input("Escolha 1 ou 2: ").strip()

        while categoria_opcao not in ["1", "2"]:
            print("Opção inválida! Digite 1 ou 2.")
            categoria_opcao = input("Escolha 1 ou 2: ").strip()

        if categoria_opcao == "1":
            categoria = "matéria-prima"
        else:
            categoria = "produto acabado"


        while True:
            try:
                quantidade = int(input("Quantidade inicial: "))
                if quantidade < 0:
                    print("A quantidade não pode ser negativa.")
                    continue
                break
            except ValueError:
                print("Digite um número válido.")

        unidade = str(input("Unidade (kg, litro, unidade, etc.): ").lower())
        valor_unitario = float(input("Valor unitário (quanto vale uma unidade)"))
        valor_total = valor_unitario * quantidade

        produto = {
            "Código": codigo,
            "Descrição do Item": descricao,
            "Categoria": categoria,
            "Unidade": unidade,
            "Quantidade": quantidade,
            "Valor Unitário (R$)": valor_unitario,
            "Valor Total (R$)": valor_total
        }

        estoque.append(produto)
        print(f"\nProduto '{descricao}' cadastrado com sucesso!\n")

        continuar = input("\nDeseja cadastrar outro produto? 1 - Sim; 2 - Não, Sair!\n").lower()
        if continuar == 1:
            cadastrar_produto()
        else:
            print("Saindo...")
            return

def registrar_entrada():
    nome_produto = str(input("Qual produto deseja lançar no sistema: "))
    quantidade = int(input("Qual a quantidade: "))

    encontrado = False

    for item in estoque:
        if item["descricao"].lower() == nome_produto.lower():
            item["quantidade"] += quantidade
            print("Quantidade atualizada")
            break
    
    if not encontrado:
        print("Produto não encontrado")

def registrar_saida():
    nome_produto = str(input("Qual produto deseja dar baixa no sistema: "))
    quantidade = int(input("Qual a quantidade: "))

    encontrado = False

    for item in estoque:
        if item["descricao"].lower() == nome_produto.lower():
            item["quantidade"] -= quantidade
            print("Quantdade atualizada")
            break

    if not encontrado:
        print("Produto não encontrado")

def mostrar_estoque():
    print("estoque: ")
    print(estoque)


def exportar_arquivo():
    sair = 0

    nome_arquivo = input("Digite o nome do arquivo Excel que deseja carregar (sem extensão): ").strip() + ".xlsx"

    try:
        planilhas = pd.read_excel(nome_arquivo, sheet_name=None)
        producao_df = planilhas["PRODUÇÃO"]
        produto_acabado_df = planilhas["PRODUTO_ACABADO"]
        print(f"Planilhas carregadas com sucesso a partir de '{nome_arquivo}'!")

        workbook = load_workbook(nome_arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo antes de exportar.")
        return

        
    while sair != 1:


        print("\nDeseja exportar os dados em excel ou CSV? 1 - Sim; 2 - Não, sair!")
        escolha = int(input())

        while escolha not in [1, 2]:
            print("Escolha inválida, digite um número de 1 a 2!")
            escolha = int(input())

        if escolha == 1:

            df = pd.DataFrame(estoque)

            # Divide em duas categorias
            df_producao = df[df["Categoria"].str.lower().isin(["matéria-prima", "materia-prima", "produção"])]
            df_produto_acabado = df[df["Categoria"].str.lower().isin(["produto acabado", "acabado"])]

            # --- Limpa duplicatas por descrição ---
            producao_df = pd.concat([producao_df, df_producao], ignore_index=True)
            producao_df = producao_df.drop_duplicates(subset="Descrição do Item", keep="last")

            produto_acabado_df = pd.concat([produto_acabado_df, df_produto_acabado], ignore_index=True)
            produto_acabado_df = produto_acabado_df.drop_duplicates(subset="Descrição do Item", keep="last")

            print("Qual opção deseja exportar?")
            print("1 - CSV; 2 - Excel")
            formato = int(input())


            while formato not in [1, 2]:
                print("Escolha inválida, digite um número de 1 a 2!")
                escolha = int(input())

            if formato == 1:
                producao_df.to_csv("PRODUCAO.csv", index=False, encoding="utf-8")
                produto_acabado_df.to_csv("PRODUTO_ACABADO.csv", index=False, encoding="utf-8")
                print("\nArquivos CSV exportados com sucesso!")

            elif formato == 2:
                with pd.ExcelWriter(nome_arquivo, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                    producao_df = producao_df.loc[:,~producao_df.columns.duplicated()]
                    produto_acabado_df = produto_acabado_df.loc[:,~produto_acabado_df.columns.duplicated()]

                    producao_df.to_excel(writer, index=False, sheet_name="PRODUÇÃO")
                    produto_acabado_df.to_excel(writer, index=False, sheet_name="PRODUTO_ACABADO")
                print("\nPlanilha Excel atualizada com sucesso!")

            else:
                print("\nOpção inválida. Nenhum arquivo foi criado.")

                
        else:
            print("Saindo...")
            
        sair = 1

    


def menu():
    while True:
        print("Bem vindo ao estoque")
        print("Escolha um das opções do menu:\n")
        print("1) Cadastrar novo produto")
        print("2) Registrar entrada")
        print("3) Registrar saída")
        print("4) Consultar estoque")
        print("5) Exportar arquivo")
        print("0) Sair")

        opcao = input("Escolha: ")
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            registrar_entrada()
        elif opcao == "3":
            registrar_saida()
        elif opcao == "4":
            mostrar_estoque()
        elif opcao == "5":
            exportar_arquivo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção invalida, digite novamente.")

menu()