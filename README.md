# flask_pydantic_easy
借鉴flask_pydantic，简化了一些参数的校验，但是对于一些仅需要对于入参校验的已经足够了。


安装
```
pip install flask_pydantic_easy
```
使用方法
```


from core import decorate

@app.route('/user/<string:some_str>', methods=['GET'])
@decorate
def ceshi(query_model: QueryModel, abc):
    print(abc)
    print(query_model.age)
    print('ok')
    return 'ok'
```

相对于flask_pydantic库，这个方法简化了一些多参数的方法和对于response的参数校验。

但通过对方法内的入参直接校验，可以获得不错的编辑器支持。

url的参数校验，方法入参使用query_model
body内的参数校验，方法入参使用body_model
