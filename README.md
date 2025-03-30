# 1. Tecnologias Utilizadas
Backend
Python 3.8+

FastAPI (para API REST)

Uvicorn (para rodar o servidor)

## Frontend
Vue.js 3 (para a interface web)

Axios (para consumir a API)

Vite (ferramenta para rodar o frontend)
 3. Instalação
3.1 Instalar o Backend
1️⃣ Instale o Python 3.8+
🔗 https://www.python.org/downloads/

2️⃣ Instale as dependências:
pip install -r backend/requirements.txt

3.2 Instalar o Frontend
1️⃣ Instale o Node.js 16+
🔗 https://nodejs.org/

2️⃣ Vá até a pasta do frontend:
cd frontend
 Instale as dependências:
npm install

 ## Funcionalidades
📄 Conversão de PDF para CSV
✅ Extrai tabelas do PDF "Rol de Procedimentos e Eventos em Saúde"
✅ Salva os dados em CSV estruturado
✅ Substitui as siglas OD e AMB pelas descrições completas

🔎 API de Busca
✅ Endpoint GET /api/operadoras?search={termo}
✅ Busca por nome e outras informações no CSV
✅ Suporte a filtros personalizados

🖥️ Frontend Vue.js
✅ Tela para buscar operadoras de saúde
✅ Lista de resultados formatados
✅ Interface simples e responsiva
