# models.py

# Neste arquivo, definimos as estruturas de dados do nosso sistema usando Classes.
# Uma classe é como uma planta baixa ou um molde para criar objetos.

class Produto:
    """
    Esta classe representa um Produto da nossa loja.
    Os atributos desta classe (id, nome, etc.) correspondem diretamente
    às colunas que criamos na nossa tabela 'produtos' no banco de dados.
    """

    def __init__(self, nome, descricao, quantidade, preco, id=None):
        """
        O método __init__ é o "construtor". Ele é chamado automaticamente
        sempre que criamos um novo objeto a partir desta classe.

        Ele serve para definir os valores iniciais dos atributos do objeto.
        """
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        """
        O método __str__ define uma representação em texto do objeto.
        Quando tentarmos "imprimir" um objeto Produto, é este texto que aparecerá.
        É extremamente útil para mostrar os dados para o usuário de forma amigável.
        O ':.2f' no preço formata o número para sempre ter duas casas decimais.
        """
        return f"ID: {self.id} | Produto: {self.nome} | Qtd: {self.quantidade} | Preço: R$ {self.preco:.2f}"


class Venda:
    """
    Esta classe representa uma transação de Venda na loja.
    """

    def __init__(self, produto_id, quantidade_vendida, id=None, data_venda=None):
        """
        Construtor da classe Venda.
        """
        self.id = id
        self.produto_id = produto_id
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda

    def __str__(self):
        """
        Representação em texto de um objeto Venda.
        """
        return f"Venda ID: {self.id} | Produto ID: {self.produto_id} | Qtd: {self.quantidade_vendida} | Data: {self.data_venda}"
