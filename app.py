import os
from flask import Flask, jsonify
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

app = Flask(__name__)

# Função para ligar à base de dados PostgreSQL do Supabase
def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({
            "status": "sucesso",
            "mensagem": "Backend do Vôlei a funcionar na nuvem!",
            "versao_bd": db_version[0]
        })
    except Exception as e:
        return jsonify({
            "status": "erro",
            "detalhe": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
