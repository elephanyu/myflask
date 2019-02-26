# coding:utf-8
MAILSERVER = 'smtp.qq.com'
UNAME = '742453618@qq.com'
PWD = ''

def sendTextMail(toname=['elephanyu_fu@163.com'], text='python sendmail test'):
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText(text, 'plain', 'utf-8')
    mail = smtplib.SMTP(MAILSERVER, 25)
    mail.set_debuglevel(1)
    mail.login(UNAME, PWD)
    mail.sendmail(UNAME, toname, msg.as_string())
    mail.quit()

def sendFlaskMail(toname=['elephanyu_fu@163.com'], html='<h3>Hello, test!!!</h3>'):
    import html2text
    from flask import Flask
    from flask_mail import Mail, Message
    app = Flask(__name__)
    app.debug = True
    app.config['MAIL_SERVER'] = MAILSERVER
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_'] = True
    app.config['MAIL_USERNAME'] = UNAME
    app.config['MAIL_PASSWORD'] = PWD
    msg = Message('Test Subject', sender=UNAME, recipients=toname)
    msg.body = html2text.html2text(html)
    msg.html = html
    # mail.send() 对程序上下文有操作(读取app.config邮箱配置获取mailserver连接）
    app.app_context().push()
    mail = Mail(app)
    mail.send(msg)

if __name__ == '__main__':
    # sendTextMail()
    sendFlaskMail()