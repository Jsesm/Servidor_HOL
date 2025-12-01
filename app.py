# app.py
from flask import Flask, request, jsonify
import requests
from game_logic import traducir_palo, traducir_valor, elegir_carta

from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

estado_juego = {}

@app.route('/')
def index():
    return "Servidor de juego activo"

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    player_id = data.get('player_id')
    move = data.get('move')


@app.route('/start', methods=['GET'])
def inicio_partida():
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=2"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        carta1 = data['cards'][0]
        carta2 = data['cards'][1]
        return jsonify({
            'valor2': traducir_valor(carta2['value']),
            'valor1': traducir_valor(carta1['value']),
            'palo': traducir_palo(carta2['value'], carta1['value']),
            'imagen_inicio': carta1['image'],
            'imagen_final':carta2['image']
        })
    else:
        return jsonify({'error': f"No se pudo obtener la carta: {response.status_code}"}), 500



@app.route('/sobre', methods=['GET'])
def sobre():
    
    numero, palo= elegir_carta()
    return jsonify({
        'numero': numero,
        'palo':palo
    })
    

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)