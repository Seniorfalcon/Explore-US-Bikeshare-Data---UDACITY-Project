import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the City : ").lower()
        if city not in CITY_DATA:
            print("please enter a valid city")
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month or enter all if you want to display all months: ").lower()
        months = ['januart', 'february', 'march', 'april', 'may', 'june']
        if month != "all" and month not in months:
            print('please enter a valid month')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter a weekday or enter all days if you want to display all days of week: ").lower()
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if day != "all" and day not in days:
            print('please enter a valid day')
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != "all":
        months = ['januart', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != "all":
        df=df[df['day_of_week'] == day.title()]

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('the most common month is : ', most_common_month)


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day = df['day_of_week'].mode()[0]
    print('the most day month is : ', common_day)


    # TO DO: display the most common start hour
    df['houe'] = df['Start Time'].dt.hour
    common_hour = df['houe'].mode()[0]
    print('the most common start hour is : ',common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('the most commonly used start station is : ',common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('the most commonly used end station is : ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + "to" + df['End Station']).mode()[0]
    print('most frequent combination of start station and end station are :',common_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time is : ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time is : ',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    print('the counts of each user types are : ',counts_of_user_type)


    ### TO DO: Display counts of gender
    if 'Gender' in df:
        counts_of_gender = df['Gender'].value_counts()
        print('counts of gender is : ',counts_of_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earlist = df['Birth Year'].min()
        print('the earlist year of birth is : ',earlist)
        most_recent = df['Birth Year'].max()
        print('the most recent year of birth is : ',most_recent)
        most_common = df['Birth Year'].mode()[0]
        print('the most common year of birth is : ',most_common)
    else:
        print('invalid birth year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_display(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


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
