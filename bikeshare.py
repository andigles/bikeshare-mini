import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
VALID_CITIES = ["chicago", "new your city", "washington"]
VALID_MONTHS = ["all", "january", "february", "march", "april", "may", "june"] # Data available only up to june
VALID_DAYS = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Select your city (chicago, new york city, washington): ").lower()
        if city in VALID_CITIES:
            break
        print("Invalid city. Type one of the available cities (chicago, new york city, washington)")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month (all, january, february, march, april, may, june): ").lower()
        if month in VALID_MONTHS:
            break
        print("Invalid month. Type one of the available options for month (all, january, february, march, april, may, june)")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day of week (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()
        if day in VALID_DAYS:
            break
        print("Invalid day. Type one of the available options for day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data from selected city
    df = pd.read_csv(CITY_DATA[city])
    #print(df.head())
    
    # Convert Start Time column in datetime format
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    # Select month from the data
    if month != "all":
        df = df[df["Start Time"].dt.month_name().str.lower() == month]
        
    if day != "all":
        df = df[df["Start Time"].dt.day_name().str.lower() == day]
        
    print(f"df shape: {df.shape}")
    print(f"first 5 rows of df:\n {df.head()}")

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
