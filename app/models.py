#Python class to represent tables in database
from app import db #instead of again initalizing obj like db=SQLALCHEMY(); we have imported already defined ones in other module that follow up the rule of reuseablity
class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    status=db.Column(db.String(20),default="Pending")
