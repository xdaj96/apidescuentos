# mi_app/app.py

from flask import Flask
from routes import initialize_routes
from flask_cors import CORS,cross_origin 
 
app = Flask(__name__)


app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, origins=["http://localhost:4200"])  # Permite solicitudes solo desde este origen

# inicializamos las rutas de la api 
initialize_routes(app)



if __name__ == '__main__':
    app.run(debug=True)