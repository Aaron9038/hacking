from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Inicio():
    return render_template('home.html')

@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

if __name__ == '__main__':
    app.run(debug=True)