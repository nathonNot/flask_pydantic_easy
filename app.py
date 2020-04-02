from typing import Optional

from flask import Flask, request, jsonify
from flask_pydantic_demo import validate
from pydantic import BaseModel

from flask_pydantic_easy.core import decorate

app = Flask("flask_pydantic_app")


class QueryModel(BaseModel):
    age: int

@app.route('/ceshi/<string:abc>', methods=['GET'])
@decorate
def ceshi(query_model: QueryModel, abc):
    print(abc)
    print(query_model.age)
    print('ok')
    return 'ok'

@app.route('/ceshi/<string:abc>', methods=['POST'])
@decorate
def ceshi(body_model: QueryModel, abc):
    print(abc)
    print(body_model.age)
    print('ok')
    return 'ok'

if __name__ == '__main__':
    app.run(port=5000)
