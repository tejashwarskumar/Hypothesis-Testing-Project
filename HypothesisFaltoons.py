import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
fantaloons = pd.read_csv("C:/My Files/Excelr/02 - Hypothesis Testing/Assignment/Faltoons.csv")

table1=fantaloons.Weekdays.value_counts()
table1
table2=fantaloons.Weekend.value_counts()
table2
count=np.array([113,167])
nop = np.array([280,520])
count2 = np.array([287,233])
nop2 = np.array([520,280])

proportions_ztest(count,nop,alternative="two-sided")
#2-Proportion Test 
proportions_ztest(count2,nop2,alternative="two-sided")

d = np.sqrt(20)/np.sqrt(10)
-3/d
