import pandas as pd
import numpy as np
import time
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(2)

# Get inputs from user, city, month, day
def user_inputs():
    while True:
        explore_data = input("Would you like to see bikeshare data for Chicago, New York, or Washington?\nPlease choose y or n:").lower()
        if "y" in explore_data:
            break
        elif "n" in explore_data:
            close_out()
        else:
            if "y" and "n" not in explore_data:
                print_sleep("Invalid response. Please try again:")
                continue

# Choose a City
    while True:
        city = input("Please choose a city - Chicago, New York City, Washington.\nWhich city?:").lower()
        if "chicago" in city:
            break
        elif "new york city" in city:
            break
        elif "washington" in city:
            break
        else:
            if "chicago" and "new york city" and "washington" not in city:
                print_sleep("Invalid response. Please try again:")
                continue

# Filter by Month
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input("Let's filter our data by month - January, February, March, April, May, June\nPlease select a month:").lower()
        if month in months:
            break
        else:
            if month not in months:
                print_sleep("Invalid response. Please try again:")
                continue

# Filter by Day
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("Let's now add a day to the filter - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\nPlease select a day:").lower()
        if day in days:
            break
        else:
            if day not in days:
                print_sleep("Invalid response. Please try again:")
                continue

    print("City choice: {}\nMonth choice: {}\nDay choice: {}".format(city, month, day))
    return city, month, day
    load_data(city, month, day)

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
