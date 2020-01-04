import pandas as pd
from scipy import stats
telecall = pd.read_csv("C:/My Files/Excelr/02 - Hypothesis Testing/Assignment/Costomer+OrderForm.csv")

count=pd.crosstab(telecall["Phillippines"],telecall["Indonesia"])
count

Chisquares_results = stats.chi2_contingency(count)
Chisquares_results[1]

count2 =pd.crosstab(telecall["Phillippines"],telecall["Malta"])
count2
Chisquares_results_2 = stats.chi2_contingency(count2)
Chisquares_results_2[1]

count3 =pd.crosstab(telecall["Phillippines"],telecall["India"])
count3
Chisquares_results_3 = stats.chi2_contingency(count3)
Chisquares_results_3[1]

count4 =pd.crosstab(telecall["Indonesia"],telecall["Malta"])
count4
Chisquares_results_4 = stats.chi2_contingency(count4)
Chisquares_results_4[1]

count5 =pd.crosstab(telecall["Indonesia"],telecall["India"])
count5
Chisquares_results_5 = stats.chi2_contingency(count5)
Chisquares_results_5[1]

count6 =pd.crosstab(telecall["Malta"],telecall["India"])
count6
Chisquares_results_6 = stats.chi2_contingency(count6)
Chisquares_results_6[1]
