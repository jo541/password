# coding: utf8
from server import app,conn,cr
from random import *
from flask import render_template,url_for,request

@app.route('/')
def index():
   	 url_for('static', filename='css')
	 return render_template('index.html')
@app.route('/generate_pass/',methods=['POST','GET'])
def generate_pass():
	password_to_return = ''
	complete_num =''
	number = False
	special_char = False
	if request.method == 'POST':
		if request.form['number']:
			number = True
		if request.form['special_char']:
			special_char = True
	for i in range(0,6):
		complete_num = ""
		for j in range(0,6):
			random_num=int(random()*6+1)
			complete_num += str(random_num)
		cr.execute("""SELECT word FROM word WHERE id = {}""".format(int(complete_num)/2))
		words = cr.fetchone()
		for word in words :
			print(type(word))
			uni_word = unicode(word)
			print(type(uni_word))
			print(uni_word.encode('UTF-8'))
			password_to_return += uni_word.encode('UTF-8')
	return render_template('index.html',number_to_return=password_to_return)

