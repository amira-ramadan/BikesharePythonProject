import time
import pandas as pd
import numpy as np

//main cities data
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
    userCityInput = ""
    usermonthInput = ""
    userdayInput = ""
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
    
    userCityInput = input("Enter City name (chicago, new york city, washington): ").lower()
    while userCityInput != "chicago" and userCityInput != "new york city" and userCityInput != "washington":
        print("Incorrect city. please select correct city")
        userCityInput = input("Enter City name (chicago, new york city, washington): ").lower()
        
        # TO DO: get user input for month (all, january, february, ... , june)
    
    while usermonthInput == "":    
        usermonthInput = input("Enter month name (january,february,march,april,may,june) or all to apply no day filter : ").lower()
        if usermonthInput != "all":
            if months.count(usermonthInput) > 0 :
                try:
                    monthIndex = months.index(usermonthInput) + 1
                except IndexError:
                    print("Incorrect month. please select correct month")
                    usermonthInput = ""
            else : 
                print("Incorrect month. please select correct month")
                usermonthInput = ""
       # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
             
    while userdayInput == "":    
        userdayInput = input("Enter day name (saturday,sunday,monday,tuesday,wednesday,thursday,friday) or all to apply no day filter : ").lower()
        if userdayInput != "all":
            if days.count(userdayInput) > 0 :
                try:
                    dayIndex = days.index(userdayInput) + 1
                except IndexError:
                    print("Incorrect day. please select correct day")
                    userdayInput = ""
            else : 
                print("Incorrect day. please select correct day")
                userdayInput = ""
              
    city = userCityInput
    month = usermonthInput
    day = userdayInput

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
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
       # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
        # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(start_time)

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print("Most comman month{}".format(popular_month))

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    # find the most popular month
    popular_day = df['day'].mode()[0]
    print("Most comman day{}".format(popular_day))

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print("Most comman hour{}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station : {}".format(df['Start Station'].value_counts().keys()[0]))

    # TO DO: display most commonly used end station
    print("most commonly used end station : {}".format(df['End Station'].value_counts().keys()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    print("frequent combination of start station and end station trip: {} , {}".format(df['Start Station'].value_counts()[0],df['End Station'].value_counts()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    sum_time = df['Trip Duration'].unique().sum()

    # TO DO: display total travel time
    print(" display total travel time : {}".format(sum_time))


    # TO DO: display mean travel time
    main_value = df['Trip Duration'].value_counts().index.tolist()
    print("display mean travel time : {}".format(sum_time/len(main_value)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Display counts of user types: {}".format(df['User Type'].value_counts()))
    
    if 'Gender' in df.columns :
        # TO DO: Display counts of gender
        print("Display counts of Gender: {}".format(df['Gender'].value_counts()))
    if 'Birth Year' in df.columns :
        # TO DO: Display earliest, most recent, and most common year of birth
        print("earliest year : {}".format(df['Birth Year'].value_counts().sort_index().keys()[0]))
        print("most recent year : {}".format(df['Birth Year'].value_counts().sort_index().keys()[-1]))
        print("most common year : {}".format(df['Birth Year'].value_counts().keys().max()))
    
    
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
        while restart.lower() == 'yes':
             print("{}\n".format(df.head(5)))
             df.drop(df.head(5).index,inplace=True)
             restart = input('\nWould you like to restart? Enterno yes or no.\n')

        if restart.lower() != 'yes':
             break
if __name__ == "__main__":
	main()
