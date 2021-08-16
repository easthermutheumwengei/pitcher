from app import create_app,db
from flask_script import Manager,Server

# Creating app instance
# app = create_app('development')
app = create_app('production')

manager = Manager(app)
migrate = Migrate(app,db)


if__name__ == '__main__':
    manager.run()