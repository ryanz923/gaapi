from functions import return_ga_data , save_df_to_excel


df = return_ga_data(
    start_date='7daysAgo',
    end_date='yesterday',
    view_id='4710681',
    metrics=[{'expression': 'ga:sessions'},{'expression': 'ga:pageValue'},{'expression': 'ga:transactions'}],
    dimensions=[{'name' : 'ga:pageTitle'}]
    ) 

df = df[['ga:pageTitle','ga:sessions','ga:pageValue','ga:transactions']]  

old_columns = list(df.columns)

for old in old_columns:
    df.rename(columns={old : old[3:]}, inplace = True)

print(df.sort_values('sessions',ascending = False))
