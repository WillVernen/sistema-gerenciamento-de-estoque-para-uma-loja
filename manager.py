# manager.py

# Este arquivo contém a lógica de negócios e as funções para gerenciar o estoque.
# Ele interage com o banco de dados e com os modelos.

# Importamos a função para obter a conexão com o banco de dados.
from database import get_db_connection
# Importamos a classe Produto para poder criar objetos Produto.
from models import Produto


def cadastrar_produto(nome, descricao, quantidade, preco):
    """
    Função para inserir um novo produto na tabela 'produtos'.

    Recebe os detalhes do produto como argumentos e os salva no banco de dados.
    """
    # Primeiro, obtemos uma conexão com o banco.
    conexao = get_db_connection()
    try:
        cursor = conexao.cursor()

        # Este é o comando SQL para inserir dados.
        # Usamos '?' como placeholders. Esta é a maneira segura de passar variáveis
        # para um comando SQL, evitando um problema de segurança chamado 'SQL Injection'.
        sql = "INSERT INTO produtos (nome, descricao, quantidade, preco) VALUES (?, ?, ?, ?)"

        # Executamos o comando, passando uma tupla com os valores na ordem dos placeholders.
        cursor.execute(sql, (nome, descricao, quantidade, preco))

        # Salvamos (commit) a transação.
        conexao.commit()

        print(f"Produto '{nome}' cadastrado com sucesso!")

    except Exception as e:
        # Se ocorrer qualquer erro, imprimimos o erro.
        print(f"Ocorreu um erro ao cadastrar o produto: {e}")

    finally:
        # Independentemente de ter dado certo ou errado, fechamos a conexão.
        conexao.close()


def consultar_produtos():
    """
    Função para buscar e retornar todos os produtos cadastrados no banco de dados.

    Retorna uma lista de objetos da classe Produto.
    """
    conexao = get_db_connection()
    cursor = conexao.cursor()

    # Comando SQL para selecionar TODAS as colunas (*) da tabela 'produtos'.
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)

    # cursor.fetchall() busca todos os resultados da consulta.
    # Cada resultado é uma 'Row' (linha) que se parece com um dicionário.
    resultados = cursor.fetchall()

    # Lista onde vamos guardar nossos objetos Produto
    produtos = []
    for resultado in resultados:
        # Para cada linha de resultado do banco, criamos um objeto da classe Produto.
        # Isso transforma os dados do banco em objetos Python, com os quais é mais fácil trabalhar.
        produto = Produto(id=resultado['id'], nome=resultado['nome'], descricao=resultado['descricao'],
                          quantidade=resultado['quantidade'], preco=resultado['preco'])
        produtos.append(produto)

    conexao.close()
    return produtos


def atualizar_estoque(produto_id, nova_quantidade):
    """
    Atualiza a quantidade em estoque de um produto específico.
    """
    conexao = get_db_connection()
    try:
        cursor = conexao.cursor()

        # Comando SQL para ATUALIZAR (UPDATE) a tabela 'produtos'.
        # SET quantidade = ? -> Define o novo valor para a coluna 'quantidade'.
        # WHERE id = ? -> Especifica QUAL produto deve ser atualizado. Isso é MUITO importante!
        sql = "UPDATE produtos SET quantidade = ? WHERE id = ?"

        cursor.execute(sql, (nova_quantidade, produto_id))
        conexao.commit()

        # cursor.rowcount nos diz quantas linhas foram afetadas pelo último comando.
        if cursor.rowcount > 0:
            print(
                f"Estoque do produto ID {produto_id} atualizado para {nova_quantidade}.")
        else:
            print(f"Produto com ID {produto_id} não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o estoque: {e}")

    finally:
        conexao.close()


def remover_produto(produto_id):
    """
    Remove um produto do banco de dados usando seu ID.
    """
    conexao = get_db_connection()
    try:
        cursor = conexao.cursor()

        # Comando SQL para DELETAR (DELETE) uma linha da tabela 'produtos'.
        # A cláusula WHERE é crucial para não apagar todos os produtos!
        sql = "DELETE FROM produtos WHERE id = ?"

        # A vírgula é necessária para que o Python entenda que é uma tupla.
        cursor.execute(sql, (produto_id,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Produto com ID {produto_id} foi removido com sucesso.")
        else:
            print(f"Produto com ID {produto_id} não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro ao remover o produto: {e}")

    finally:
        conexao.close()
