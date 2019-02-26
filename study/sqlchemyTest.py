# coding:utf-8
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

def make_shell_context():
    return dict(db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))

class TestOperation(object):
    def createAll(self):
        db.create_all()

    def insert(self):
        role_test = Role(name='test')
        db.session.add(role_test)
        # db.session.add_all([role_user, role_test])
        db.session.commit()

    def __call__(self, *args, **kwargs):
        return db

if __name__ == '__main__':
    '''
    table operation：
    >>> db.drop_all()
    >>> db.create_all()
    
    insert：
    >>> user_role = Role(name='User')
    >>> user_david = User(username='david', role=user_role)
    >>> print(user_role.id)
        None
    >>> db.session.add(user_role)
    >>> db.session.add(user_david)
    >>> db.session.commit()
    >>> print(user_role.id)
        3
    
    update：
    >>> admin_role.name = 'Administrator'
    >>> db.session.add(admin_role)
    >>> db.session.commit()
    
    delete：
    >>> db.session.delete(mod_role)
    >>> db.session.commit()
    
    query：
    >>> Role.query.all()
        [<Role u'Administrator'>, <Role u'User'>]
    >>> User.query.filter_by(role=user_role).all()
        [<User u'susan'>, <User u'david'>]
    >>> str(User.query.filter_by(role=user_role))
        'SELECT users.id AS users_id, users.username AS users_username,
        users.role_id AS users_role_id FROM users WHERE :param_1 = users.role_id'
    '''
    manager.run()