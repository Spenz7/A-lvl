import flask, sqlite3
from flask import render_template,request

app = flask.Flask(__name__)

@app.route('/')
def form():
    
    return render_template('receivelocation.html')

@app.route('/process/')
def process():
    if 'location'  in request.args:
        db = sqlite3.connect('equipment.db')
        print(request.args)
        s = request.args['location']
        print(s)
        data = db.execute('select serialnumber, type from device where location = ?',(s,))
        print(data)
        rows = data.fetchall()
        print(rows)
        #rmb to close db
        db.close()
        return render_template('results.html',location = s, rows = rows)
    return 'No form data found'
    

    

if __name__ == '__main__':
    app.run()

