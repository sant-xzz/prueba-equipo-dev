from flask import Flask, jsonify

app = Flask(__name__)

tareas = [
    {"id": 1, "texto": "Aprender Git", "completada": False},
    {"id": 2, "texto": "Practicar GitHub", "completada": True}
]

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

@app.route('/tareas/<int:id>/completar', methods=['PUT'])
def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completada'] = True
            return jsonify(tarea)
    return jsonify({"error": "Tarea no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)