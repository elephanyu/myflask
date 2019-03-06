- flask默认基础配置
    ```python
    from datetime import timedelta
    from werkzeug.datastructures import ImmutableDict
    default_config = ImmutableDict({
        'ENV':                                  None,
        'DEBUG':                                None,
        'TESTING':                              False,
        'PROPAGATE_EXCEPTIONS':                 None,
        'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
        'SECRET_KEY':                           None,
        'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
        'USE_X_SENDFILE':                       False,
        'SERVER_NAME':                          None,
        'APPLICATION_ROOT':                     '/',
        'SESSION_COOKIE_NAME':                  'session',
        'SESSION_COOKIE_DOMAIN':                None,
        'SESSION_COOKIE_PATH':                  None,
        'SESSION_COOKIE_HTTPONLY':              True,
        'SESSION_COOKIE_SECURE':                False,
        'SESSION_COOKIE_SAMESITE':              None,
        'SESSION_REFRESH_EACH_REQUEST':         True,
        'MAX_CONTENT_LENGTH':                   None,
        'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
        'TRAP_BAD_REQUEST_ERRORS':              None,
        'TRAP_HTTP_EXCEPTIONS':                 False,
        'EXPLAIN_TEMPLATE_LOADING':             False,
        'PREFERRED_URL_SCHEME':                 'http',
        'JSON_AS_ASCII':                        True,
        'JSON_SORT_KEYS':                       True,
        'JSONIFY_PRETTYPRINT_REGULAR':          False,
        'JSONIFY_MIMETYPE':                     'application/json',
        'TEMPLATES_AUTO_RELOAD':                None,
        'MAX_COOKIE_SIZE': 4093,
    })
    ```

- falsk有四种配置加载方式
    - 使用对象加载
        ```python
        from flask import Flask
        from config import setObj
        
        app = Flask(__name__)
        app.config.from_object(setObj)
        ```
    - 使用py文件加载
        ```python
        from flask import Flask
        
        app = Flask(__name__)    
        app.config.from_pyfile('settings.py', silent=True)
  
        ```
    - 使用json对象加载
        ```python
        from flask import Flask
        
        app = Flask(__name__)    
        app.config.from_json('settings.json', silent=True)
        ```
    - 使用环境变量加载
        ```python
        from flask import Flask
        
        app = Flask(__name__)    
        app.config.from_envvar('FLASK_SETTING', silent=True)
        ```