from flask import Flask, request, jsonify

app = Flask(__name__)
PORT = 8888

@app.route('/recibir-datos', methods=['POST'])
def recibir_datos():
    datos = request.json
    print('Datos recibidos:', datos)
    # Aquí puedes procesar los datos recibidos según sea necesario
    return jsonify({'mensaje': 'Datos recibidos correctamente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
