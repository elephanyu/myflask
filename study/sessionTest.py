from datetime import timedelta
from flask import Flask, current_app, g, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guss key'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

@app.route('/set/<string:pname>')
def set(pname):
    g.setdefault(pname, default=pname)
    g.setdefault(pname+'1', default=pname+'1')
    msg = 'set session key {0} to [{1}]'.format(pname, pname)
    session[pname] = pname
    '''
    {
      'subdomain_matching': False, 
      'error_handler_spec': {}, 
      '_before_request_lock': <thread.lock object at 0x00000000068D6650>, 
      'jinja_env': <flask.templating.Environment object at 0x0000000007565630>, 
      'before_request_funcs': {}, 
      'teardown_appcontext_funcs': [], 
      'shell_context_processors': [], 
      'after_request_funcs': {}, 
      'cli': <flask.cli.AppGroup object at 0x00000000075656A0>, 
      '_blueprint_order': [], 
      'before_first_request_funcs': [], 
      'view_functions': {
          'delete': <function delete at 0x0000000007558588>, 
          'clear': <function clear at 0x0000000007558EB8>, 
          'set': <function set at 0x0000000007540E48>, 
          'static': <bound method Flask.send_static_file of <Flask 'sessionTest'>>, 
          'get': <function get at 0x00000000075589E8>
      }, 
      'instance_path': 'D:\\code\\myflask27\\study\\instance', 
      'teardown_request_funcs': {}, 
      'url_value_preprocessors': {}, 
      'config': <Config {
          'JSON_AS_ASCII': True, 
          'USE_X_SENDFILE': False, 
          'SESSION_COOKIE_SECURE': False, 
              'SESSION_COOKIE_PATH': None, 
          'SESSION_COOKIE_DOMAIN': None, 
          'SESSION_COOKIE_NAME': 'session', 
          'MAX_COOKIE_SIZE': 4093, 
          'SESSION_COOKIE_SAMESITE': None, 
          'PROPAGATE_EXCEPTIONS': None, 
          'ENV': 'development', 
          'DEBUG': False, 
          'SECRET_KEY': 'hard to guss key', 
          'EXPLAIN_TEMPLATE_LOADING': False, 
          'MAX_CONTENT_LENGTH': None, 
          'APPLICATION_ROOT': '/', 
          'SERVER_NAME': None, 
          'PREFERRED_URL_SCHEME': 'http', 
          'JSONIFY_PRETTYPRINT_REGULAR': False, 
          'TESTING': False, 
          'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 
          'TEMPLATES_AUTO_RELOAD': None, 
          'TRAP_BAD_REQUEST_ERRORS': None, 
          'JSON_SORT_KEYS': True, 
          'JSONIFY_MIMETYPE': 'application/json', 
          'SESSION_COOKIE_HTTPONLY': True, 
          'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 
          'PRESERVE_CONTEXT_ON_EXCEPTION': None, 
          'SESSION_REFRESH_EACH_REQUEST': True, 
          'TRAP_HTTP_EXCEPTIONS': False
      }>, 
      '_static_url_path': None, 
      'template_context_processors': {
          None: [
              <function _default_template_ctx_processor at 0x00000000067FD908>
          ]
      },
      'template_folder': 'templates', 
      'blueprints': {}, 
      'url_map': Map([
          <Rule '/clear' (HEAD, OPTIONS, GET) -> clear>,
          <Rule '/delete/<pname>' (HEAD, OPTIONS, GET) -> delete>,
          <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
          <Rule '/set/<pname>' (HEAD, OPTIONS, GET) -> set>,
          <Rule '/get/<pname>' (HEAD, OPTIONS, GET) -> get>]
      ), 
      'name': 'sessionTest', 
      '_got_first_request': True, 
      'import_name': 'sessionTest', 
      'root_path': 'D:\\code\\myflask27\\study', 
      '_static_folder': 'static', 
      'extensions': {}, 
      'url_default_functions': {}, 
      'url_build_error_handlers': []
    }
    '''
    print current_app.__dict__
    '''
    {
        'view_args': {'pname': u'elephan'}, 
        'url_rule': <Rule '/set/<pname>' (HEAD, OPTIONS, GET) -> set>, 
        'cookies': {
            'session': u'eyJlbGVwaGFuIjoiZWxlcGhhbiJ9.XIBvgg.DOtZWHav0RcVne63b4hhnbDZ6Pw', 
            'show_followed': u''
        }, 
        'shallow': False, 
        'environ': {
            'wsgi.multiprocess': False, 
            'HTTP_COOKIE': 'show_followed=; session=eyJlbGVwaGFuIjoiZWxlcGhhbiJ9.XIBvgg.DOtZWHav0RcVne63b4hhnbDZ6Pw', 
            'SERVER_SOFTWARE': 'Werkzeug/0.14.1', 
            'SCRIPT_NAME': '', 
            'REQUEST_METHOD': 'GET', 
            'PATH_INFO': '/set/elephan', 
            'SERVER_PROTOCOL': 'HTTP/1.1', 
            'QUERY_STRING': '', 
            'werkzeug.server.shutdown': <function shutdown_server at 0x00000000075ECCF8>, 
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.20 Safari/537.36', 
            'HTTP_CONNECTION': 'keep-alive', 
            'SERVER_NAME': '127.0.0.1', 
            'REMOTE_PORT': 50432, 
            'wsgi.url_scheme': 'http', 
            'SERVER_PORT': '5000', 
            'werkzeug.request': <Request 'http://127.0.0.1:5000/set/elephan' [GET]>, 
            'wsgi.input': <socket._fileobject object at 0x00000000075C85E8>, 
            'HTTP_HOST': '127.0.0.1:5000', 
            'wsgi.multithread': True, 
            'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
            'HTTP_CACHE_CONTROL': 'max-age=0', 
            'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
            'wsgi.version': (1, 0), 
            'wsgi.run_once': False, 
            'wsgi.errors': <open file '<stderr>', mode 'w' at 0x000000000557B150>, 
            'REMOTE_ADDR': '127.0.0.1', 
            'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 
            'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br'
        }, 
        'url': u'http://127.0.0.1:5000/set/elephan', 
        'shallow': False, 
        'url_rule': <Rule '/set/<pname>' (HEAD, OPTIONS, GET) -> set>, 
        'environ': {
            'wsgi.multiprocess': False, 
            'HTTP_COOKIE': 'show_followed=; session=eyJlbGVwaGFuIjoiZWxlcGhhbiJ9.XIBvgg.DOtZWHav0RcVne63b4hhnbDZ6Pw', 
            'SERVER_SOFTWARE': 'Werkzeug/0.14.1', 
            'SCRIPT_NAME': '', 
            'REQUEST_METHOD': 'GET', 
            'PATH_INFO': '/set/elephan', 
            'SERVER_PROTOCOL': 'HTTP/1.1', 
            'QUERY_STRING': '', 
            'werkzeug.server.shutdown': <function shutdown_server at 0x00000000075ECCF8>, 
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.20 Safari/537.36', 
            'HTTP_CONNECTION': 'keep-alive', 
            'SERVER_NAME': '127.0.0.1', 
            'REMOTE_PORT': 50432, 
            'wsgi.url_scheme': 'http', 
            'SERVER_PORT': '5000', 
            'werkzeug.request': <Request 'http://127.0.0.1:5000/set/elephan' [GET]>, 
            'wsgi.input': <socket._fileobject object at 0x00000000075C85E8>, 
            'HTTP_HOST': '127.0.0.1:5000', 
            'wsgi.multithread': True, 
            'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
            'HTTP_CACHE_CONTROL': 'max-age=0', 
            'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
            'wsgi.version': (1, 0), 
            'wsgi.run_once': False, 
            'wsgi.errors': <open file '<stderr>', mode 'w' at 0x000000000557B150>, 
            'REMOTE_ADDR': '127.0.0.1', 
            'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 
            'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br'
        }
    }
    '''
    print request.__dict__
    '''
    {
        u'elephan1': u'elephan1', 
        u'elephan': u'elephan'
    }
    '''
    print g.__dict__
    '''
    {
        'on_update': <function on_update at 0x000000000765C0B8>, 
        'accessed': True, 
        'modified': True
    }
    '''
    print session.__dict__
    return msg

@app.route('/get/<string:pname>')
def get(pname):
    print current_app.__dict__
    if session is not None and session.has_key(pname):
        # session.setdefault('xxx', 'xxx')
        # session.get(pname) is None
        ret = session.get(pname)
        return 'get session key {0}[{1}]'.format(pname, ret)
    else:
        return 'session is null or session key {0} is not exist'.format(pname)

@app.route('/delete/<string:pname>')
def delete(pname):
    if session is not None and session.has_key(pname):
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