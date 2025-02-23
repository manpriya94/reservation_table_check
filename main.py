import datetime

import requests

url = 'https://www.tablecheck.com/en/shops/pizza-4ps-in-indiranagar/available/timetable'
date_today = str(datetime.date.today())
params = {

    "reservation[num_people_adult]": 2,
    "reservation[start_date]": date_today

}
response = requests.request("GET", url,params=params)

timetable = response.json()
print(timetable)
