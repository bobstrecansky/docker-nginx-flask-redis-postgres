from flask import Flask
import redis

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379)

@app.route('/')
def hello_world():
    foo = cache.set('foo', 'bar')
    foo = cache.get('foo')
    return 'hello' + str(foo)

@app.route('/test')
def test():
    return 'TEST SUCCESSFUL'

@app.route('/foo')
def x():
    return 'bar'

@app.route('/bar')
def y():
    return 'foo2'
