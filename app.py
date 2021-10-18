from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mediana', methods=['POST'])
def median():
    entrada = request.form['lista']
    if request.method == 'POST':
        if entrada == '':
            flash('No se han ingresado valores, por favor, ingresa una lista de números')
        else:
            numeros=entrada
            if numeros.find(',') != -1:
                lista = [float(i) for i in numeros.split(',')]
                num_of_terms = len(lista)
                sum_of_terms = 0
                for term in lista:
                    sum_of_terms  += term
                    
                median = sum_of_terms / num_of_terms   

            else:
                lista = [float(i) for i in numeros.split(' ')]
                num_of_terms = len(lista)
                sum_of_terms = 0
                for term in lista:
                    sum_of_terms  += term
                median = sum_of_terms / num_of_terms  
                 
    return render_template('index.html',mediana=median)

    

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
