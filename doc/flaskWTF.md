- Flask-WTF
    - CSRF保护
        ```python
        from flask import Flask
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'hard to guess string'
        ```
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
        - IPAddress 验证 IPv4 网络地址
        - Length 验证输入字符串的长度
        - NumberRange 验证输入的值在数字范围内
        - Optional 无输入值时跳过其他验证函数
        - Required 确保字段中有数据
        - Regexp 使用正则表达式验证输入值
        - URL 验证 URL
        - AnyOf 确保输入值在可选值列表中
        - NoneOf 确保输入值不在可选值列表中
        
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
    
    - example
        ```python
        from flask_wtf import FlaskForm
        from wtforms import StringField, TextAreaField, BooleanField, SelectField, PasswordField, SubmitField
        from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
        from wtforms import ValidationError
        from ..models import Role, User
        
        # 用户信息表单
        class EditProfileForm(FlaskForm):
            name = StringField('Real name', validators=[Length(0, 64)])
            location = StringField('Location', validators=[Length(0, 64)])
            about_me = TextAreaField('About me')
            submit = SubmitField('Submit')
        
        # 管理员信息表单       
        class EditProfileAdminForm(FlaskForm):
            email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                                     Email()])
            username = StringField('Username', validators=[
                DataRequired(), Length(1, 64),
                Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                       'Usernames must have only letters, numbers, dots or '
                       'underscores')])
            confirmed = BooleanField('Confirmed')
            role = SelectField('Role', coerce=int)
            name = StringField('Real name', validators=[Length(0, 64)])
            location = StringField('Location', validators=[Length(0, 64)])
            about_me = TextAreaField('About me')
            submit = SubmitField('Submit')
        
            def __init__(self, user, *args, **kwargs):
                super(EditProfileAdminForm, self).__init__(*args, **kwargs)
                self.role.choices = [(role.id, role.name)
                                     for role in Role.query.order_by(Role.name).all()]
                self.user = user
        
            def validate_email(self, field):
                if field.data != self.user.email and \
                        User.query.filter_by(email=field.data).first():
                    raise ValidationError('Email already registered.')
        
            def validate_username(self, field):
                if field.data != self.user.username and \
                        User.query.filter_by(username=field.data).first():
                    raise ValidationError('Username already in use.')
        
        # 用户注册表单            
        class RegistrationForm(FlaskForm):
            email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                                     Email()])
            username = StringField('Username', validators=[
                DataRequired(), Length(1, 64),
                Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                       'Usernames must have only letters, numbers, dots or '
                       'underscores')])
            password = PasswordField('Password', validators=[
                DataRequired(), EqualTo('password2', message='Passwords must match.')])
            password2 = PasswordField('Confirm password', validators=[DataRequired()])
            submit = SubmitField('Register')
        
            def validate_email(self, field):
                if User.query.filter_by(email=field.data).first():
                    raise ValidationError('Email already registered.')
        
            def validate_username(self, field):
                if User.query.filter_by(username=field.data).first():
                    raise ValidationError('Username already in use.')
        ```
        
