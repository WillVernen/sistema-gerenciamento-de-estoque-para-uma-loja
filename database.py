# database.py (VERSÃO CORRIGIDA E COMPLETA)

import sqlite3

DATABASE_NAME = 'estoque.db'


def get_db_connection():
    """
    Cria e retorna uma conexão com o banco de dados.
    Esta é a função que será usada por todo o sistema para obter acesso ao banco.
    """
    conexao = sqlite3.connect(DATABASE_NAME)

    # Esta linha é MUITO importante! Ela faz com que os resultados das consultas
    # venham em um formato que permite acessar as colunas pelo nome.
    # Ex: resultado['nome'] ao invés de resultado[1]
    conexao.row_factory = sqlite3.Row

    return conexao


def criar_banco_de_dados():
    """
    Cria as tabelas do banco de dados se elas ainda não existirem.
    """
    print("Verificando e criando tabelas, se necessário...")
    # Agora a função de criar o banco também usa a nossa função de conexão padrão
    conexao = get_db_connection()
    cursor = conexao.cursor()

    # Criação da Tabela de Produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        );
    ''')

    # Criação da Tabela de Vendas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            quantidade_vendida INTEGER NOT NULL,
            data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
        );
    ''')

    conexao.commit()
    conexao.close()
    print("Banco de dados pronto para uso.")


if __name__ == '__main__':
    criar_banco_de_dados()
