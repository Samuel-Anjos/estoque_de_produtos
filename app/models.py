from app import db
from datetime import datetime

class Produto(db.Model):
    __tablename__ = 'produto'
    id_produto = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(255), nullable=False, unique=True)
    valor_produto = db.Column(db.Numeric(10, 2), nullable=False)
    quantidade = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    custo = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)

    vendas = db.relationship('RegistroVendas', backref='produto', lazy=True)

    def __repr__(self):
        return f'<Produto {self.nome_produto}>'

class Producao(db.Model):
    __tablename__ = 'producao'
    id_producao = db.Column(db.Integer, primary_key=True)
    nome_ingrediente = db.Column(db.String(255), nullable=False)
    unidade_medida = db.Column(db.String(10), nullable=False)
    custo_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Producao {self.nome_ingrediente}>'

class RegistroVendas(db.Model):
    __tablename__ = 'registro_vendas'
    id_venda = db.Column(db.Integer, primary_key=True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id_produto'), nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    quantidade_vendida = db.Column(db.Numeric(10, 2), nullable=False)
    valor_venda_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    custo_venda_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<Venda {self.id_venda}>'
