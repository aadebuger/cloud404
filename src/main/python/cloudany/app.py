'''
Created on Sep 7, 2015

@author: aadebuger
'''

from flask import Flask
app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Hello World!',404

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)