# Import the pandas library as pd
import pandas as pd
# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')
# Examine the head of the DataFrame
print(ri.head())
# Count the number of missing values in each column
print(ri.isnull().sum())
# Dropping columns uses .drop
ri.drop(['county_name', 'state'], axis='columns', inplace=True)
# Dropping rows uses .dropna
ri.dropna(subset=['driver_gender'], inplace=True)

# Checking dtype of colum
df.column.dtype   # this is dot notation
df['column'].dtype   # this is bracket notation

# Concatinating columns
date_time = apple['date'].str.cat(apple['time'], sep=' ')
# Converting to datetime object in pandas
pd.to_datetime(date_time)

# Counting unique values in a series
.value_counts()
# Expressing counts as proportions
.value_counts(normalize=True)

# Searching for strings
ri['inventory'] = ri.search_type.str.contains('Inventory', na=False)   # na=False returns False when it finds NaN

# dt accessor is not used with a DatetimeIndex

# Resampling
apple.groupby(apple.index.month).price.mean()
apple.price.resample('M').mean()   # same output

# Concatinating two df
monthly = pd.concat([monthly_price, monthly_volume], axis='columns')
# Plotting 2 variables agains common x-values
monthly.plot(subplots=True)

# Computing a frequency table
pd.crosstab(ri.driver_race, ri.driver_gender)

# Mapping one set of values to another
mapping = {'up':True, 'down':False}
apple['is_up'] = apple['change'].map(mapping)

# Changing datatype from object to category
cats = ['short', 'medium', 'long']
ri['stop_length'] = ri.stop_length.astype('category', ordered=True, categories=cats)
# or
cats = pd.CategoricalDtype(['short', 'medium', 'long'], ordered=True)
ri['stop_length'] = ri.stop_length.astype(cats)

# Merging dataframes
apple_high = pd.merge(left=apple, right=high, left_on='date', right_on='DATE', how='left')

# Converting a multi-indexed Series to a DataFrame
search_rate.unstack()
# or
ri.pivot_table(index='violation', columns='driver_gender', values='search_conducted')

