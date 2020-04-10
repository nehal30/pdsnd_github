Import time
import pandas as pd
import numpy as np
import datetime as dt
# load data file into a dataframe
city_data = pd.read_csv (r’/c/Users/computec/Desktop/project2/chicago.csv, /c/Users/computec/Desktop/project2/Washington.csv, /c/Users/computec/Desktop/project2/new_york_city.csv ')
     another solution                    
chicago =  pd.read_csv (r’/c/Users/computec/Desktop/project2/chicago.csv)
new york city = pd.read_csv (r’/c/Users/computec/Desktop/project2/new_york_city.csv) 
 washington =  pd.read_csv (r’/c/Users/computec/Desktop/project2/ washington.csv) 


#  create the dictionary city_data to group the imported cities .csv
 city_data = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }

# creating a DataFrame manually from a dictionary city_data , then passing the dictionary city_data to the pd.DataFrame() function.
dataframes = []
for city in city_data:
cities =dataframes.append(pd.read_csv(chicago))
#selecting data filters, city, month, day
    print('\nHello! Let\'s explore some US bikeshare data!\n')

  """
Specifiying a city, month, and day to analyze
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""
def get_filters():
    cities = ['Chicago','New York','Washington']
    months = ['January','Feburary','March','April','May','June','All']
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

    # selecting for city (Chicago, New York, Washington).
""" selecting the city that we want to analyze from the cities list that have been filtered"""
    while True:
        city = input('\n"Chicago\", \"New York\" or \"Washington\" \n')
        if city.title() in cities:
            print('\n {}.'.format(city.title()))
            break
 #    selecting month (January - June or All).
""" selecting the month or all monthes that we want to analyze from the cities list that have been filtered"""
    while True:
        month = input('\nDo you want to search for a specific month? You can pick data from January to June. If you need data for all months, just enter All. \n')
        if month.title() in months:
            print('\n {}.'.format(month.title()))
            break
    # selecting day of week (Sunday - Saturday or All)
""" selecting the day of week that we want to analyze from the cities list that have been filtered"""
    while True:
        day =      input('\n'Monday\','Tuesday\','Wednesday\','Thursday\','Friday\','Saturday\','Sunday\','All'\n')
        if day.title() in days_of_week:
            print('\n {}.'.format(day.title()))
            break
#    Loading data for analysis based on city, month, and day filters
"""creating data frame for each city"""
   def load_data(city, month, day):
    df = pd.read_csv.cities(city)

#1 Popular times of travel (i.e., occurs most often in the start time(Which is the most common month preferable for travelling for the 3 cities?)
    # Converting the Start Time column to datetime
"""selecting an object (start time column ) from the data frame (df) and converting it to date time using date time function """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extracting month and day from Start Time column to create a new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #Month filter - using the index of the month from list to get corresponding int
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    #  Created new dataframe for month by filtering the month
        df = df[df['month'] == month]
# the most common day of  week 
#  filter by day of week if applicable
    if day != 'all':
  """Created new dataframe for day””’
        df = df[df['day_of_week'] == day.title()]
    return df 

	    """Displaying the statistics for the Most frequent time to travel"""
	def time_stats(df):
	    print('\nCalculating The Most Frequent Times of Travel...\n')
	    start_time = time.time()
	    df['Start Time'] = pd.to_datetime(df['Start Time'])
      	    # Most common month
	    df['Month'] = df['Start Time'].dt.month
	Common_month = df['month'].mode()[0]
         “””find the most popular month””’

           print( 'Most common month: ', common _ month )

	    # Most common day of week
	    df['day_of_week'] = df['Start Time'].dt.day
            “””find the most common day “””
	common_day = df['day_of_week'].mode()[0]
    print( 'Most common day : ', common_ day )

    # Most common hour
    df['hour'] = df['Start Time'].dt.hour
  common_hour = df['hour'].mode()[0]
    print('Most popular hour: ', common_hour)   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#2 Popular stations and trip
    #   Most popular stations and trip
	def station_stats(df):
 """Displays statistics on the most popular stations and trip."""
	    print('\nCalculating The Most Popular Stations and Trip...\n')
	    start_time = time.time()
	  #  Most common start station
df['common_start'] = df['Start Station']
    """display most commonly used start station"""
       common_Start = df['common_start'].mode()[0]
       print ('The most common start station is: ', common_Start)

    # C #   Common end station
    df['common_end'] = df['End Station']
    common_end = df['common_end'].mode()[0]
    print('The most common end station is: ', common_end)
    # Frequent start and end station
    common_trip = df['common_start'] + ' to ' + df['common_end']
    print ('The most common trip is: ', common_trip.mode()[0])
    another solution
 """display most frequent combination of start station and end station trip"""
    common_trip = (df['Start Station']+df['End Station']).mode()[0]
    print(common_trip)

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

  #    Trip duration function
 """Displays statistics on the total and average trip duration."""
def trip_duration_stats(df):
print('\nCalculating Trip Duration...\n')
start_time = time.time()
	    #  Trip start time
	    trip_start = pd.to_datetime(df['Start Time'])
		    #  Trip end time
	    trip_end = pd.to_datetime(df['End Time'])
		    #  Total trip time - new column
	    df['Trip Total Time'] = trip_start - trip_end
	    #  Adding total trip
	    total_time =  df['Trip Total Time'].sum()
	    print("The total amount of time for a trip is: " + str(total_time))
Average travel time
	    mean_time = df['Trip Duration'].mean()
	    print("The average time of a trip is: " + str(mean_time))
	    print("\nThis took %s seconds." % (time.time() - start_time))
                 print('-'*40)	
another solution
# display total travel time
    total_travel = df['Trip Duration'].sum()
    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Total travel time: ", total_travel)
    print("mean travel time: ", mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
	
    	    # User data Function
	def user_stats(df):
 """Displays statistics on bikeshare users."""
	    print('\nCalculating User Stats...\n')
	    start_time = time.time()
	     # Count user type
	    user_type = df['User Type'].value_counts()
	    # Count gender
	    gender = df['Gender'].value_counts()
	    # Earliest and most common year of birth
	    earliest_year = df.sort_values('Birth Year').iloc[0]
	    common_year = df['Birth Year'].mode() [0]
another solution
df =df.sort_values(by='birth year',descending=True)
return. df
 # Display earliest, most recent, and most common year of birth
    earliest_birthdate = df['Birth Year'].min()
    most_recent_birthdate = df['Birth Year'].max()
    most_common_birthdate = df['Birth Year'].mode()
	    print('Count of user types: ', user_type)
	    print('Count of gender: ', gender)
	    print('Oldest person to rent: ', earliest_year['Birth Year'])
	    print('Most common birth year: ', common_year)
	    print("\nThis took %s seconds." % (time.time() - start_time))
              print('-'*40)

	    # Additional data
	def display_data(df):
	    view_data = input('Would you like to see the next five rows of data? Yes or No: ')
	    view_data = view_data.lower()
	    if view_data == 'yes':
	        print(df.head(5))
	        display_data(df)
	    else:
	        exit(print("Thank you for Exploring US Bikeshare Data"))
	    # Main Funtion - Call all the funtions
	def main() -> object:
	    while True:
	        city, month, day = get_filters()
	        df = load_data(city, month, day)
	        time_stats(df)
	        station_stats(df)
	        trip_duration_stats(df)
	        user_stats(df)
	        display_data(df)
	        restart = input('\nWould you like to restart? Enter yes or no.\n')
	        if restart.lower() != 'yes':
	            break
	if __name__ == "__main__":
	    main()






