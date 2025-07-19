import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Produto:
    def __init__(self, nome, descricao, quantidade_disponivel, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco

class Venda:
    def __init__(self, produto_id, quantidade_vendida, data_venda=None, id=None):
        self.id = id
        self.produto_id = produto_id
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda or datetime.now()

class SistemaEstoque:
    def __init__(self, host, user, password, database):
        try:
            self.con = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.con.cursor(dictionary=True)
            print("Conectado ao banco de dados.")
        except Error as e:
            print(f"Erro ao conectar: {e}")
            self.con = None
            self.cursor = None

    def cadastrar_produto(self, produto: Produto):
        if self.cursor:
            sql = "INSERT INTO Produto (nome, descricao, quantidade_disponivel, preco) VALUES (%s, %s, %s, %s)"
            valores = (produto.nome, produto.descricao, produto.quantidade_disponivel, produto.preco)
            self.cursor.execute(sql, valores)
            self.con.commit()
            print(f"Produto '{produto.nome}' cadastrado com sucesso.")
        else:
            print("Cursor não disponível. Operação cancelada.")

    def listar_produtos(self):
        if self.cursor:
            self.cursor.execute("SELECT * FROM Produto")
            produtos = self.cursor.fetchall()
            return produtos
        else:
            print("Cursor não disponível.")
            return []

    def atualizar_quantidade(self, produto_id, nova_quantidade):
        if self.cursor:
            sql = "UPDATE Produto SET quantidade_disponivel = %s WHERE id = %s"
            self.cursor.execute(sql, (nova_quantidade, produto_id))
            self.con.commit()
            print(f"Quantidade do produto ID {produto_id} atualizada para {nova_quantidade}.")
        else:
            print("Cursor não disponível. Operação cancelada.")

    def remover_produto(self, produto_id):
        if self.cursor:
            sql = "DELETE FROM Produto WHERE id = %s"
            self.cursor.execute(sql, (produto_id,))
            self.con.commit()
            print(f"Produto ID {produto_id} removido do cadastro.")
        else:
            print("Cursor não disponível. Operação cancelada.")

    def fechar_conexao(self):
        if self.con and self.con.is_connected():
            self.cursor.close()
            self.con.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    # Configure aqui suas credenciais do banco MySQL
    sistema = SistemaEstoque(host="localhost", user="seu_usuario", password="sua_senha", database="sistema_estoque")

    # Exemplo básico de uso
    p1 = Produto(nome="Teclado", descricao="Teclado mecânico RGB", quantidade_disponivel=10, preco=150.00)
    sistema.cadastrar_produto(p1)

    produtos = sistema.listar_produtos()
    print("Produtos cadastrados:")
    for p in produtos:
        print(p)

    if produtos:
        sistema.atualizar_quantidade(produtos[0]['id'], 20)

    if produtos:
        sistema.remover_produto(produtos[0]['id'])

    sistema.fechar_conexao()
