import datetime

import requests

from process_timetable import process_timetable
from send_ses_email import send_email

url = "https://www.tablecheck.com/en/shops/pizza-4ps-in-indiranagar/available/timetable"
date_today = str(datetime.date.today())
params = {"reservation[num_people_adult]": 2, "reservation[start_date]": date_today}
response = requests.request("GET", url, params=params)

timetable = response.json()
print(timetable)

result = process_timetable(timetable)

if result is None:
    print("The function didn't return a value.")
else:
    send_email(
        "bc@prabodhagarwal.com",
        "agrawalpriyanka1612@gmail.com",
        "Test Email from SES",
        result,
        "",
    )
