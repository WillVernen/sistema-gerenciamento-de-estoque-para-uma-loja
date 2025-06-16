# PROJETO DE UM SISTEMA DE GERENCIAMENTO DE ESTOQUE PARA UMA LOJA

## Tecnologias: Python e sqlite3

### Objetivos:
- Cria um banco de dados
- Cria uma tabela Produtos e outra tabela Vendas
- Cadastrar produtos
- Consultar produtos
- Atualizar o estoque
- Remover produtos

### Como usar:
* Criando o Banco de Dados:
  - Crie uma pasta `gerenciador_estoque` para salvar os arquivos do VS Code
  - Abrir o arquivo salvo database.py
  - Abrir o terminal e digitar: python database.py
  - Você verá as mensagens de sucesso no terminal. E o mais importante: olhe para a sua lista de arquivos no VS Code. Um novo arquivo chamado estoque.db terá aparecido.
   
* Executando o Programa: 
  - Para rodar o programa abra o terminal no VS Code, dentro da pasta gerenciador estoque e digite o comando e pressione enter: python main.py

### Adições Futuras:
1. Implementar a Venda: Crie as opções no menu e as funções no manager.py para registrar uma venda. Ao vender um produto, lembre-se de que a quantidade em estoque dele deve diminuir!
2. Relatórios: Crie uma nova opção no menu para "Ver Relatório de Vendas", que consultaria a tabela vendas.
3. Validações: Melhore as validações. Por exemplo, não permita cadastrar um produto com quantidade ou preço negativos. Não permita vender mais produtos do que existem em estoque.
