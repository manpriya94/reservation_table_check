import requests

url = 'https://www.tablecheck.com/en/shops/pizza-4ps-in-indiranagar/available/timetable'
params = {

    "reservation[num_people_adult]": 2,
    "reservation[start_date]": '2025-02-23'

}
response = requests.request("GET", url,params=params)

timetable = response.json()
