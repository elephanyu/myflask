# coding: utf-8
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from flask_script import Manager, Shell

app = create_app('default')
manager = Manager(app)

def make_shell_context():
    return dict(db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)

manager.add_command("shell", Shell(make_context=make_shell_context))

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    '''
    1、初始化数据库，角色列表
    python myflask.py shell
    >>> db.create_all()
    >>> Role.insert_roles()
    2、运行web并注册账号
    python myflask.py runserver
    '''
    # No handlers could be found for logger "root"
    import logging
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(pathname)s - %(filename)s - %(funcName)s - %(message)s"
    logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)
    manager.run()
