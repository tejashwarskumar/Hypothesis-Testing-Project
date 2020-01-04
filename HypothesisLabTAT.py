import pandas as pd
import scipy 
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

tatData = pd.read_csv("C:/My Files/Excelr/02 - Hypothesis Testing/Assignment/LabTAT.csv")
tatData.columns="Laboratory1","Laboratory2","Laboratory3","Laboratory4"

#Shapiro test/ Normality Test
stats.shapiro(tatData["Laboratory1"])
stats.shapiro(tatData["Laboratory2"])
stats.shapiro(tatData["Laboratory3"])
stats.shapiro(tatData["Laboratory4"])

#Variance test/ Levene Test
scipy.stats.levene(tatData["Laboratory1"],tatData["Laboratory2"])
scipy.stats.levene(tatData["Laboratory2"],tatData["Laboratory3"])
scipy.stats.levene(tatData["Laboratory3"],tatData["Laboratory4"])
scipy.stats.levene(tatData["Laboratory4"],tatData["Laboratory1"])
scipy.stats.levene(tatData["Laboratory2"],tatData["Laboratory4"])
scipy.stats.levene(tatData["Laboratory4"],tatData["Laboratory3"])

#ANOVA Test
mod=ols('Laboratory1~Laboratory2+Laboratory3+Laboratory4',data=tatData).fit()
aov_table=sm.stats.anova_lm(mod,type=2)
print(aov_table)