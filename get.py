# importamos lo necesario
from flask import Flask, render_template, request
import pickle
import numpy as np

# Instancia de Flask. Aplicación
app = Flask(__name__,template_folder='template')

# Creamos nuestro primer route. '/login'
@app.route('/login')
def template():
	# Renderizamos la plantilla. Formulario HTML.
	# templates/form.html
	return render_template("pagina.html")

@app.route('/usuario',methods=['GET'])
def validacion():
	with open('modelo.bin','rb') as f:
    		logreg = pickle.load(f)
	
	l_sepalo = float(request.args.get('larg_sepalo'))
	a_sepalo = float(request.args.get('anch_sepalo'))
	l_petalo = float(request.args.get('larg_petalo'))

	
	Z = logreg.predict(np.c_[l_sepalo,a_sepalo,l_petalo])

	if Z == 0:
		mata ='I.setosa'
	elif Z == 1:
		mata ='I. versicolor'
	elif Z == 2:
		mata ='I. virginica'
	else:
		mata ='revisate loco'
	
	return mata

if __name__ == '__main__':
	# Iniciamos la apicación en modo debug
	app.run(host='127.0.0.1',
			debug=True,
            port=5000)