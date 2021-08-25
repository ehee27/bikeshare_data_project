import pandas as pd
import numpy as np
import time
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(2.5)

def intro():
    print_sleep("We're going to explore some US bikeshare data!")
    print_sleep("We have 3 cities to choose from: Chicago, New York City and Washington")

# Get inputs from user, city, month, day
def user_inputs():
# Choose a City
    while True:
        cities = ['chicago','new york city','washington']
        city = input("Which city would you like to explore?:").lower()
        if city in cities:
            print_sleep("Okay, let's take a look at {}.".format(city))
            break
        else:
                print_sleep("Invalid response. Please try again:")
                continue

# Filter by Month
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input("Let's filter our data by month: January, February, March, April, May, June.\nPlease select a month:").lower()
        if month in months:
            break
        else:
            if month not in months:
                print_sleep("Invalid response. Please try again:")
                continue

# Filter by Day
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("Let's filter our data by day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\nPlease select a day:").lower()
        if day in days:
            break
        else:
            if day not in days:
                print_sleep("Invalid response. Please try again:")
                continue

    #print("City choice: {}\nMonth choice: {}\nDay choice: {}".format(city, month, day))
    return city, month, day

# Generate the DataFrame
def load_data(city, month, day):

    #city yields dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #call the month and day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    #filter by month to create new DF
    df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

#### date and time data results
def popular_time_data(df):

    print_sleep("Calculating bikeshare data...")
    #start timer
    start_time = time.time()

    # most common month to ride - mode
    print("The most popular month is", df['month'].mode()[0])

    # most common day of the day of week
    print("The most popular day is", df['day_of_week'].mode()[0])

    #stop timer
    e_t = ("execution: %s seconds" % (time.time() - start_time))

    # most common hours to ride
    #df['hour'] = df['Start Time'].mode()[0]

    print(e_t)
    time.sleep(2)

### stations and trip data results
def popular_stations_data(df):

    print_sleep("Calculating bikeshare data...")
    #start timer
    start_time = time.time()

    # most common starting station
    print("The most popular Start Station is", df['Start Station'].mode()[0])

    # most common end station
    print("The most popular End Station is", df['End Station'].mode()[0])

    # most common trip from start to finish - (combo of start/end stations)
    df['Common Trip'] = df['Start Station'] + " to " + df['End Station']
    print("The most common trip is", df['Common Trip'].mode()[0])

    e_t = ("execution: %s seconds" % (time.time() - start_time))
    print(e_t)
    time.sleep(2)

def run():
    while True:
        intro()
        city, month, day = user_inputs()
        df = load_data(city,month,day)
        popular_time_data(df)
        popular_stations_data(df)

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

 ####### QUESTIONS to ANSWER
def trip_duration():
    #3. Trip Duration

    # total travel time
    df['Trip Duration'].sum()

    # average travel time
    df['Trip duration'].mean()

#4. User Info
# counts of each user type
# counts of each gender (only avail NYC and Chicago)
# earliest, most recent, most common year of birth (only avail NYC and Chicago)
