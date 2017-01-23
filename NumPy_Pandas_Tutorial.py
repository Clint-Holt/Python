import pandas as pd
import numpy as np

enrollments_file = 'C:\Users\clint\Downloads\enrollments.csv'
daily_engagements_file = 'C:\Users\clint\Downloads\daily_engagement_full.csv'
project_submissions_file = 'C:\Users\clint\Downloads\project_submissions.csv'


daily_engagement = pd.read_csv(daily_engagements_file)

print len(daily_engagement['acct'].unique())