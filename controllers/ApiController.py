import json
from index import app
#from service.SeleniumService import search
from service.SeleniumService import SeleniumService

@app.route('/')
def index():
    return SeleniumService().search('https://www.youtube.com/watch?v=Y04RDlvAM04', '//*[@id="container"]/h1/yt-formatted-string')