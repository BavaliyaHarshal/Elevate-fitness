from flask import Flask
from app.routes.user_routes import user_routes
from app.utils.database import create_tables
from app.routes.physique_routes import physique_routes 


app = Flask(__name__)

create_tables()

app.register_blueprint(user_routes, url_prefix="/api")
app.register_blueprint(physique_routes, url_prefix='/api')


@app.route("/")
def home():
    return "Welcome to the Fitness AI Backend!"

if __name__ == "__main__":
    app.run(debug=True)
