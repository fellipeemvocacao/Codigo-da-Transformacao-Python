# Pensamento Computacional - Projeto Final ⛪

Este projeto é uma aplicação web interativa desenvolvida em Python com Flask, projetada para fornecer conteúdos educativos de forma dinâmica. A interface permite navegar por tópicos estruturados (como O Credo, Os Sacramentos, entre outros) e subtopicos correspondentes, buscando as informações em tempo real em um banco de dados relacional leve.

## 🚀 Tecnologias Utilizadas

* **Backend:** Python 3.14+ & Flask
* **Banco de Dados:** SQLite
* **ORM:** Flask-SQLAlchemy (para mapeamento e consultas ao banco)
* **Frontend:** HTML5, CSS3 e JavaScript (para requisições dinâmicas via API)

## 📁 Estrutura do Projeto

```text
pensamento_computacional_projeto_final/
├── instance/
│   └── igreja_catolica.db      # Banco de dados SQLite (gerado automaticamente)
├── templates/
│   └── index.html               # Interface principal do usuário
├── app.py                       # Arquivo principal do servidor Flask e modelos
├── inicializar_bd.py            # Script para criação automática das tabelas
└── README.md                    # Documentação do projeto