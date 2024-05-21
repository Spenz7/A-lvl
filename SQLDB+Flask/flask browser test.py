import flask
from flask import url_for
from flask import redirect
app = flask.Flask(__name__)


#@app.route('/<input>')
#def home(input):
#   return 'Hello, {}'.format(input)

@app.route('/')
def home():
    #rmb from flask import url for
    url1 = url_for('fixedroute')
    print(url1)
    url2 = url_for('string', s = 'alex')
    print(url2)
    url3 = url_for('number', i = 123)
    print(url3)
    return 'routed to fixed'


@app.route('/string/<s>')
def string(s):
    return 'Routed to string() , where s = {}'.format(s)

@app.route('/number/<int:i>')
def number(i):
    return 'Routed to number(), where i = {}'.format(i)

@app.route('/fixed/')
def fixedroute():
    return 'Routed to fixed()'

@app.route('/error')
def errorpath():
    # need '' to show no content
    # tuple(content, status code, header field)
    return ('',500)

@app.route('/rawhtml')
def rawhtml():
    headers = {'Content-Type':'text/plain'}
    return ('<b>This is raw html code</b>',200,headers)
    #if return '<b>This is raw html code</b>' server treats it as html code
    #and boldens it

@app.route('/redirect')
#NEVER call function redirect() it overrides the imported function
def relocate():
    #rmb from flask import redirect
    return redirect('http://example.com')
   
if __name__ == '__main__':
    app.run()
