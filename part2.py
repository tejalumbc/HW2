import pandas as pd
from pandas_profiling import ProfileReport

# Load the dataset
df = pd.read_csv('red_wine.csv')

# Generate the profile report
profile = ProfileReport(df, title='Red Wine Quality Profiling Report', explorative=True)

# Save to HTML file
profile.to_file('red_wine_report.html')