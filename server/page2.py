from server import app

@app.route('/page2')
def page2():
	return 'Hello page2'
