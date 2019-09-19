from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app02 import create_app, db

app = create_app()
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def func(args):
    print(args)
    return args


@manager.option('--who', dest='who')
@manager.option('-a', '--age', dest='age')
def func2(who, age):
    print(who, age)
    return who, age


if __name__ == '__main__':
    manager.run()
