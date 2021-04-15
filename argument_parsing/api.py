from flask import Flask, app
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'rate': args['rate']}


api.add_resource(HelloWorld, '/todos')

if __name__ == '__main__':
    parser = reqparse.RequestParser()
    parser.add_argument(
        'rate', type=int, help='Rate to chage for this resource')
    args = parser.parse_args()

    app.run(debug=True)
