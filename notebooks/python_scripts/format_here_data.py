def format_here_data(data):
    # import necessary modules
    import pandas as pd
    from ast import literal_eval

    # establish the features from data that we'll keep
    features = ['start_lat_long','end_lat_long']
    # establihs the dataframe
    df = pd.DataFrame(columns=['start','end','text'])
    # read in the coordinates, evaluating columns because read_csv reads lists and tuples
    # as strings
    df['start'] = [literal_eval(data['start_lat_long'][i]) for i in range(len(data))]
    df['end'] = [literal_eval(data['end_lat_long'][i]) for i in range(len(data))]
    df['text'] = None

    return df
