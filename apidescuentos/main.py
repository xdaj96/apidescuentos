# mi_app/app.py

from flask import Flask
from routes import initialize_routes
from flask_cors import CORS,cross_origin 
 
app = Flask(__name__)

# inicializamos las rutas de la api 
initialize_routes(app)

cors = CORS(app,origins='*') # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run(debug=True)