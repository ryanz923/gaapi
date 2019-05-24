from functions import return_ga_data , save_df_to_excel
### Returns sessions and tranactions by channel for a specific Analytics View Id

# be sure to add correct view ID
df = return_ga_data(
    start_date='7daysAgo',
    end_date='yesterday',
    view_id='ADD VIEW ID',
    metrics=[{'expression': 'ga:sessions'},{'expression': 'ga:transactions'}],
    dimensions=[{'name' : 'ga:channelGrouping'}]
    ) 

# generate dataframe
df = df[['ga:channelGrouping','ga:sessions','ga:pageValue','ga:transactions']]  

#cleans up column names
old_columns = list(df.columns)

for old in old_columns:
    df.rename(columns={old : old[3:]}, inplace = True)

    
# print out dataframe
print(df.sort_values('sessions',ascending = False))
