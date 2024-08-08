from flask  import Flask
from flask_restful import Api
from app.routes.example_route import example_route







app = Flask(__name__)
api = Api(app)





app.register_blueprint(example_route,url_prefix ='/api')

if __name__ =="__main__":
    app.run(debug = True)