from datetime import date, datetime, timedelta, timezone

# Creating date object
birthday = date(1994, 10, 26)   # (year, month, day)
# Access what day of the week
birthday.weekday()   # returns 0-Monday, 1-Tuesday, 2-Wednesday and so on...
# Access day, month year
birthday.day
birthday.month
birthday.year

# Math with dates
min(birthday, date.today())

# ISO 8601 format: YYYY-MM-DDTHH:MM:SS returns a string object
birthday.isoformat()

# strftime and strptime (string parse time)
'https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior'
datetime.strptime('string to be parsed', 'desired format')

# Creating datetime object
dt = datetime(year=2017, month=10, day=1, hour=15, minute=23, second=25, microsecond=500000)
# Replacing parts of datetime
dt_hr = dt.replace(minute=0, second=0, microsecond=0)

# A timestamp
ts = 1514665153.0
# Convert to datetime and print
datetime.fromtimestamp(ts)

# US Eastern Standard time zone
ET = timezone(timedelta(hours=-5))
# Timezone-aware datetime
dt = datetime(2017, 12, 30, 15, 9, 3, tzinfo = ET)
# India Standard time zone
IST = timezone(timedelta(hours=5, minutes=30))
# Convert to IST
dt.astimezone(IST)
# Adjusting timezone
dt.replace(tzinfo=timezone.utc)
# Change original to match UTC
dt.astimezone(timezone.utc)

# Time zone database
from dateutil import tz
# Eastern time
et = tz.gettz('America/New_York')

# Check if datetime is ambiguous
tz.datetime_ambiguous(birthday)
# When the start is later than the end, set the fold to be 1
tz.enfold(birthday)

# Loading datetimes with parse_dates
rides = pd.read_csv('capital-onebike.csv', parse_dates = ['Start date', 'End date'])
# or
rides['Start date'] = pd.to_datetime(rides['Start date'], format = "%Y-%m-%d %H:%M:%S")
# or display in total seconds
rides['Duration'].dt.total_seconds()   # emphasis on .dt.
# Average duration by month
rides.resample('M', on = 'Start date')['Duration seconds'].mean()
# Size per group
rides.groupby('Member type').size()

# Shortcuts to get not only the distribution but also the percentage
rides['Member type'].value_counts() / len(rides)   # Use .value_counts first the divide by len()

# Localizing and Handling ambiguous datetimes in pandas
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')
# See weekdays for first three rides
rides['Start date'].head(3).dt.day_name()
# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')
# Shift the indexes forward one, padding with NaT
rides['End date'].shift(1)
