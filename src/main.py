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
    ''' This is a function and requires a comment to make pylint happy'''
    #reminder_name = input("What do you want to call this reminder? ")
    reminder_name = "Take over world with python"
    reminder_time = input("In how many minutes should I remind you? ")

    minute_increase = int(reminder_time)
    if minute_increase < 1:
        raise ValueError("reminder must be greater than 1")

    #hours_increase = int(reminder_time[:2])
    #minute_increase = int(reminder_time[2:])

    #print(datetime.now())
    time_to_remind = datetime.now() + timedelta(minutes=minute_increase)

    print("I'll remind you of [{0}] at {1}.".format(reminder_name, time_to_remind.strftime("%I:%M")))
    print()

    seconds_in_minutes = 60
    zzz(minute_increase * seconds_in_minutes)

    print("Hey!")
    print("HEY!\n")
    print("time to: {0}".format(reminder_name))
    webbrowser.open("https://www.youtube.com/watch?v=N4mEzFDjqtA")

welcome_message()
ask_for_reminder()
