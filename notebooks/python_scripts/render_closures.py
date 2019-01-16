def render_closures(data):
    import gmaps
    # layout options: draw a comfortable-sized map
    figure_layout = {
    'width': '700px',
    'height': '400px',
    'padding': '1px',
    'margin': '0 auto 0 auto'
    }
    # initialize map
    fig = gmaps.figure(layout=figure_layout)

    # draw road closures
    for index,point in data.iterrows():
        # The parameters are mostly self-explanatory, but I will note that this uses
        # walking directions in case start and end points are contrary to one-way streets
        close = gmaps.directions_layer(start=data.iloc[index][0],end=data.iloc[index][1],
                                       travel_mode='WALKING',show_markers=False,
                                      stroke_color='Red', stroke_opacity=0.8)
        fig.add_layer(close)

    # establish labeled markers
    marker_layer = gmaps.marker_layer(locations=data['start'],
                                  label=data['text'])
    # and add them to the map
    fig.add_layer(marker_layer)
    return fig
