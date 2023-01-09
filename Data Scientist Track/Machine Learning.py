# Exploratory Data Analysis
# Jittering

height_jitter = height + np.random.normal(0, 2, size=len(df))

# Violin Plot
data = brfss.dropna(subset=['AGE', 'WTKG3'])
sns.violinplot(x='AGE', y='WTKG3', data=data, inner=None)
plt.show()

# Box Plot
sns.boxplot(x='AGE', y='WTKG3', data=data, whis=10)
plt.yscale('log')   # Plot the y-axis on a log scale
plt.show()

# Strength of Effect / Slope of the Line
from scipy.stats import linregress
line1 = linregress(x1, y1)
line2 = linregress(x2, y2)

# Compute the line of best fit
fx = np.array([x1.min(), x1.max()])   # Getting the min and max of x-values
fy = line1.intercept + line1.slope * fx   # Substitute those values to y=mx+b
plt.plot(fx, fy, '-')

# Regression is not symmetric
# Regression does not cause causation

# Simple Regression using statsmodels
import statsmodels.formula.api as smf
results = smf.ols('INCOME2 ~ _VEGESU1', data=brfss).fit()   # ols stands for ordinary least squares
            # ols('y ~ x'                                   # (another name for regression)
results.params

# Multiple Regression using statsmodels
results = smf.ols('realinc ~ educ + age', data=gss).fit()
results.params
# Adding a quadratic term
gss['age2'] = gss['age']**2
model = smf.ols('realinc ~ educ + age + age2', data=gss)
results = model.fit()
results.params

# Visualizing Regressions
gss['age2'] = gss['age']**2
gss['educ2'] = gss['educ']**2
model = smf.ols('realinc ~ educ + educ2 + age + age2',  data=gss)
results = model.fit()
# Generating predictions
df = pd.DataFrame()
df['age'] = np.linspace(18, 85)
df['age2'] = df['age']**2
df['educ'] = 12
df['educ2'] = df['educ']**2
pred12 = results.predict(df)
# Plotting Predictions
plt.plot(df['age'], pred12, label='High school')
plt.plot(mean_income_by_age, 'o', alpha=0.5)
plt.xlabel('Age (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
# Modifying Levels of Education
df['educ'] = 14
df['educ2'] = df['educ']**2
pred14 = results.predict(df)
plt.plot(df['age'], pred14, label='Associate')

df['educ'] = 16
df['educ2'] = df['educ']**2
pred14 = results.predict(df)
plt.plot(df['age'], pred14, label='Bachelor')

# Logistic Regression (good for binary variables)
gss['gunlaw'].replace([2], [0], inplace=True)   # Replacing 2 (no) for 0 resulting to 1 (True) and 0 (False) bool
formula = 'gunlaw ~ age + age2 + educ + educ2 + C(sex)'
results = smf.logit(formula, data=gss).fit()

