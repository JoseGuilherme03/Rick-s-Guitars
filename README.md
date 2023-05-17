
# RICK'S GUITARS

Um Sistema de Gerenciamento de Estoque de uma loja de guitarras chamada Rick's Guitars. Projeto proposto durante a matéria de POO e implementado com o framework Django


## Rodando localmente

Clone o projeto

```bash
  git clone "https://github.com/JoseGuilherme03/Ricks-Guitars.git"
```

Entre no diretório do projeto

```bash
  cd Ricks-Guitars
```

Crie um ambiente virtual 

```bash
  python -m venv venv
```

Ative o ambiente virtual

```bash
  venv/scripts/activate.ps1
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Aplique a migração dos apps para a aplicação funcionar corretamente

```bash
  python manage.py migrate
```

Inicie o servidor

```bash
  python manage.py runserver
```


## Funcionalidades

- Cadastro, edição e exclusão de itens
- Filtro por nome do item
- Filtro personalizado com as especificações dos itens


## Referência

 - Livro: https://g.co/kgs/8xDfvY
