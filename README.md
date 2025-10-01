# Sistema de Gerenciamento de Tarefas

## Descrição do Projeto
Sistema de gerenciamento de tarefas desenvolvido em Python para a disciplina de Qualidade de Software, aplicando conceitos de controle de versão com Git e GitHub e qualidade de software conforme ISO/IEC 25010.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.x
- **Controle de Versão**: Git e GitHub
- **Armazenamento**: JSON
- **Sistema Operacional**: Windows

## Instalação e Execução

### Pré-requisitos
- Python 3.x instalado
- Git instalado

### Como executar:
```bash
# Clonar repositório
git clone https://github.com/Paiva166/projeto-qualidade-software.git

# Entrar na pasta do projeto
cd projeto-qualidade-software

# Executar aplicação
python main.py
Funcionalidades Implementadas
1. Adicionar Tarefas
Permite adicionar novas tarefas com descrição

Valida entrada vazia

Atribui ID automático

2. Listar Tarefas
Exibe todas as tarefas cadastradas

Mostra status (concluída/pendente)

Formatação clara da lista

3. Marcar como Concluída
Altera status da tarefa

Valida existência da tarefa

Impede dupla marcação

4. Excluir Tarefas
Remove tarefas do sistema

Valida existência da tarefa

Confirmação de exclusão

Qualidade de Software (ISO/IEC 25010)
1. Funcionalidade
Completude funcional: Todas as funcionalidades requisitadas foram implementadas

Correção funcional: Validações de entrada e tratamento de erros

Adequação: Atende perfeitamente ao propósito de gerenciar tarefas

2. Confiabilidade
Tolerância a falhas: Tratamento de erros em operações de arquivo

Recuperabilidade: Dados são persistidos automaticamente em JSON

Disponibilidade: Sistema sempre responde adequadamente

3. Usabilidade
Interface intuitiva: Menus claros e organização visual

Facilidade de aprendizado: Fluxo simples e direto

Experiência do usuário: Feedback imediato para todas as ações

Testes
Para executar os testes do sistema:

bash
python test_tarefas.py
Os testes verificam:

Importação do sistema

Estrutura de arquivos

Sintaxe do código

Controle de Versão
Estratégia Utilizada
Branch main: Código estável e versionado

Commits significativos: Mensagens descritivas seguindo convenção

Histórico de Commits
feat: cria sistema básico de gerenciamento de tarefas

feat: sistema completo de gerenciamento de tarefas

docs: finaliza documentação completa do projeto

Desenvolvedor
Gustavo Paiva Lima - Desenvolvimento completo do projeto