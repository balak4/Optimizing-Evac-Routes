
# API Authentication Credentials
Running and improving upon the Optimizing Evacuation Routes build currently requires access to the following APIs:
-   **Gmaps and Geopy:** these can share a single [Google Maps API key](https://developers.google.com/maps/documentation/javascript/get-api-key). _When selecting the API services, check all three boxes._
-   **Twitter Search and Twitter Stream:** Follow the steps in [this guide](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html).
-   **Here.com Maps:** These can be accessed [here](https://developer.here.com/).
   
# Guidelines for Future Iterations

We have identified areas where we believe further refinement would add value to the tool:

-   Collect more tweets to continue training the model
	-   The model was only trained on a corpus made from 143 tweets, most of which came from similar news sources that only contained a geolocation
  
-   Continue to train the NLP model on new text data to improve performance
    
-   Add map functionality to visually differentiate between partially closed roads and fully blocked roads
    
-   Improve map optimization to find the optimal route between points A and B
    
-   Integrate Twitter Stream API into the mapping functionality, so that output reflects live tweet data
    
-   Build out intersection interpretation capabilities, to allow for the input of other location data formats
    
-   Improve label displays - center them on the road closure, clean up the formatting, and add interactivity via mouse click or hover-text
    
-   Experiment with additional open-source mapping applications that may allow for more customization in number of closures displayed
    
-   Implement a way to detect and visually represent larger area hazards, such as flooding or wide-spread fire, using polygons on the map
    
-   Allow mapping tool to render larger numbers of road closures