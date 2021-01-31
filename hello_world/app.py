import os
from flask import Flask
from hello_world.service import hello_world

app = Flask(__name__)

app.register_blueprint(
    hello_world.blueprint,
    url_prefix='/helloworld')
