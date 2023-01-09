import matplotlib.pyplot as plt
import seaborn as sns

# Plotting scatter plot
sns.scatterplot(x="n_claims", y="total_payment_sek", data=swedish_motor_insurance)
# Plotting with regression line
sns.regplot(x="n_claims", y="total_payment_sek", data=swedish_motor_insurance, ci=None)

# ols
from statsmodels.formula.api import ols
mdl_payment_vs_claims = ols("total_payment_sek ~ n_claims", data=swedish_motor_insurance).fit()
                                                                    # dont forget to call .fit()
mdl_payment_vs_claims.params   # contains intercept and slope

# Visualizing 1 numeric and 1 categorical variable
sns.displot(data=fish, x="mass_g", col="species", col_wrap=2, bins=9)
# without the intercept
mdl_mass_vs_species = ols("mass_g ~ species + 0", data=fish).fit()

# Predicting inside a DataFrame
mdl_mass_vs_length = ols("mass_g ~ length_cm", data=bream).fit()
explanatory_data = pd.DataFrame({"length_cm": np.arange(20, 41)})
prediction_data = explanatory_data.assign(
    mass_g=mdl_mass_vs_length.predict(explanatory_data))

# .fittedvalues attribute
# Fittedvalues: predictions on the original data set
mdl_mass_vs_length.fittedvalues
# or
explanatory_data = bream["length_cm"]
mdl_mass_vs_length.predict(explanatory_data)

# .resid attribute
# .summary()
# .rsquared attribute (also called coefficient of determination)
# RSE = np.sqrt(MSE)
# MSE = RSE ** 2: .mse_resid attribute

# Making Residual Plot
sns.residplot()

# Making qqplot()
from statsmodels.api import qqplot
qqplot(data=mdl_bream.resid, fit=True, line="45")   # access .resid on the model as the data of the plot
                                                    # fit=True will compare data quantiles to a normal distribution
                                                    # line='45' will make a line at 45 degrees angle

# Making scale-location plot
model_norm_residuals_bream = mdl_bream.get_influence().resid_studentized_internal
model_norm_residuals_abs_sqrt_bream =\
    np.sqrt(np.abs(model_norm_residuals_bream))  # take the absolute values then square root
sns.regplot(x=mdl_bream.fittedvalues, y=model_norm_residuals_abs_sqrt_bream, ci=None, lowess=True)

# Extracting leverage and influence
# Create summary_info
summary_info = mdl_price_vs_dist.get_influence().summary_frame()
# Add the hat_diag column to taiwan_real_estate, name it leverage
taiwan_real_estate["leverage"] = summary_info["hat_diag"]
# Sort taiwan_real_estate by leverage in descending order and print the head
print(taiwan_real_estate.sort_values('leverage', ascending=False).head())
# Add the cooks_d column to taiwan_real_estate, name it cooks_dist
taiwan_real_estate["cooks_dist"] = summary_info["cooks_d"]
# Sort taiwan_real_estate by cooks_dist in descending order and print the head.
print(taiwan_real_estate.sort_values('cooks_dist', ascending=False).head())

# Plotting Logistic Regression
from statsmodels.formula.api import logit
mdl_churn_vs_recency_logit = logit("has_churned ~ time_since_last_purchase", data=churn).fit()

# Creating Histogram using sns seaborn
sns.displot(data=churn, x='time_since_last_purchase', col='has_churned')
# Creating regplot for Logistic Regression
sns.regplot(x="time_since_last_purchase", y="has_churned", data=churn, ci=None, logistic=True)   # set logistic=True

# Making predictions
mdl_recency = logit("has_churned ~ time_since_last_purchase", data = churn).fit()
explanatory_data = pd.DataFrame({"time_since_last_purchase": np.arange(-1, 6.25, 0.25)})
prediction_data = explanatory_data.assign(has_churned = mdl_recency.predict(explanatory_data))
# Adding point predictions
sns.regplot(x="time_since_last_purchase", y="has_churned", data=churn, ci=None, logistic=True)
sns.scatterplot(x="time_since_last_purchase", y="has_churned", data=prediction_data, color="red")

# Getting the most likely outcome
prediction_data = explanatory_data.assign(has_churned = mdl_recency.predict(explanatory_data))
prediction_data["most_likely_outcome"] = np.round(prediction_data["has_churned"])   # Rounding off data
#Visualizing most likely outcome
sns.regplot(x="time_since_last_purchase", y="has_churned", data=churn, ci=None, logistic=True)
sns.scatterplot(x="time_since_last_purchase", y="most_likely_outcome", data=prediction_data, color="red")

# Calculating Odds Ratio
prediction_data["odds_ratio"] = prediction_data["has_churned"] / (1 - prediction_data["has_churned"])
# Visualizing odds ratio
sns.lineplot(x="time_since_last_purchase", y="odds_ratio", data=prediction_data)
plt.axhline(y=1, linestyle="dotted")   # to add y=1 on the graph
# can scale y-axis to make the graph linear
plt.yscale("log")
# Calculating log odds ratio
prediction_data["log_odds_ratio"] = np.log(prediction_data["odds_ratio"])

# CALCULATING CONFUSION MATRIX
# Get the actual responses
actual_response = churn["has_churned"]
# Get the predicted responses
predicted_response = np.round(mdl_churn_vs_relationship.predict())
# Create outcomes as a DataFrame of both Series
outcomes = pd.DataFrame({"actual_response": actual_response,
                         "predicted_response": predicted_response})
# Print the outcomes
print(outcomes.value_counts(sort = False))

# DRAWING MOSAIC PLOT
# Import mosaic from statsmodels.graphics.mosaicplot
from statsmodels.graphics.mosaicplot import mosaic
# Calculate the confusion matrix conf_matrix
conf_matrix = mdl_churn_vs_relationship.pred_table()
# Print it
print(conf_matrix)
# Draw a mosaic plot of conf_matrix
mosaic(conf_matrix)
plt.show()

# MEASURING LOGISTIC MODEL PERFORMANCE
# Extract TN, TP, FN and FP from conf_matrix
TN = conf_matrix[0,0]
TP = conf_matrix[1,1]
FN = conf_matrix[1,0]
FP = conf_matrix[0,1]
# Calculate and print the accuracy
accuracy = (TN + TP) / (TN + FN + FP + TP)
print("accuracy: ", accuracy)
# Calculate and print the sensitivity
sensitivity = TP / (TP + FN)
print("sensitivity: ", sensitivity)
# Calculate and print the specificity
specificity = TN / (TN + FP)
print("specificity: ", specificity)











