def render_closures(data):
    # import modules for the python script:
    import pandas as pd
    import gmaps
    import time

    # layout options: draw a comfortable-sized map
    figure_layout = {
    'width': '700px',
    'height': '400px',
    'padding': '1px',
    'margin': '0 auto 0 auto'
    }
    # initialize map
    fig = gmaps.figure(layout=figure_layout)

    # establish list for map markers
    marker_coords = []
    marker_labels = []

    # draw road closures
    for index,_ in data.iterrows():
        # The parameters are mostly self-explanatory, but I will note that this uses
        # walking directions in case start and end points are contrary to one-way streets
        close = gmaps.directions_layer(start=data.iloc[index][0],end=data.iloc[index][1],
                                       travel_mode='DRIVING',show_markers=False,
                                      stroke_color='Red', stroke_opacity=0.8)
        # add this closure's layer
        fig.add_layer(close)
        # check for label text:
        if data.iloc[index][2] is not None:
            # append label info (I'm not really happy with how these end up looking, but
            # we're on a time crunch. Function over form, I say!)
            marker_coords.append(data.iloc[index][0])
            marker_labels.append(data.iloc[index][2])

        # Google Maps API limits to 50 requests per second
        time.sleep(0.3)

    # if marker_labels isn't empty
    if marker_labels != []:
        # establish labeled markers
        marker_layer = gmaps.marker_layer(locations=marker_coords,
                                  label=marker_labels)
        # and add them to the map
        fig.add_layer(marker_layer)
    return fig
