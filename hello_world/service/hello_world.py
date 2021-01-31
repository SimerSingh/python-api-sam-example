
import os
import re
from typing import Dict, List, Set
from flask import Blueprint, Response, abort, jsonify, make_response, request

blueprint = Blueprint(__name__, __name__)


@blueprint.route('/hello', methods=['GET'])
def hello_world():
    print('hello_world')
    return jsonify({'hello': 'world'})
