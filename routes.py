from flask import render_template, request, redirect, url_for
from main import app, get_connection
from datetime import datetime

@app.route("/")
def home():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM produto WHERE ativo = TRUE")
        produtos = cursor.fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)


@app.route("/produtos", methods=["GET", "POST"])
def produtos():
    conn = get_connection()
    if request.method == "POST":
        nome_produto = request.form.get("nomeProduto")
        quantidade = request.form.get("quantidade")
        valor_unitario = request.form.get("valorUnitario")

        quantidade = float(quantidade)
        valor_unitario = float(valor_unitario)
        valor_total = valor_unitario * quantidade
        data_cadastro = datetime.now()

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO produto (nome_produto, valor_produto, quantidade, custo, data_cadastro) 
                VALUES (%s, %s, %s, %s, %s)""", (nome_produto, valor_unitario, quantidade, valor_total, data_cadastro))
            conn.commit()
        conn.close()

    return render_template("produto.html")


@app.route("/ingredientes")
def ingredientes():
    return render_template("ingredientes.html")

@app.route("/baixa")
def baixa():
    return render_template("baixa.html")

@app.route("/venda", methods=["GET", "POST"])
def venda():
    conn = get_connection()
    if request.method == "POST":
        id_produto = request.form.get("id_produto")
        quantidade_vendida = float(request.form.get("quantidade"))
        valor_venda_unitario = float(request.form.get("valorUnitario"))
        valor_total = valor_venda_unitario * quantidade_vendida
        data_venda = datetime.now()

        with conn.cursor() as cursor:
            # SELECT pra diminuir a quantidade na outra tabela
            cursor.execute("SELECT quantidade, valor_produto FROM produto WHERE id_produto = %s", (id_produto,))
            produto = cursor.fetchone()

            if not produto:
                print("Produto não encontrado!")
                return redirect(url_for("venda"))

            estoque_atual = float(produto["quantidade"])
            valor_unitario_produto = float(produto["valor_produto"])

            if estoque_atual < quantidade_vendida:
                print("Estoque insuficiente para a venda!")
                return redirect(url_for("venda"))

            novo_estoque = estoque_atual - quantidade_vendida
            novo_custo = valor_unitario_produto * novo_estoque

            cursor.execute(
                "UPDATE produto SET quantidade = %s, custo=%s WHERE id_produto = %s",
                (novo_estoque, novo_custo, id_produto)
            )

            cursor.execute("""
                INSERT INTO registro_vendas (id_produto, data_venda, quantidade_vendida, valor_venda_unitario, 
                valor_total)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_produto, data_venda,  quantidade_vendida, valor_venda_unitario, valor_total))
            conn.commit()

            conn.close()

        return redirect(url_for("venda"))

    with conn.cursor() as cursor:
        cursor.execute("SELECT id_produto, nome_produto FROM produto WHERE ativo = TRUE")
        produtos = cursor.fetchall()
    conn.close()
    return render_template("venda.html", produtos=produtos)


@app.route("/add_ingrediente", methods=["GET", "POST"])
def add_ingrediente():
    conn = get_connection()
    if request.method == "POST":
        nome_ingrediente = request.form.get("nome_ingrediente")
        unidade_medida = request.form.get("unidade_medida")
        custo_unitario = request.form.get("custo_unitario")

        custo_unitario = float(custo_unitario)
        data_cadastro = datetime.now()

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO producao (nome_ingrediente, unidade_medida, custo_unitario, data_cadastro) 
                VALUES (%s, %s, %s, %s)""", (nome_ingrediente, unidade_medida, custo_unitario, data_cadastro))
            conn.commit()
        conn.close()

    return render_template("add-ingrediente.html")

@app.route("/editar-produto/<int:id>")
def editar_produto(id):
    # edição do banco de dados (colocar lógica em breve)
    # return render_template("editar-produto.html", id=id)
    pass

@app.route("/excluir-produto/<int:id>")
def excluir_produto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE produto SET ativo = FALSE WHERE id_produto = %s", (id,))
    conn.commit()
    cursor.close()
    return redirect(url_for("home"))