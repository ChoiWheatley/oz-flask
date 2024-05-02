# 03. flask-restfulapi 활용하여  REST API 생성

```python
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Item(Resource):
    def get(self, name):
        pass
    ...

api.add_resource(Item, "/item/<string:name>") 

if __name__ == "__main__":
    app.run()

```
