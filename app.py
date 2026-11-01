from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Microservicio de Pagos - Estatus: Activo (Puerto 5000)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
