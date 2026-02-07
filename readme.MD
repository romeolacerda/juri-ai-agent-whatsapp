# 🏛️ Sistema Jurídico com IA

Sistema de gestão jurídica integrado com inteligência artificial para análise de documentos, consulta de processos e assistência virtual.

## 🛠️ Tecnologias

- **Backend:** Django 6.0
- **IA/ML:** Agno, LanceDB, OpenAI/Anthropic
- **OCR:** Docling
- **Async Tasks:** Django Q2
- **Frontend:** TailwindCSS, Alpine.js

## 📋 Pré-requisitos

- Python 3.10+
- pip
- Git

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/romeolacerda/juri-ai-agent-whatsapp.git
cd juri-ai-agent-whatsapp
```

### 2. Configure as variáveis de ambiente
```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione suas chaves de API:
```env
OPENAI_API_KEY=sua-chave-openai
```

### 3. Crie e ative o ambiente virtual

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Execute as migrações
```bash
python manage.py migrate
```

### 6. Crie um superusuário (admin)
```bash
python manage.py createsuperuser
```

### 7. Inicie os serviços

**Terminal 1 - Servidor Django:**
```bash
python manage.py runserver
```

**Terminal 2 - Django Q Cluster (processamento assíncrono):**
```bash
python manage.py qcluster
```

### 8. Acesse o sistema

- **Interface Web:** http://localhost:8000
- **Admin Django:** http://localhost:8000/admin

## 📁 Estrutura do Projeto
```
├── usuarios/          # App de autenticação e gestão de clientes
│   ├── models.py     # Cliente, Documentos
│   ├── views.py      # Views de cadastro, login, clientes
│   └── signals.py    # Processamento assíncrono de documentos
├── ia/               # App de inteligência artificial
│   ├── agent.py      # Agente JuriAI com RAG
│   ├── tasks.py      # Tasks de OCR e embeddings
├── templates/        # Templates HTML
├── static/          # Arquivos estáticos (CSS, JS)
├── media/           # Uploads de usuários
├── lancedb/         # Banco vetorial (não versionado)
└── manage.py
```

### Usando OpenAI (GPT-4)
```env
OPENAI_API_KEY=sk-...
```
## 📚 Como Usar

### 1. Cadastrar Cliente

- Acesse "Clientes" → "Novo Cliente"
- Preencha nome, email, tipo (PF/PJ) e status

### 2. Upload de Documentos

- Entre no perfil do cliente
- Faça upload do documento (PDF, DOCX, etc.)
- O sistema automaticamente:
  - Extrai o texto via OCR
  - Indexa no banco vetorial
  - Disponibiliza para consulta via IA

### 3. Consultar Processos (DataJud)

Via chat com a IA, pergunte:
```
"Busque o processo 00008323520184013202 no TJSP"
```

### 4. Chat com Documentos

A IA tem acesso aos documentos do cliente:
```
"Resuma o contrato social da empresa X"
"Quais são as cláusulas de rescisão no documento Y?"
```

## 🧪 Desenvolvimento

### Executar testes
```bash
python manage.py test
```

### Criar novas migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### Acessar shell do Django
```bash
python manage.py shell
```

## 🐛 Troubleshooting

### Erro: `OPENAI_API_KEY not set`
- Verifique se o arquivo `.env` existe e tem a chave configurada
- Reinicie o servidor após editar o `.env`

### Django Q não processa tarefas
- Certifique-se de que o `qcluster` está rodando
- Verifique logs com `python manage.py qcluster --verbose`

### Erro de banco de dados
```bash
python manage.py migrate --run-syncdb
```