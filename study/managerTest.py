from flask import Flask
from flask_script import Manager, Command

app = Flask(__name__)
manager = Manager(app)

class Hello(Command):
    # rewrite flask_script.Command.run method
    # cant run with args[too many arguments]
    def run(self):
        print 'Hello, World!!!'

manager.add_command('hello', Hello())

@manager.command
def world():
    # cant run with args[too many arguments]
    print 'hello, world!!!'

@manager.option('-a', '--args', dest='arg1', default=None, help="the arg1")
@manager.option('-r', '--recycle', dest='arg2', default=None, help="the arg2")
@manager.option('-g', '--generate', dest='arg3', default='arg3', help="the arg3, default is arg3")
def test(**kwargs):
    print kwargs

if __name__ == '__main__':
    '''
    >>> python managerTest.py hello
    >>> python managerTest.py world
    >>> python managerTest.py hello -a 1 -r 2 -g 3
        {'arg1': u'1', 'arg2': u'2', 'arg3': u'3'}
    >>> python managerTest.py hello fasdf
        usage: managerTest.py [-?] {hello,world,test,shell,runserver} ...
        managerTest.py: error: too many arguments
    >>> python managerTest.py hello --help
        usage: managerTest.py hello [-?]
        optional arguments:
        -?, --help  show this help message and exit
    '''
    manager.run()
