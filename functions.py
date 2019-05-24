import connect
import pandas as pd
import xlsxwriter

VIEW_ID = 'ADD VIEW ID HERE'

def convert_reponse_to_df(response):
    list = []
    # get report data
    for report in response.get('reports', []):
        # set column headers
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get(
            'metricHeader', {}).get(
            'metricHeaderEntries', [])
        rows = report.get('data', {}).get('rows', [])

        for row in rows:
            # create dict for each row
            dict = {}
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            # fill dict with dimension header (key) and dimension value (value)
            for header, dimension in zip(dimensionHeaders, dimensions):
                dict[header] = dimension

            # fill dict with metric header (key) and metric value (value)
            for metric, values in enumerate(dateRangeValues):
                for metric, value in zip(metricHeaders, values.get('values')):
                    # set int as int, float a float
                    if ',' in value or '.' in value:
                        dict[metric.get('name')] = float(value)
                    else:
                        dict[metric.get('name')] = int(value)

            list.append(dict)

        df = pd.DataFrame(list)
        return df


def get_report(analytics, start_date, end_date, view_id, metrics, dimensions):
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
                    'metrics': metrics,
                    'dimensions': dimensions
                }]
        }
    ).execute()


def return_ga_data(start_date, end_date, view_id, metrics, dimensions):
    return convert_reponse_to_df(
        get_report(
            connect.service,
            start_date,
            end_date,
            view_id,
            metrics,
            dimensions))

# def save_df_to_excel(df, path, file_name, sheet_name):
#     writer = pd.ExcelWriter(path+file_name+'.xlsx', engine = 'xlsxwriter')
#     df.to_excel(writer, sheet_name = sheet_name)
#     writer.save()

def clean_columns(df):
    old_columns = list(df.columns)

    for old in old_columns:
        df.rename(columns={old: old[3:]}, inplace=True)

def save_df_to_excel(df, file_name):
    df.to_csv(file_name)
