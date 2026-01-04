
'''
#  pyenv e como criar um ambiente virtual com ele
O pyenv é uma ferramenta que permite gerenciar múltiplas versões do Python em um sistema operacional.
Ele facilita a instalação e a troca entre diferentes versões do Python, sendo útil para desenvolvedores
que trabalham com projetos que exigem versões específicas do Python.

Para criar um ambiente virtual com o pyenv:

1. Instale o pyenv seguindo as instruções oficiais para seu sistema operacional.
2. Use o comando `pyenv install <versao>` para instalar uma versão específica do Python.
3. Use `pyenv global <versao>` para definir a versão padrão do Python.
4. Para criar um ambiente virtual, utilize o comando `python -m venv <nome_do_ambiente>` dentro do diretório do projeto.
5. Ative o ambiente virtual com `source <nome_do_ambiente>/bin/activate` no Linux/Mac ou `<nome_do_ambiente>\Scripts\activate` no Windows.

Isso permite que você tenha diferentes versões do Python instaladas e use ambientes virtuais isolados para cada projeto,
evitando conflitos entre dependências.

VERIFIQUE A INSTALAÇÃO DO PYENV:
pyenv --version
pyenv versions
pyenv install 3.12.1
    3.11.3
    3.11.5
    * 3.11.9 (set by C:\Users\Diego\.pyenv\pyenv-win\version)
    3.12.1
    3.12.6
pyenv global 3.12.1

Atruibuições da versão do pytohn para o projeto:
django pyenv local 3.11.9
pandas pyenv local 3.12.1
streanlit pyenv local 3.12.6

'''

'''
# entendimento do PIP (Python Improvement Proposal)
PIP é o gerenciador de pacotes padrão do Python. Ele permite instalar e gerenciar bibliotecas e dependências que não fazem parte da instalação padrão do Python.

Comandos básicos do PIP:
- pip install <nome_do_pacote>: Instala um pacote.
- pip list: Lista todos os pacotes instalados.
- pip show <nome_do_pacote>: Mostra informações sobre um pacote específico.
- pip uninstall <nome_do_pacote>: Desinstala um pacote.
- pip freeze > requirements.txt: Gera um arquivo com todas as dependências instaladas.

O arquivo requirements.txt é usado para manter o controle das dependências de um projeto, permitindo que outros desenvolvedores recriem o mesmo ambiente de desenvolvimento.

Exemplo de conteúdo de requirements.txt:
django==4.2.0
pandas==1.5.3
numpy==1.24.0

Isso garante que todos os desenvolvedores estejam usando as mesmas versões das bibliotecas.
'''

'''
# entendimento do VENV (Virtual Environment)

O VENV (Virtual Environment) é uma ferramenta que permite criar ambientes Python isolados.
Cada ambiente virtual tem seu próprio conjunto de pacotes e dependências,
o que evita conflitos entre diferentes projetos.
Para criar um ambiente virtual com VENV:
1. Navegue até o diretório do seu projeto.
2. Execute o comando: python -m venv nome_do_ambiente
3. Ative o ambiente virtual:
   - No Windows: nome_do_ambiente\Scripts\activate
   - No Linux/Mac: source nome_do_ambiente/bin/activate
4. Instale as dependências necessárias usando pip.
5. Para desativar o ambiente virtual, use o comando: deactivate
   Usar ambientes virtuais é uma prática recomendada para manter projetos organizados e evitar conflitos de dependências.
'''

'''
limpar todas as bibliotecas instaladas no ambiente virtual
# $ pip freeze | grep -v "^-e" | xargs pip uninstall -y
'''

'''
# Explique o PIPX
PIPX é uma ferramenta que permite instalar e executar pacotes Python como comandos de terminal. 
Ele é útil para instalar ferramentas que você deseja usar como comandos do sistema, como `black` (formatador de código), 
`flake8` (verificador de estilo), ou `httpie` (cliente HTTP). Com PIPX, você pode instalar essas ferramentas em um ambiente 
isolado, sem afetar o ambiente virtual do projeto. 
Para usar o PIPX:
1. Instale o PIPX usando o comando: `pip install pipx`
2. Instale um pacote com PIPX: `pipx install nome_do_pacote`
3. Execute o comando diretamente no terminal: `nome_do_pacote argumentos`
4. Para listar os pacotes instalados com PIPX: `pipx list`
5. Para desinstalar um pacote: `pipx uninstall nome_do_pacote`
Isso permite que você use ferramentas Python globalmente, sem a necessidade de instalá-las em cada ambiente virtual.    
'''

'''
# Explique o poetry
Poetry é uma ferramenta de gerenciamento de dependências e empacotamento para Python. 
Ele permite gerenciar as dependências do projeto de forma mais eficiente, criando um arquivo `pyproject.toml` 
que descreve o projeto e suas dependências. Com o Poetry, você pode:
1. Criar novos projetos com `poetry new nome_do_projeto`
2. Adicionar dependências com `poetry add nome_do_pacote`
3. Instalar dependências com `poetry install`
4. Publicar pacotes com `poetry publish`
5. Gerenciar versões e ambientes virtuais automaticamente.
Poetry facilita a criação de ambientes isolados e garante que todas as dependências estejam corretamente configuradas,
 tornando o desenvolvimento mais seguro e organizado.

 poetry config virtualenvs.in-project true  (só uma vez)
 poetry new meu_projeto                     (cria a estrutura do projeto)
 cd meu_projeto                             (entra na pasta do projeto)
    poetry add requests                     (to install a package)
    poetry install                          (to install all dependencies)
    poetry shell                            (to activate the virtual environment)
    poetry show                             (to list installed packages)
    poetry add flask                        (to add another package)
    poetry remove flask                     (to remove a package)
    poetry update                           (to update dependencies)
    poetry lock                             (to update the lock file)
    poetry publish                          (to publish the package)
'''