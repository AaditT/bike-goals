
from flask import *
import sys
from datetime import *


app = Flask(__name__)



def dist_between_dates(date1, date2):
    date_format = "%m/%d/%Y"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days # that's it
def todaydate():
    now = datetime.now()
    now = now.strftime(str(datetime.today().month)+"/%d/%Y")
    return now


@app.route('/', methods=['GET','POST'])
def index():
    current_total_miles = 0.0
    number_of_rides = 0
    if request.method == 'POST':
        with open('miles.txt', 'a') as mile_file:
            mile_file.write(str(request.form['miles'])+'\n')
            mile_file.close()
        with open('dates.txt', 'a') as date_file:
            date_file.write(str(request.form['date'])+'\n')
            date_file.close()
    miles = []
    dates = []
    milefile = 'miles.txt'
    mileFile = open("miles.txt", 'r')
    for mile in mileFile.readlines():
        miles.append(str(mile.rstrip()))
        latest_mile = (miles[-1])
        current_total_miles += float(latest_mile)
        number_of_rides += 1
    mileFile.close()
    dateFile = open("dates.txt")
    for date in dateFile.readlines():
        dates.append(str(date.rstrip()))
    dateFile.close()
    current_days = dist_between_dates("1/1/2020",todaydate())
    current_mile_per_day = round((current_total_miles / current_days),2)
    required_mile_per_day = round((500/365),2)
    current_total_miles = round(current_total_miles, 2)
    return render_template(
        'home.html',
        miles=miles,
        dates=dates,
        current_total_miles=current_total_miles,
        number_of_rides=number_of_rides,
        current_days=current_days,
        current_mile_per_day=current_mile_per_day,
        required_mile_per_day=required_mile_per_day,
    )

"""
@app.route('/add_miles', methods=['GET', 'POST'])
def add_miles():
    if request.method == 'POST':


        with open('miles.txt', 'a') as mile_file:
            mile_file.write(str(request.form['miles'])+'\n')
            mile_file.close()
        with open('dates.txt', 'a') as date_file:
            date_file.write(str(request.form['date'])+'\n')
            date_file.close()

    return render_template('add_miles.html')
"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)
