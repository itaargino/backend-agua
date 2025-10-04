# backend-agua

API FastAPI para receber telemetria de qualidade da água.

## Como rodar localmente
1. Criar venv:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Rodar
   ```bash
   uvicorn main:app --reload
   http://127.0.0.1:8000/docs
