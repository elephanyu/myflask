from datetime import timedelta
from flask import Flask, request, session, g
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guss key'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

@app.route('/set/<string:pname>')
def set(pname):
    g.setdefault(pname, default=pname)
    g.setdefault(pname+'1', default=pname+'1')
    msg = 'set session key {0} to [{1}]'.format(pname, pname)
    session[pname] = pname
    for v in g:
        print v
    return msg

@app.route('/get/<string:pname>')
def get(pname):
    if session is not None and session.has_key('username'):
        ret = session.get(pname)
        return 'get session key {0}[{1}]'.format(pname, ret)
    else:
        return 'session is null or session key {0} is not exist'.format(pname)

@app.route('/delete/<string:pname>')
def delete(pname):
    if session is not None and session.has_key('username'):
        session.pop(pname)
        return 'delete session success'
    else:
        return 'session is null or session key {0} is not exist'.format(pname)

@app.route('/clear')
def clear():
    if session is not None:
        session.clear()
        return 'clear session'
    else:
        return 'session already is null'

if __name__ == '__main__':
    app.run(debug=True)