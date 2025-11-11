from flask import render_template, redirect, url_for, Blueprint

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/produtos")
def produtos():
    return render_template("produto.html")

@bp.route("/ingredientes")
def ingredientes():
    return render_template("ingredientes.html")

@bp.route("/baixa")
def baixa():
    return render_template("baixa.html")

@bp.route("/venda")
def venda():
    return render_template("venda.html")

@bp.route("/add_ingrediente")
def add_ingrediente():
    return render_template("add-ingrediente.html")

@bp.route("/editar-produto/<int:id>")
def editar_produto(id):
    # edição do banco de dados (colocar lógica em breve)
    # return render_template("editar-produto.html", id=id)
    pass

@bp.route("/excluir-produto/<int:id>")
def excluir_produto(id):
    # exclusão do banco de dados(colocar lógica em breve)
    # return redirect(url_for("produtos"))
    pass