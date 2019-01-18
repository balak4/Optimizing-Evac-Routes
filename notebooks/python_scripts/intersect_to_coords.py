def intersect_to_coords(data,exdata=None):
    import pandas as pd
    import geopy
    from python_scripts import config

    # instantiate a google maps geocoder
    geolocator = geopy.geocoders.GoogleV3(api_key=config.gmaps_key)
    # build lists to put into our new DataFrame
    starts = []
    ends = []
    texts = []

    # iterate over rows
    for index,point in data.iterrows():
        # geocode the start and end points
        new_start = geolocator.geocode(data.start[index] +',' + data.city[index])
        new_end = geolocator.geocode(data.end[index] +',' + data.city[index])
        # put their latitudes and longitudes into our lists
        starts.append([new_start.latitude,new_start.longitude])
        ends.append([new_end.latitude,new_end.longitude])
        texts.append(data.text[index])

    # convert sublists to tuples so all my functions play nice
    starts = [tuple(_) for _ in starts]
    ends = [tuple(_) for _ in ends]
    
    # put all that together!
    new_dict = {'start':starts,'end':ends,'text':texts}
    new_df = pd.DataFrame(new_dict)

    if exdata is not None:
        new_df = pd.concat([new_df,exdata],ignore_index=True)
        tuple(new_df['start'])
        tuple(new_df['end'])
    return new_df
