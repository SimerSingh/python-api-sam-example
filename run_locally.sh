set -e
export PYTHONPATH=.

export FLASK_ENV=development
export FLASK_DEBUG=true
export FLASK_APP=hello_world.app:app
flask run
