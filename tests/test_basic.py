# Test Case for Flask framework

import unittest

from flask import Flask

def create_app(cfg=None):
    app = Flask(__name__)
    return app

class FlaskClientTestCase(unittest.TestCase):

        def setUp(self):
                self.app = create_app('unittest')
                self.app_context = self.app.app_context()
                self.app_context.push()
                self.client = self.app.test_client()

                @self.app.route("/")
                def helloworld():
                        return "Hello World!"

                @self.app.route("/hello")
                def hello():
                        return "hello"

                @self.app.route("/world")
                def world():
                    return "world"



        def test_home_page(self):
                response = self.client.get('/')
                self.assertTrue('Hello World' in response.get_data(as_text=True))
                response = self.client.get('/hello')
                self.assertTrue('hello' in response.get_data(as_text=True))
                response = self.client.get('/world')
                self.assertTrue('world' in response.get_data(as_text=True))




