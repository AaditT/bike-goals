from datetime import *
def todaydate():
    now = datetime.now()
    now = now.strftime(str(datetime.today().month)+"/%d/%Y")
    return now


todaydate()

def dist_between_dates(date1, date2):
    date_format = "%m/%d/%Y"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days # that's it

print(dist_between_dates("1/1/2020", todaydate()))
