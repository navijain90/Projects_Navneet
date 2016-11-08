from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app=Flask(__name__)

HOSTNAME='localhost'
#HOSTNAME = '192.168.99.100'
#HOSTNAME = 'mydb'
DATABASE = 'ems_2'
PASSWORD = 'admin'
USER = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
def CreateDB():
	engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
	engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) #create db

db=SQLAlchemy(app)

class ems(db.Model):
	__tablename__='ems'
	id=db.Column('id',db.Integer,primary_key=True)
	name=db.Column('name',db.String(45))
	email=db.Column('email',db.String(45))
	category=db.Column('category',db.String(45))
	description=db.Column('description',db.String(45))	
	link=db.Column('link',db.String(45))
	estimated_costs=db.Column('estimated_costs',db.String(45))
	submit_date=db.Column('submit_date',db.String(45))
	decision_date=db.Column('decision_date',db.String(45))
	status=db.Column('status',db.String(45))

	def __init__(self,name,email,category,description,link,estimated_costs,submit_date):
		self.name=name
		self.email=email
		self.category=category
		self.description=description
		self.link=link
		self.estimated_costs=estimated_costs
		self.submit_date=submit_date
		self.decision_date='09-08-2016'
		self.status='pending'
	
	
	
