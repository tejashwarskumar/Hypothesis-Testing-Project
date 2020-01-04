import pandas as pd
import scipy 
from scipy import stats
cutlets = pd.read_csv('C:/My Files/Excelr/02 - Hypothesis Testing/Assignment/Cutlets.csv')
#Shapiro test / Normality test
stats.shapiro(cutlets["Unit A"])
stats.shapiro(cutlets["Unit B"])
#Variance test / Levene Test
scipy.stats.levene(cutlets["Unit A"],cutlets["Unit B"])
#2-sample T test
stats.ttest_ind(cutlets["Unit A"],cutlets["Unit B"],equal_var = True)
cutlets["Unit A"].mean()
cutlets["Unit B"].mean()