def intersect_to_coords(data):
    import pandas as pd
    import geopy
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
        starts.append((new_start.latitude,new_start.longitude))
        ends.append((new_end.latitude,new_end.longitude))
        texts.append(data.text[index])

    # put all that together!
    new_dict = {'start':starts,'end':ends,'text':texts}
    new_df = pd.DataFrame(new_fake)
    return new_df
