# Removing $ from Revenue Column then Converting to int
sales['Revenue'] = sales['Revenue'].str.strip('$')
sales['Revenue'] = sales['Revenue'].astype('int')

# Verify that Revenue is now an integer
assert sales['Revenue'].dtype == 'int'

# Convert to categorical
df['Status'] = df['Status'].astype('category')

# Drop values using filtering
movies = movies[movies['avg_rating'] <= 5]
# Drop values using .drop()
movies.drop(movies[movies['avg_rating'] > 5].index, inplace = True)   # .drop(index to be dropped, inplace=True)
# Convert avg_rating > 5 to 5
movies.loc[movies['avg_rating'] > 5, 'avg_rating'] = 5
# Assert results
assert movies['avg_rating'].max() <= 5

# Convert to date
user_signups['subscription_date'] = pd.to_datetime(user_signups['subscription_date']).dt.date
# Drop values using filtering
user_signups = user_signups[user_signups['subscription_date'] < today_date]
# Drop values using .drop()
user_signups.drop(user_signups[user_signups['subscription_date'] > today_date].index, inplace = True)
# Drop values using filtering
user_signups.loc[user_signups['subscription_date'] > today_date, 'subscription_date'] = today_date
# Assert is true
assert user_signups.subscription_date.max().date() <= today_date

# Column names to check for duplication
column_names = ['first_name','last_name','address']
duplicates = height_weight.duplicated(subset=column_names, keep=False)   # keep: 'first', 'last', False
# Output duplicate values
height_weight[duplicates].sort_values(by='first_name')
# Drop duplicates
height_weight.drop_duplicates(inplace=True)
# Group by column names and produce statistical summaries
column_names = ['first_name','last_name','address']
summaries = {'height': 'max', 'weight': 'mean'}
height_weight = height_weight.groupby(by=column_names).agg(summaries).reset_index()

# Dropping inconsistent categories
inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])
inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)
# Access inconsistent data
inconsistent_data = study_data[inconsistent_rows]
# Drop inconsistent categories and get consistent data only
consistent_data = study_data[~inconsistent_rows]   # use of ~ tilde

# Using cut() - create category ranges and names
ranges = [0, 200000, 500000, np.inf]
group_names = ['0-200K', '200K-500K', '500K+']
# Create income group column
demographics['income_group'] = pd.cut(demographics['household_income'], bins=ranges, labels=group_names)
demographics[['income_group', 'household_income']]
# Create mapping dictionary and replace
mapping = {'Microsoft':'DesktopOS', 'MacOS':'DesktopOS', 'Linux':'DesktopOS', 'IOS':'MobileOS', 'Android':'MobileOS'}
devices['operating_system'] = devices['operating_system'].replace(mapping)

# Replace "+" with "00"
phones["Phone number"] = phones["Phone number"].str.replace("+", "00")
# Replace "-" with nothing
phones["Phone number"] = phones["Phone number"].str.replace("-", "")
# Replace phone numbers with lower than 10 digits to NaN
digits = phones['Phone number'].str.len()
phones.loc[digits < 10, "Phone number"] = np.nan
# Find length of each row in Phone number column
sanity_check = phone['Phone number'].str.len()
# Assert minmum phone number length is 10
assert sanity_check.min() >= 10
# Assert all numbers do not have "+" or "-"
assert phone['Phone number'].str.contains("+|-").any() == False
# Replace letters with nothing using Regex
phones['Phone number'] = phones['Phone number'].str.replace(r'\D+', '')

# Converting Fahrenheit values in temperature column to Celsius
temp_fah = temperatures.loc[temperatures['Temperature'] > 40, 'Temperature']
temp_cels = (temp_fah - 32) * (5/9)
temperatures.loc[temperatures['Temperature'] > 40, 'Temperature'] = temp_cels
# Converts to datetime
birthdays['Birthday'] = pd.to_datetime(birthdays['Birthday'],
                                       # Attempt to infer format of each date
                                       infer_datetime_format=True,
                                       # Return NA for rows where conversion failed
                                       errors='coerce')
# Changing Date Format
birthdays['Birthday'] = birthdays['Birthday'].dt.strftime("%d-%m-%Y")

# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'
# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1
# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'
# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

# Cross field Validation
sum_classes = flights[['economy_class', 'business_class', 'first_class']].sum(axis = 1)   # axis=1 will sum per row,
                                                                                          # axis=0 will sum per column
passenger_equ = sum_classes == flights['total_passengers']
# Find and filter out rows with inconsistent passenger totals
inconsistent_pass = flights[~passenger_equ]
consistent_pass = flights[passenger_equ]

# Getting today date
today = dt.date.today()

# Return missing values
airquality.isna()
# Get summary of missingness
airquality.isna().sum()   # Will return sum of missing values for each column

# Missingno
import missingno as msno
import matplotlib.pyplot as plt
# Visualize missingness
msno.matrix(airquality)
plt.show()

# Isolate missing and complete values aside
missing = airquality[airquality['CO2'].isna()]
complete = airquality[~airquality['CO2'].isna()]

# Drop missing values
airquality_dropped = airquality.dropna(subset = ['CO2'])
# Replacing with statistical measures
co2_mean = airquality['CO2'].mean()
airquality_imputed = airquality.fillna({'CO2': co2_mean})

# Collapsing all of the state
from thefuzz import process

for state in categories['state']:
    # Find potential matches in states with typoes
    matches = process.extract(state, survey['state'], limit=survey.shape[0])
    # For each potential match match
    for potential_match in matches:
        # If high similarity score
        if potential_match[1] >= 80:
            # Replace typo with correct category
            survey.loc[survey['state'] == potential_match[0]] = state

# Import recordlinkage
import recordlinkage
# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()
# Block pairing on cuisine_type
indexer.block('cuisine_type')
# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)
# Create a comparison object
comp_cl = recordlinkage.Compare()
# Find exact matches on city, cuisine_types -
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')
# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold=0.8)
# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]
# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)
# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]
# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)