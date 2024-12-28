## Projeto KANBAN

Criando e acessar o ambiente virtual
### LINUX
````bash
    python3 -m venv .venv
````
````bash
    source .venv/bin/activate 
````

### WINDOWS
````bash
    python -m venv venv
````
````bash
    .venv/Scripts/activate 
````

Instalar gerenciador de pacotes
````bash
    pip install uv
````

Baixar as libs
````bash
  uv sync
````

Rodar as migrations
````bash
  uv migrate
````

Criar superuser
````bash
  task createsuperuser
````

Rodar o servidor
````bash
  task runserver
````

