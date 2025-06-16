# main.py

# Este é o arquivo principal, a porta de entrada do nosso programa.
# Ele é responsável por exibir o menu e interagir com o usuário.

# Importamos as funções que criamos no nosso módulo gerenciador.
# Damos a ele o apelido de 'manager' para facilitar a chamada das funções.
import manager
import time  # Usaremos para dar uma pequena pausa no programa
import database


def exibir_menu():
    """
    Função dedicada a apenas mostrar as opções do menu.
    """
    print("\n--- Sistema de Gerenciamento de Estoque ---")
    print("1. Cadastrar Novo Produto")
    print("2. Consultar Todos os Produtos")
    print("3. Atualizar Estoque de um Produto")
    print("4. Remover Produto")
    print("5. Sair")
    print("-----------------------------------------")


def main():
    """
    Função principal que executa o loop do programa.
    """
    while True:
        exibir_menu()

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            # --- CADASTRAR PRODUTO ---
            print("\n-> Cadastrando Novo Produto...")
            try:
                nome = input("Nome do produto: ")
                descricao = input("Descrição do produto: ")
                quantidade = int(input("Quantidade em estoque: "))
                preco = float(input("Preço (ex: 10.50): "))

                # Chama a função do manager para efetivamente cadastrar
                manager.cadastrar_produto(nome, descricao, quantidade, preco)

            except ValueError:
                # Se o usuário digitar um texto onde deveria ser um número
                print("Erro: Quantidade e preço devem ser números. Tente novamente.")

        elif escolha == '2':
            # --- CONSULTAR PRODUTOS ---
            print("\n-> Consultando Todos os Produtos...")
            produtos = manager.consultar_produtos()

            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                # O __str__ da classe Produto que criamos em models.py formata a exibição!
                for produto in produtos:
                    print(produto)

        elif escolha == '3':
            # --- ATUALIZAR ESTOQUE ---
            print("\n-> Atualizando Estoque...")
            try:
                id_produto = int(
                    input("Digite o ID do produto que deseja atualizar: "))
                nova_quantidade = int(
                    input("Digite a nova quantidade em estoque: "))

                manager.atualizar_estoque(id_produto, nova_quantidade)

            except ValueError:
                print(
                    "Erro: ID e quantidade devem ser números inteiros. Tente novamente.")

        elif escolha == '4':
            # --- REMOVER PRODUTO ---
            print("\n-> Removendo Produto...")
            try:
                id_produto = int(
                    input("Digite o ID do produto que deseja remover: "))

                manager.remover_produto(id_produto)

            except ValueError:
                print(
                    "Erro: O ID do produto deve ser um número inteiro. Tente novamente.")

        elif escolha == '5':
            # --- SAIR DO SISTEMA ---
            print("Saindo do sistema... Até logo!")
            break  # 'break' encerra o loop 'while'

        else:
            # --- OPÇÃO INVÁLIDA ---
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

        # Pausa para o usuário poder ler a saída antes do menu ser exibido novamente
        print("\n")
        time.sleep(1)  # Espera 1 segundo


# A linha abaixo garante que a função main() só seja executada
# quando o arquivo main.py for rodado diretamente.
if __name__ == '__main__':
    # Antes de iniciar o programa, vamos garantir que o banco e as tabelas existem.
    # Não tem problema rodar isso toda vez, pois nosso comando é 'CREATE TABLE IF NOT EXISTS'.
    database.criar_banco_de_dados()
    main()
