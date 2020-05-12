from setuptools import setup, find_packages

setup(
    name="flask_pydantic_easy",
    version="0.0.2",
    description="快速，方便的flask路由参数校验器",
    license="MIT Licence",

    url="https://github.com/674197141/flask_pydantic_easy",
    author="刘宇",
    author_email="674197141@qq.com",

    packages=["flask_pydantic_easy"],
    include_package_data=True,
    platforms="any",
    install_requires=["flask", "pydantic"]
)
