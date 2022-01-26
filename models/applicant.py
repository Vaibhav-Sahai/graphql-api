from sqlite3 import Timestamp
from orator import Model
from db import Model

class Applicant(Model):
    __table__ = 'applicants'
    __fillable__ = ['name', 'email', 'gpa']
    __timestamps__ = False

    pass

