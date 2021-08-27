# we want to inform the user that we're exploring bikeshare data from one of three cities
# they will select a city
# they will then choose to filter data by month, day or none
# we will build the dataframe according to their selections
# answer questions per time, stations, and user data

import pandas as pd
import numpy as np
import time
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# print the messages and sleep
def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(2.5)

def intro():
    print_sleep("Let's explore some US bikeshare data!")
    print_sleep("\nWe have 3 cities to choose from: Chicago, New York City and Washington")

# Get inputs from user, city, month, day
def user_inputs():
# Choose a City
    while True:
        cities = ['chicago','new york city','washington']
        city = input("\nWhich city would you like to explore?").lower()
        if city in cities:
            print_sleep(city.title() + " it is.")
            break
        else:
                print_sleep("Invalid response. Please try again:")
                continue

# Filter by Month
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input("\nLet's filter our data by month: January, February, March, April, May, June.\n\nPlease select a month:\n").lower()
        if month in months:
            print_sleep("\nCool, let's look more closely at " + month.title() + ".")
            break
        else:
            if month not in months:
                print_sleep("Invalid response. Please try again:")
                continue

# Filter by Day
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("\nLet's filter our data by day: Monday - Sunday.\nPlease select a day of the week:\n").lower()
        if day in days:
            print_sleep("\nOkay, " + day.title() + " is our chosen day of the week.")
            break
        else:
            if day not in days:
                print_sleep("Invalid response. Please try again:")
                continue

    print("\nCity choice: {}\nMonth choice: {}\nDay choice: {}".format(city.title(), month.title(), day.title()))
    return city, month, day

# Generate the DataFrame
def load_data(city, month, day):

    # city yields dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # call the month and day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create new DF
    df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

### Questions to answer based off df results

###### popular times data
def popular_time_data(df):

    #start timer to calculate executions
    print_sleep("\nCalculating bikeshare data for time stats...")
    start_time = time.time()

    # most common month to ride - mode
    print("The most popular month is", df['month'].mode()[0])

    # most common day of the day of week
    print("The most popular day is", df['day_of_week'].mode()[0])

    # most common hour to ride
    df['hour'] = df['Start Time'].dt.hour.mode()[0]

    # stop timer
    e_t = ("execution: %s seconds" % (time.time() - start_time))

    print(e_t)
    time.sleep(2)

###### stations data
def popular_stations_data(df):

    # start timer to calculate executions
    print_sleep("\nCalculating bikeshare data for station stats...")
    start_time = time.time()

    # most common starting station
    print("The most popular Start Station is", df['Start Station'].mode()[0])

    # most common end station
    print("The most popular End Station is", df['End Station'].mode()[0])

    # most common trip from start to finish - (combo of start/end stations)
    df['Common Trip'] = df['Start Station'] + " to " + df['End Station']
    print("The most common trip is", df['Common Trip'].mode()[0])

    # stop timer
    e_t = ("execution: %s seconds" % (time.time() - start_time))
    print(e_t)
    time.sleep(2)

###### trip data
def trip_duration_data(df):

    # start timer to calculate executions
    print_sleep("\nCalculating bikeshare data for trip stats...")
    #start timer
    start_time = time.time()

    # total travel time
    print("Total travel time is", df['Trip Duration'].sum())

    # average travel time
    print("Average travel time is", df['Trip Duration'].mean())

    e_t = ("execution: %s seconds" % (time.time() - start_time))
    print(e_t)
    time.sleep(2)

####### user data
def user_data(df, city):

    # start timer to calculate executions
    print_sleep("\nCalculating bikeshare data for user stats...")
    #start timer
    start_time = time.time()

    # count each type of user
    user_type = df.groupby(['User Type'])['User Type'].count()
    print("User Type count:", df['Trip Duration'].sum())

    # counts gender type (only available NYC and Chicago)
    cities2 = ['chicago','new york city']
    if city in cities2:
        gender_type = df.groupby(['Gender'])['Gender'].count()
        print("Gender Type count:", df['Trip Duration'].mean())
    else:
        pass

    # earliest, most recent, most common birth year (only available NYC and Chicago)
    if city in cities2:
        print("The earliest birthday is", df['Birth Year'].min())
        print("The most recent birthday is", df['Birth Year'].max())
        print("The most common birth year is", df['Birth Year'].value_counts())

    e_t = ("execution: %s seconds" % (time.time() - start_time))
    print(e_t)
    time.sleep(2)

def play_again():
    while True:
        replay = input("Would you like to explore more?\nPlease choose y or n:").lower()
        if "y" in replay:
            run()
        elif "n" in replay:
            print("Have a nice day!")
            break
        else:
            if "y" and "n" not in reaply:
                print_sleep("Invalid response. Please try again:")
                continue
            replay()
            break

# run the program
def run():
    while True:
        intro()
        city, month, day = user_inputs()
        df = load_data(city, month, day)
        popular_time_data(df)
        popular_stations_data(df)
        trip_duration_data(df)
        user_data(df, city)
        play_again()


# Will I need to split off into filter choices (month, day, none) with separate load_data?
# or, can I do it all withint the same loop?

# Choose a filter
#    while True:
#        filters = ['month','day','none']
#        print_sleep("\nLet's filter our data. Would you like to filter by month, day or not at all?")
#        filter = input("Please input month, day or 'none'.").lower()
#        if filter in filters:
#            if filter == 'month':
#                month_filter()
#            elif filter == 'day':
#                day_filter()
#            elif filter == 'none':
#                none_filter()
#         else:
#            print_sleep("Invalid response. Please try again.")
