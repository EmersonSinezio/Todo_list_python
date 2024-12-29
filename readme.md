# To-Do List App

Este é um esboço de um aplicativo de lista de tarefas (to-do list) desenvolvido em Python. O objetivo deste projeto é fornecer uma base funcional para gerenciar tarefas, permitindo adicionar, visualizar, marcar como concluídas e remover tarefas.

## Funcionalidades

- **Adicionar Tarefa**: Permite adicionar uma nova tarefa à lista.
- **Mostrar Tarefas**: Exibe todas as tarefas, indicando se estão concluídas ou pendentes.
- **Marcar Tarefa como Concluída**: Permite marcar uma tarefa específica como concluída usando seu ID.
- **Remover Tarefa**: Permite remover uma tarefa específica usando seu ID.

## Estrutura do Projeto

- `main.py`: Arquivo principal que executa o menu e as opções do usuário.
- `models/todo.py`: Contém a classe `Todo` responsável pelas operações principais de gerenciamento de tarefas.
- `views/todo_view.py`: Contém as funções de exibição e interação com o usuário.

## Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/todo-list-app.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd todo-list-app
   ```

3. Execute o aplicativo:
   ```bash
   python main.py
   ```

## Exemplo de Uso

Ao executar o aplicativo, você verá um menu com as seguintes opções:

--- To-Do List --- 1 - Adicionar tarefa 2 - Mostrar todas as tarefas 3 - Marcar tarefa como concluída 4 - Remover tarefa 5 - Sair

Escolha uma opção digitando o número correspondente e siga as instruções.

## Observações

Este projeto é um esboço inicial e está sujeito a modificações. Pretendo adicionar mais funcionalidades e melhorar a interface do usuário no futuro.
