import json
from functools import wraps
from inspect import signature
from typing import Optional, Callable, TypeVar, Any, Union, Iterable, Type, List

from flask import request, jsonify, make_response, Response, abort
from pydantic import BaseModel, ValidationError

try:
    from flask_restful import original_flask_make_response as make_response
except ImportError:
    pass


def decorate():
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_data = signature(func)
        query_model = func_data.parameters.get('query_model')
        body_model = func_data.parameters.get('body_model')
        q, b, err = None, None, {}
        if query_model:
            query_params = request.args
            model = query_model.annotation
            try:
                q = model(**query_params)
                kwargs['query_model'] = q
            except ValidationError as ve:
                err["query_params"] = ve.errors()
        if body_model:
            body_params = request.get_json() if request.get_json() else request.values
            model = body_model.annotation
            try:
                b = model(**body_params)
                kwargs['body_model'] = b
            except ValidationError as ve:
                err["body_params"] = ve.errors()

        if err:
            return make_response(jsonify({"validation_error": err}), 400)
        res = func(*args, **kwargs)

        return res

    return wrapper
