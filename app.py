from flask import *
from chatbot import respuesta

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    pregunta = None
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        pregunta = request.form['pregunta']
        return render_template('index.html', answer=respuesta(pregunta))

if __name__ == '__main__':
    app.run(debug=True)