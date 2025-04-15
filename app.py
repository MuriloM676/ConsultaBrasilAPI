from flask import Flask, jsonify, request, render_template
import requests
import logging

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Base URL da BrasilAPI
BRASIL_API_URL = "https://brasilapi.com.br/api"

# Rota principal para renderizar a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint para listar Bancos
@app.route('/api/banks', methods=['GET'])
def get_banks():
    try:
        logger.info("Consultando a rota /banks/v1 na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/banks/v1")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data[:5]}), 200  # Limita a 5 bancos
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /banks/v1: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar Câmbio
@app.route('/api/cambio', methods=['GET'])
def get_cambio():
    try:
        logger.info("Consultando a rota /cambio na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/cambio?currency=USD")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /cambio: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar CEP (com validação)
@app.route('/api/cep/<string:cep>', methods=['GET'])
def get_cep(cep):
    try:
        # Validação básica de CEP (8 dígitos numéricos)
        if not cep.isdigit() or len(cep) != 8:
            logger.warning(f"CEP inválido recebido: {cep}")
            return jsonify({"status": "error", "message": "CEP deve ter 8 dígitos numéricos"}), 400
        
        logger.info(f"Consultando a rota /cep/v2/{cep} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/cep/v2/{cep}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /cep/v2/{cep}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar CNPJ (com validação)
@app.route('/api/cnpj/<string:cnpj>', methods=['GET'])
def get_cnpj(cnpj):
    try:
        # Validação básica de CNPJ (14 dígitos numéricos)
        if not cnpj.isdigit() or len(cnpj) != 14:
            logger.warning(f"CNPJ inválido recebido: {cnpj}")
            return jsonify({"status": "error", "message": "CNPJ deve ter 14 dígitos numéricos"}), 400
        
        logger.info(f"Consultando a rota /cnpj/v1/{cnpj} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/cnpj/v1/{cnpj}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /cnpj/v1/{cnpj}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para listar Corretoras
@app.route('/api/corretoras', methods=['GET'])
def get_corretoras():
    try:
        logger.info("Consultando a rota /corretoras/v1 na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/corretoras/v1")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data[:5]}), 200  # Limita a 5 corretoras
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /corretoras/v1: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar CPTEC (ex.: clima em uma cidade)
@app.route('/api/cptec/<string:city_code>', methods=['GET'])
def get_cptec(city_code):
    try:
        logger.info(f"Consultando a rota /cptec/v1/clima/previsao/{city_code} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/cptec/v1/clima/previsao/{city_code}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /cptec/v1/clima/previsao/{city_code}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar DDD (com validação)
@app.route('/api/ddd/<string:ddd>', methods=['GET'])
def get_ddd(ddd):
    try:
        # Validação básica de DDD (2 dígitos numéricos)
        if not ddd.isdigit() or len(ddd) != 2:
            logger.warning(f"DDD inválido recebido: {ddd}")
            return jsonify({"status": "error", "message": "DDD deve ter 2 dígitos numéricos"}), 400
        
        logger.info(f"Consultando a rota /ddd/v1/{ddd} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/ddd/v1/{ddd}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /ddd/v1/{ddd}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar Feriados Nacionais (com validação)
@app.route('/api/feriados/<int:ano>', methods=['GET'])
def get_feriados(ano):
    try:
        # Validação básica de ano (entre 1900 e 2100)
        if ano < 1900 or ano > 2100:
            logger.warning(f"Ano inválido recebido: {ano}")
            return jsonify({"status": "error", "message": "Ano deve estar entre 1900 e 2100"}), 400
        
        logger.info(f"Consultando a rota /feriados/v1/{ano} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/feriados/v1/{ano}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /feriados/v1/{ano}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar FIPE (com validação)
@app.route('/api/fipe/<string:codigo_fipe>', methods=['GET'])
def get_fipe(codigo_fipe):
    try:
        # Validação básica de código FIPE (formato XXXYYY-Z)
        if not codigo_fipe or len(codigo_fipe) != 8 or codigo_fipe[6] != '-':
            logger.warning(f"Código FIPE inválido recebido: {codigo_fipe}")
            return jsonify({"status": "error", "message": "Código FIPE deve ter o formato XXXXXX-Y (ex.: 038003-1)"}), 400
        
        logger.info(f"Consultando a rota /fipe/preco/v1/{codigo_fipe} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/fipe/preco/v1/{codigo_fipe}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /fipe/preco/v1/{codigo_fipe}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar IBGE (ex.: nomes)
@app.route('/api/ibge/nomes/<string:nome>', methods=['GET'])
def get_ibge_nomes(nome):
    try:
        logger.info(f"Consultando a rota /ibge/nomes/v2/{nome} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/ibge/nomes/v2/{nome}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /ibge/nomes/v2/{nome}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar ISBN (com validação)
@app.route('/api/isbn/<string:isbn>', methods=['GET'])
def get_isbn(isbn):
    try:
        # Validação básica de ISBN (10 ou 13 dígitos)
        if not isbn.isdigit() or (len(isbn) != 10 and len(isbn) != 13):
            logger.warning(f"ISBN inválido recebido: {isbn}")
            return jsonify({"status": "error", "message": "ISBN deve ter 10 ou 13 dígitos numéricos"}), 400
        
        logger.info(f"Consultando a rota /isbn/v1/{isbn} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/isbn/v1/{isbn}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /isbn/v1/{isbn}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar NCM (com validação)
@app.route('/api/ncm/<string:code>', methods=['GET'])
def get_ncm(code):
    try:
        # Validação básica de NCM (formato XXXX.XX.XX)
        if not code or len(code) != 10 or code[4] != '.' or code[7] != '.':
            logger.warning(f"Código NCM inválido recebido: {code}")
            return jsonify({"status": "error", "message": "Código NCM deve ter o formato XXXX.XX.XX (ex.: 0101.21.00)"}), 400
        
        logger.info(f"Consultando a rota /ncm/v1/{code} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/ncm/v1/{code}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /ncm/v1/{code}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para listar PIX
@app.route('/api/pix', methods=['GET'])
def get_pix():
    try:
        logger.info("Consultando a rota /pix/v1/participants na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/pix/v1/participants")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data[:5]}), 200  # Limita a 5 participantes
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /pix/v1/participants: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar Registro BR (com validação)
@app.route('/api/registrobr/<string:domain>', methods=['GET'])
def get_registrobr(domain):
    try:
        # Validação básica de domínio
        if not domain or '.' not in domain:
            logger.warning(f"Domínio inválido recebido: {domain}")
            return jsonify({"status": "error", "message": "Domínio deve conter pelo menos um ponto (ex.: exemplo.com.br)"}), 400
        
        logger.info(f"Consultando a rota /registrobr/v1/{domain} na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/registrobr/v1/{domain}")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /registrobr/v1/{domain}: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

# Endpoint para consultar Taxas
@app.route('/api/taxas', methods=['GET'])
def get_taxas():
    try:
        logger.info("Consultando a rota /taxas/v1 na BrasilAPI")
        response = requests.get(f"{BRASIL_API_URL}/taxas/v1")
        response.raise_for_status()
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.exceptions.RequestException as err:
        logger.error(f"Erro ao consultar /taxas/v1: {str(err)}")
        return jsonify({"status": "error", "message": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)