from app import create_app
from flask_script import Server,Manager
app = create_app('development') 
manager = Manager(app)
manager.add_command('server',Server())
@manager.command
def test():
    """Run test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verboity=2).run(tests)
if __name__ == '__main__':
    manager.run()
