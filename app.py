from typing import Optional

from flask import Flask, request, jsonify
from pydantic import BaseModel

from flask_pydantic_easy.core import decorate

app = Flask("app")


class QueryModel(BaseModel):
    age: int


@app.route('/user/<string:some_str>', methods=['GET'])
@decorate
def get_user(query_model: QueryModel, some_str):
    print(some_str)
    print(query_model.age)
    print('ok')
    return 'ok'


@app.route('/user/<string:some_str>', methods=['POST'])
@decorate
def create_user(body_model: QueryModel, some_str):
    print(some_str)
    print(body_model.age)
    print('ok')
    return 'ok'


if __name__ == '__main__':
    app.run(port=5000)
