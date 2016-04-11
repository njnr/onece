#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role, Permission, Post
from flask.ext.script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)



def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def loaddb():
    db.drop_all()
    db.create_all()
    Role.insert_roles()
    u = User(email='skyfan1981@gmail.com', username='harry', password='single', 
        confirmed=True)
    u1 = User(email='harry.fan@foxmail.com', username='imguagua', password='single',
        confirmed=True)
    db.session.add(u)
    db.session.add(u1)
    db.session.commit()
    
    u.role = Role.query.filter_by(permissions=0xff).first()
    u1.role =Role.query.filter_by(default=True).first()
    db.session.add(u)
    db.session.add(u1)
    User.generate_fake(100)
    Post.generate_fake(1000)
    print u.role
    print u1.role

if __name__ == '__main__':
    manager.run()
