
from flask import *
import sys

app = Flask(__name__)




@app.route('/')
def index():
    miles = []
    dates = []
    milefile = 'miles.txt'
    mileFile = open("miles.txt", 'r')
    for mile in mileFile.readlines():
        miles.append(str(mile.rstrip()))
    mileFile.close()
    dateFile = open("dates.txt")
    for date in dateFile.readlines():
        dates.append(str(date.rstrip()))
    dateFile.close()
    print("miles " + str(miles))
    print("dates " + str(dates))
    return render_template('home.html',miles=miles,dates=dates)

@app.route('/add_miles', methods=['GET', 'POST'])
def add_miles():
    if request.method == 'POST':
        
        print(request.form['miles'])
        print(request.form['date'])
        with open('miles.txt', 'a') as mile_file:
            mile_file.write(str(request.form['miles'])+'\n')
            mile_file.close()
        with open('dates.txt', 'a') as date_file:
            date_file.write(str(request.form['date'])+'\n')
            date_file.close()

    return render_template('add_miles.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
