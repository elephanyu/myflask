import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'migrate.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer)

if __name__ == '__main__':
    '''
>>> python migrateTest.py db --help
usage: Perform database migrations

Perform database migrations

positional arguments:
  {init,revision,migrate,edit,merge,upgrade,downgrade,show,history,heads,branches,current,stamp}
    init                Creates a new migration repository
    revision            Create a new revision file.
    migrate             Alias for 'revision --autogenerate'
    edit                Edit current revision.
    merge               Merge two revisions together. Creates a new migration
                        file
    upgrade             Upgrade to a later version
    downgrade           Revert to a previous version
    show                Show the revision denoted by the given symbol.
    history             List changeset scripts in chronological order.
    heads               Show current available heads in the script directory
    branches            Show current branch points
    current             Display the current revision for each database.
    stamp               'stamp' the revision table with the given revision;
                        don't run any migrations
    usualy use: init migrate upgrade
    '''
    manager.run()