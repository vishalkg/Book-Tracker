import os
basedir = os.path.abspath(os.environ.get('DB_DIR'))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'book-tracker.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
