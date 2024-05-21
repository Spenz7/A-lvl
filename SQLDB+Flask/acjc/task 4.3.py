import flask, sqlite3
from flask import render_template, request

app = flask.Flask(__name__)

@app.route('/')
def form():
    return render_template('receiveservicestatus.html')


@app.route('/process/')
def process():
    if 'service_status'  in request.args:
        db = sqlite3.connect('records.db')
        print(request.args)
        s = request.args['service_status']
        print(s)
        data = db.execute('select Employee_name, Service_status from Employee where Service_status = ?',(s,))
        #data is  object
        #use fetchall when select is used for db.execute select
        rows = data.fetchall() #take out records from object
        print(rows)
        namerows = []
        for i in rows:
            namerows.append(i[0])
        namerows.sort()
        
       
        
        #rmb to close db
        db.close()
        return render_template('results.html',service_status = s, rows = namerows)
    return 'No form data found'



if __name__ == '__main__':
    app.run()
