#!/usr/bin/env python
from datetime import datetime, timedelta
from time import sleep as zzz
import webbrowser
'''
look at me go! comments and all
I should comment this when I understand its voodoo
This triple double (or single) quotes removes the missing docstring module warning from pylint
'''
def welcome_message():
    ''' Friendly message to user '''
    print("Welcome to the simplest reminder (not to be used for work)!\n")

def ask_for_reminder():
    ''' takes in minutes to remind and opens url'''
    reminder_name = input("What do you want to call this reminder? (optional) ")
    reminder_time = input("In how many minutes should I remind you? ")

    if len(reminder_name) < 1:
        reminder_name = "Take over world with python"

    minute_increase = int(reminder_time)
    if minute_increase < 1:
        raise ValueError("reminder must be greater than 1")

    time_to_remind = datetime.now() + timedelta(minutes=minute_increase)

    print("I'll remind you of [{0}] at {1}.".format(reminder_name, time_to_remind.strftime("%I:%M")))
    print()

    seconds_in_minute = 60
    zzz(minute_increase * seconds_in_minute)

    print("Hey!")
    print("HEY!\n")
    print("time to: {0}".format(reminder_name))
    webbrowser.open("https://www.youtube.com/watch?v=N4mEzFDjqtA")

welcome_message()
ask_for_reminder()
