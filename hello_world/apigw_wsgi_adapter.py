import serverless_wsgi

from hello_world.app import app


def lambda_handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
