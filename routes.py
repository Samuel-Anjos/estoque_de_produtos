from flask import render_template
from main import app, get_connection

@app.route("/")
def home():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM produto")
        produtos = cursor.fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

@app.route("/produtos")
def produtos():
    return render_template("produto.html")

@app.route("/ingredientes")
def ingredientes():
    return render_template("ingredientes.html")

@app.route("/baixa")
def baixa():
    return render_template("baixa.html")

@app.route("/venda")
def venda():
    return render_template("venda.html")

@app.route("/add_ingrediente")
def add_ingrediente():
    return render_template("add-ingrediente.html")

@app.route("/editar-produto/<int:id>")
def editar_produto(id):
    # edição do banco de dados (colocar lógica em breve)
    # return render_template("editar-produto.html", id=id)
    pass

@app.route("/excluir-produto/<int:id>")
def excluir_produto(id):
    # exclusão do banco de dados(colocar lógica em breve)
    # return redirect(url_for("produtos"))
    pass