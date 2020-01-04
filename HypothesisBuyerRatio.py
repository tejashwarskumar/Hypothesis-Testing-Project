import pandas as pd 
from scipy import stats
BuyerRatio = pd.read_csv("C:/My Files/Excelr/02 - Hypothesis Testing/Assignment/BuyerRatio.csv")

#Shapiro test/ Noramlity Test
stats.shapiro(BuyerRatio.Males)
stats.shapiro(BuyerRatio.Females)
#Variance test/ Levene Test
stats.levene(BuyerRatio.Males,BuyerRatio.Females)

#2 sample T test
stats.ttest_ind(BuyerRatio.Males,BuyerRatio.Females,equal_var = False)