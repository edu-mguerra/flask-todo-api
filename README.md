# 📝 Flask To-Do API

Uma API RESTful simples para gerenciamento de tarefas (To-Do List), desenvolvida com **Flask** e **MongoDB**.

---

## 🚀 Funcionalidades

- Criar uma nova tarefa  
- Listar todas as tarefas (com filtro por status)  
- Obter os dados de uma tarefa específica  
- Atualizar uma tarefa  
- Deletar uma tarefa  

---

## 💻 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd flask-todo-api
```
### 2. Execute o projeto
```bash
python main.py
````
Acesse em:
http://localhost:5000

### 3 📦 Dependências
Flask
pymongo
python-dotenv

### 4 🧪 Testando os endpoints
Use ferramentas como Postman, Insomnia ou curl para testar os endpoints:

POST /tasks

GET /tasks

GET /tasks/<task_id>

PUT /tasks/<task_id>

DELETE /tasks/<task_id>



