# Sistema de Estoque em Python com MySQL

Este projeto implementa um sistema simples de gerenciamento de estoque utilizando **Python** e **MySQL**. O sistema permite:

- Cadastro de produtos
- Consulta de produtos cadastrados
- Atualização da quantidade disponível de produtos
- Remoção de produtos do cadastro

---

## Estrutura do Projeto

- `sistema_estoque.py`: arquivo Python contendo a implementação das classes e operações CRUD para produtos.
- `banco_estoque.sql`: script SQL para criar o banco de dados e as tabelas necessárias (fornecido separadamente).

---

## Requisitos

- Python 3.x instalado
- MySQL instalado e em execução
- Biblioteca `mysql-connector-python` instalada:

```bash
pip install mysql-connector-python
