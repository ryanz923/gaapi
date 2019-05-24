import pandas as pd
import matplotlib.pyplot as plt
from functions import return_ga_data, save_df_to_excel, clean_columns, VIEW_ID

# Get data from Analytics
df = return_ga_data(
    start_date='30daysAgo',
    end_date='yesterday',
    view_id=VIEW_ID,
    metrics=[{'expression': 'ga:sessionsPerUser'}],
    dimensions=[{'name': 'ga:channelGrouping'}]
)

# Creat pandas dataframe
df = df[['ga:channelGrouping', 'ga:sessionsPerUser']]

# rename columns
clean_columns(df)

# Save to csv
save_df_to_excel(df, 'spu.csv')

# Display chart
df.head(10).sort_values(
    'sessionsPerUser',
    ascending=False).plot(
        kind='bar',
        x='channelGrouping',
    y='sessionsPerUser')
plt.show()

