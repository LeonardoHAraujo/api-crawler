import json
from index import app
from service.seleniumService import SeleniumService

@app.route('/<string:dish>')
def index(dish):
    return SeleniumService().search(dish)