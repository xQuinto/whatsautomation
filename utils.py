import datetime
import pywhatkit


def time_to_send():
    print("Now lets talk about the time you want it to send. I'll ask you the hours(24) and minutes apart.")
    hour = input("hour:")
    minutes = input("minutes:")
    int_hour = int(hour)
    int_minutes = int(minutes)
    while int_minutes > 59:
        int_minutes = int_minutes - 60
        int_hour = int_hour + 1
    return int_hour, int_minutes


def dag_tekst(now):
    if now.hour < 12:
        dag_teksts = "Good morning, "
    elif now.hour > 18:
        dag_teksts = "Good afternoon, "
    else:
        dag_teksts = "I wish you a good day, "
        # de now.minute + interval aanpassen voor als ddit meer dan 60 wordt
    return dag_teksts


def make_screenshot():
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    hours = str(now.hour)
    minute = str(now.minute)
    pywhatkit.take_screenshot("whatsapp" + year + "-" + month + "-" + day + "-" + hours + "-" + minute, 20)

