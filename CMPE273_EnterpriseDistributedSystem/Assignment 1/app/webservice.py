from flask import Flask,json,jsonify
from flask import request
from alchemy import db
from alchemy import ems
from alchemy import CreateDB

app=Flask(__name__)


CreateDB()
db.create_all()

@app.route('/v1',methods=['POST'])
def welcome():
	return "Welcome to the Web Service App"

@app.route('/v1/expenses',methods=['POST'])
def insert_expense():
	request_json = request.get_json(force=True)
	obj_ems= ems(request_json['name'],request_json['email'],request_json['category'],request_json['description'],request_json['link'],request_json			           ['estimated_costs'] ,request_json['submit_date'])
	db.session.add(obj_ems)
	db.session.commit()
	return jsonify({
			'id':obj_ems.id,
			'name':obj_ems.name,
			'email':obj_ems.email,
			'category':obj_ems.category,
			'description':obj_ems.description,
			'link':obj_ems.link,
			'estimated_costs':obj_ems.estimated_costs,
			'submit_date':obj_ems.submit_date,
			'decision_date':obj_ems.decision_date,
			'status':obj_ems.status,
			}),201

@app.route('/v1/expenses/<int:expenseid>',methods=['GET','PUT','DELETE'])
def request_update(expenseid):
	if request.method== 'GET':
		show_data=ems.query.filter_by(id=expenseid).first_or_404()
		return jsonify({
			'id':show_data.id,
			'name':show_data.name,
			'email':show_data.email,
			'category':show_data.category,
			'description':show_data.description,
			'link':show_data.link,
			'estimated_costs':show_data.estimated_costs,
			'submit_date':show_data.submit_date,
			'decision_date':show_data.decision_date,
			'status':show_data.status
			}),200

	elif request.method =='PUT':
		request_json=request.get_json(force=True)
		obj_update=ems.query.filter_by(id=expenseid).first_or_404()

		obj_update.estimated_costs=request_json['estimated_costs']
		db.session.commit()
		return jsonify({'status':True}),202

	elif request.method =='DELETE':
		delete_obj=ems.query.filter_by(id=expenseid).first_or_404()
		db.session.delete(delete_obj)
		db.session.commit()
		return jsonify({'status':True}),204	


if __name__ == '__main__':
   app.run("0.0.0.0",debug=True)
