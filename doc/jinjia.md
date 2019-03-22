- jinjia
    - web业务逻辑和表现逻辑
        - 业务逻辑 路由函数处理请求
        - 表现逻辑 jinjia模板
    - Flask提供的render_template函数把Jinja2模板引擎集成到了程序中
        - return render_template('user.html', name=name)
        - 模板位置，变量
    - 语法
        - 变量
            - 使用{{ xx }}占位符，支持python变量使用语法
                ```html::jinjia
                <h1>Hello, {{ name|capitalize }}!</h1>
                <p>A value from a dictionary: {{ mydict['key'] }}.</p>
                <p>A value from a list: {{ mylist[3] }}.</p>
                <p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
                <p>A value from an object's method: {{ myobj.somemethod() }}.</p>
                ```
            - 变量处理器
                - safe 渲染值时不转义
                - capitalize 把值的首字母转换成大写，其他字母转换成小写
                - lower 把值转换成小写形式
                - upper 把值转换成大写形式
                - title 把值中每个单词的首字母都转换成大写
                - trim 把值的首尾空格去掉
                - striptags 渲染之前把值中所有的 HTML 标签都删掉
            - 控制结构
                - 条件语句
                    ```html::jinjia
                    {% if user %}
                        Hello, {{ user }}!
                    {% else %}
                        Hello, Stranger!
                    {% endif %}
                    ```
                - 循环语句
                    ```html::jinjia
                    <ul>
                        {% for comment in comments %}
                            <li>{{ comment }}</li>
                        {% endfor %}
                    </ul>
                    ```
                - 宏
                    ```html::jinjia
                    <!-- macros.html -->
                    <!-- 宏定义在单个文件中以便重复使用 -->
                    {% macro render_comment(comment) %}
                        <li>{{ comment }}</li>
                    {% endmacro %}
                    ```
                    ```html::jinjia
                    <!-- 宏导入 -->
                    {% import 'macros.html' as macros %}
                    <ul>
                        {% for comment in comments %}
                            <!-- 宏引用 -->
                            {{ macros.render_comment(comment) }}
                        {% endfor %}
                    </ul>
                    ```
                - 模板
                    - 通用代码包含
                        ```html::jinjia
                        {% include 'common.html' %}
                        ```
                    - 模板继承
                        ```html::jinjia
                        <!--base.html -->
                        <html>
                        <head>
                            {% block head %}
                            <title>{% block title %}{% endblock %} - My Application</title>
                            {% endblock %}
                        </head>
                        <body>
                            {% block body %}
                            {% endblock %}
                        </body>
                        </html>
                        ```
                        ```html::jinjia
                        <!-- 模板继承 -->
                        {% extends "base.html" %}
                        <!-- 模板内容实例化 -->
                        {% block title %}Index{% endblock %}
                        {% block head %}
                            {{ super() }}
                            <style>
                            </style>
                        {% endblock %}
                        {% block body %}
                        <h1>Hello, World!</h1>
                        {% endblock %}
                        ```
    - Flask-Bootstrap 
        - 集成Twitter Bootstrap 
            - 引入了Bootstrap 中的所有CSS和JavaScript文件
            - 业务逻辑引入
                ```python
                from flask import Flask
                from flask_bootstrap import Bootstrap
                
                bootstrap = Bootstrap()
                app = Flask(__name__)
                bootstrap.init_app(app)
                ```
            - 表现逻辑引入
                ```html::jinjia
                {% extends "bootstrap/base.html" %}
                {% block title %}Flasky{% endblock %}
                {% block navbar %}
                <div class="navbar navbar-inverse" role="navigation">
                    <div class="container">
                        <div class="navbar-header">
                            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        </div>
                    </div>
                </div>
                {% endblock %}
                {% block content %}
                <div class="container">
                    <div class="page-header">
                        <h1>Hello, {{ name }}!</h1>
                    </div>
                </div>
                {% endblock %}
                ```
        - bootstrap/base.html中定义的块
            - doc 整个 HTML 文档
            - html_attribs \<html\> 标签的属性
            - html \<html\> 标签中的内容
            - head \<head\> 标签中的内容
            - title \<title\> 标签中的内容
            - metas 一组 \<meta\> 标签
            - styles 层叠样式表定义
            - body_attribs \<body\> 标签的属性
            - body \<body\> 标签中的内容
            - navbar 用户定义的导航条
            - content 用户定义的页面内容
            - scripts 文档底部的JavaScript声明
            ######向已经有内容（styles和scripts）的块中添加新内容，使用Jinja2提供的super()函数，防止冲突
            ```html::jinjia
            {% block scripts %}
            {{ super() }}
            <script type="text/javascript" src="my-script.js"></script>
            {% endblock %}
            ```