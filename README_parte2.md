# Engenharia-de-Software-AV2-Parte2
## Tarefa 2.1, Definição da Arquitetura
O padrão arquitetural MVC (Model-View-Controller) foi escolhido para o desenvolvimento do sistema de gerenciamento da atlética devido à sua capacidade de organizar e separar as responsabilidades da aplicação. 
Como o sistema possui funcionalidades relacionadas a cadastro, gerenciamento de informações e controle de usuários, a divisão em camadas facilita a manutenção, compreensão e expansão do código.

No padrão MVC, cada componente possui uma responsabilidade específica, permitindo que a lógica de negócio, a interface do usuário e o controle das ações fiquem separados. 
Essa organização torna o sistema mais estruturado, reduz o acoplamento entre as partes do código e facilita futuras alterações e correções. 
Além disso, a separação em classes e responsabilidades contribui para uma maior segurança e melhor reutilização do código durante o desenvolvimento do projeto.

### Relacionamentos dos componentes principais

O sistema será constituído pelos componentes View, Controller e Model, seguindo o padrão arquitetural MVC (Model-View-Controller).

O conjunto de classes da camada View terá como objetivo representar a interface do sistema, sendo responsável por toda a interação com o usuário.
Nessa camada estarão presentes as telas, formulários, menus e demais elementos visuais que permitem ao usuário visualizar informações e executar ações dentro da aplicação.

A camada Controller será responsável pelo controle das funcionalidades do sistema e pelo processamento das ações realizadas pelos usuários.
Seu objetivo é intermediar a comunicação entre a interface e as regras de negócio, recebendo dados da View, processando as solicitações e encaminhando as operações necessárias para a camada Model.

Já a camada Model será responsável pelo gerenciamento dos dados e pela comunicação com o banco de dados. 
Nela estarão localizadas as classes que representam as entidades do sistema, além das regras relacionadas ao armazenamento, manipulação e organização das informações utilizadas pela aplicação.

### Limitações do MVC
Em aplicações de pequeno porte, a utilização do padrão MVC pode aumentar desnecessariamente a complexidade do projeto, devido à grande quantidade de arquivos, classes e camadas exigidas pela arquitetura. 
Embora o padrão proporcione melhor organização e manutenção do código, sua estrutura pode tornar o desenvolvimento inicial mais trabalhoso e difícil de gerenciar em sistemas mais simples.

### Minha reflexão:
Tenho preferência pela utilização do padrão MVC, pois ele proporciona maior organização e clareza na estrutura do código. 
A separação das responsabilidades entre as camadas facilita o entendimento do sistema, permitindo identificar com mais facilidade onde cada funcionalidade, regra de negócio ou componente da interface deve estar localizado.

## Tarefa 2.2, Implementação com Padrões de Projeto

### Padrão Singleton
#### Categoria
O padrão Singleton pertence à categoria de padrões criacionais, pois é responsável por controlar a criação de objetos, garantindo que exista apenas uma única instância de determinada classe durante a execução do sistema.
┌─────────────────────┐
│      Database       │
├─────────────────────┤
│ - _instance         │
│ - conn              │
│ - cursor            │
├─────────────────────┤
│ + __new__()         │
│ + get_connection()  │
│ + get_cursor()      │
└─────────────────────┘
           ▲
           │
           │ utiliza
           │
┌─────────────────────┐
│  AtletaController   │
└─────────────────────┘

### Padrão Factory
#### Categoria 
O padrão Factory pertence à categoria de padrões criacionais, pois tem como objetivo centralizar e controlar a criação de objetos do sistema.
┌─────────────────────────┐
│     UsuarioFactory      │
├─────────────────────────┤
│ + criar_usuario()       │
└─────────────────────────┘
              │
              │ cria
              ▼
┌─────────────────────────┐
│         Atleta          │
├─────────────────────────┤
│ - id                    │
│ - nome                  │
│ - ra                    │
│ - curso                 │
│ - telefone              │
└─────────────────────────┘
              ▲
              │ utiliza
              │
┌─────────────────────────┐
│    AtletaController     │
└─────────────────────────┘
