- Flask-WTF
    - CSRF保护
        -  使用current_app.config\['WTF_CSRF_SECRET_KEY'\]，如果没有配置，则使用current_app.config['SECRET_KEY']
    - WTForms字段类型
        - StringField 文本字段
        - TextAreaField 多行文本字段
        - PasswordField 密码文本字段
        - HiddenField 隐藏文本字段
        - DateField 文本字段，值为 datetime.date 格式
        - DateTimeField 文本字段，值为 datetime.datetime 格式
        - IntegerField 文本字段，值为整数
        - DecimalField 文本字段，值为 decimal.Decimal
        - FloatField 文本字段，值为浮点数
        - BooleanField 复选框，值为 True 和 False
        - RadioField 一组单选框
        - SelectField 下拉列表
        - SelectMultipleField 下拉列表，可选择多个值
        - FileField 文件上传字段
        - SubmitField 表单提交按钮
        - FormField 把表单作为字段嵌入另一个表单
        - FieldList 一组指定类型的字段
    - WTForms验证函数
        - Email 验证电子邮件地址
        - EqualTo 比较两个字段的值；常用于要求输入两次密码进行确认的情况
            - EqualTo('password', message='Passwords must match')
        - IPAddress 验证 IPv4 网络地址
        - Length 验证输入字符串的长度
            - Length(5, 64)
        - NumberRange 验证输入的值在数字范围内
        - Optional 无输入值时跳过其他验证函数
        - DataRequired 确保字段中有数据，Required已经弃用
        - Regexp 使用正则表达式验证输入值
            - Regexp('^\[A-Za-z\]\[A-Za-z0-9_.\]*$',0,'Username must have only letters, numbers, dots or underscores')
        - URL 验证 URL
        - AnyOf 确保输入值在可选值列表中
            - AnyOf('xx', 'yy', 'zz')
        - NoneOf 确保输入值不在可选值列表中
    - 常用方法
        - form.is_submitted() 表单是否提交
        - form.validate() 验证提交的表单数据
        - form.validate_on_submit() 表单是否提交，提交了是否通过验证
        - 表单定义的应用方法
        
    - WTForms在html中的渲染
        - 字段渲染
            ```html::jinjia
            <form method="POST">
            {{ form.hidden_tag() }}
            {{ form.name.label }} {{ form.name(id='my-text-field') }}
            {{ form.submit() }}
            </form>
            ```
        - 使用Flask-Bootstrap渲染
            ```html::jinjia
            {% import "bootstrap/wtf.html" as wtf %}
            {{ wtf.quick_form(form) }}
            ```
        
