## Padrão de Commits com Emojis 🎉

Este guia define um padrão de commits para facilitar a comunicação e a organização do histórico de alterações do projeto. Vc pode usar emojis para tornar a leitura do histórico mais agradável e intuitiva.

### Tipos de Commits

Utilizaremos os seguintes tipos de commits para categorizar as alterações:

| Emoji | Tipo       | Descrição                                            |
| :---: | :--------- | :------------------------------------------------- |
| 🐛    | **fix**    | Corrige um bug                                    |
| ✨    | **feat**   | Adiciona uma nova funcionalidade                     |
| 🎨    | **refactor** | Refatora código sem adicionar novas funcionalidades |
| 🧪    | **test**   | Adiciona ou altera testes                           |
| 📝    | **docs**   | Altera a documentação                               |
| 🏗️    | **build**   | Altera o sistema de build                          |
| 📦    | **chore**   | Altera tarefas que não se encaixam em outras categorias |
| 🗑️    | **remove**  | Remove código ou arquivos                          |
| 🔒    | **security** | Corrige uma vulnerabilidade de segurança           |

### Formato do Commit

O formato do commit deve seguir a seguinte estrutura:
Use code with caution.

```Markdown
<tipo>(<opcional: escopo>): <mensagem curta>

<opcional: corpo da mensagem>

<opcional: referência a um problema ou tarefa>
```

**Exemplo:**

```Md
Use code with caution.
feat(api): Adiciona endpoint para buscar usuários

Adiciona um novo endpoint na API para buscar informações de usuários.

Fixes #123
```

### Detalhes do Commit

* **Tipo:** Define o tipo de alteração feita (ex: `fix`, `feat`, `refactor`).
* **Escopo (opcional):** Fornece mais contexto sobre a área do código que foi alterada (ex: `api`, `components`, `database`).
* **Mensagem curta:** Uma breve descrição da alteração (máximo de 50 caracteres).
* **Corpo da mensagem (opcional):** Fornece mais detalhes sobre a alteração, incluindo justificativa, código antes e depois da alteração, etc.
* **Referências (opcional):** Liga o commit a um problema ou tarefa (ex: `Fixes #123`).

### Emojis

Além do tipo de commit, podemos usar emojis para tornar o histórico de alterações mais visualmente interessante. Use os emojis listados na tabela acima para representar o tipo de commit.

### Exemplos de Commits

```Md
feat(auth): Adiciona autenticação de usuário 🔐

Adiciona a funcionalidade de autenticação de usuário por email e senha.

Fixes #25
```

```Md
fix(api): Corrige erro de retorno da API 🐛

Corrige um erro que causava o retorno de dados inválidos para a API.
```
```Md
docs(README): Atualiza a documentação do projeto 📝

Atualiza o arquivo README.md com novas informações sobre a instalação e uso do projeto.
```

### Vantagens de Usar um Padrão de Commits

* **Comunicação:** Torna o histórico de alterações mais fácil de entender e navegar.
* **Organização:** Categoriza as alterações de forma lógica, facilitando a pesquisa por commits específicos.
* **Automação:** Permite automatizar tarefas como a geração de logs e a criação de releases.

### Ferramentas que Suportam Emojis em Commits

* **GitHub:** Suporta emojis no histórico de alterações.
* **GitLab:** Suporta emojis no histórico de alterações.
* **Bitbucket:** Suporta emojis no histórico de alterações.

### Dicas Adicionais

* Use frases curtas e concisas para a mensagem do commit.
* Evite usar frases como "Fixes", "Adds", "Implements" no início da mensagem.
* Documente as alterações de forma clara e concisa.
* Mantenha o histórico de alterações organizado e limpo.


bjs bjs eh issooo!!!