def get_outliers(data):
    quartiles = data['value'].quantile([0.25,0.75])

    iqr = quartiles.iloc[1] - quartiles.iloc[0]

    upper = quartiles.iloc[1]  + 1.5*iqr

    lower = quartiles.iloc[0] - 1.5*iqr

    outliers = data[(data['value']<lower) | (data['value']>upper)]
    
    filtered_data = data[(data['value'] > lower) & (data['value'] < upper)]
    
    return outliers,filtered_data