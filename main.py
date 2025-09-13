from flask import Flask, render_template
import sys
import os

# Agregar ruta al módulo visualizacion.py
sys.path.append(os.path.join(os.path.dirname(__file__), 'templates', 'projects', 'visualizacion'))
from visualizacion import generar_grafico

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/projects/<project_name>")
def project(project_name):
    try:
        return render_template(f"projects/{project_name}/{project_name}.html")
    except:
        return render_template("404.html"), 404

@app.route("/projects/visualizacion")
def visualizacion():
    graph_html = generar_grafico()
    return render_template("projects/visualizacion/visualizacion.html", graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)