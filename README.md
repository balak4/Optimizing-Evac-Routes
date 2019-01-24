# Optimizing Evacuation Routes: Identifying Blocked Roads in Real Time

_By Brian Brakefield, Veronica Giannotta, Bala Krishnamoorthy, and Amy Taylor_

During emergency situations, every second matters. Search and rescue teams must be able to locate and get to survivors as quickly as possible. The latest GIS and navigation systems allow responders to calculate travel time and distance between origin and destination, and propose an optimal route to the destination. However, few current platforms rely on real-time data to identify blocked routes, damaged roads, etc., leading to potentially longer response times during and immediately following disastrous events.

To that end, we have built a tool that utilizes machine learning techniques and social media / location data to identify and visualize road closures in real time. The tool takes in live Twitter posts and Here.com data, filters out the data that relate specifically to road closures in a given city, and dynamically populates the closures on a Google Map. This information can be leveraged by users to find the shortest, fastest routes to their destination by displaying current road closures in real time.

This Deliverable Includes:

-   The mapping tool
-   A set of Jupyter notebooks and executable scripts that output road closures on a Google Map
-   Training and testing datasets of collected web data
-   Guidance on future generations of the mapping tool

And here's the final output of the map:

 ![Alt text](https://github.com/balak4/Optimizing-Evac-Routes/blob/master/data/3-final/Sample_map_output_image.png)   

## Methodology

**Data Collection** |  _Sources: Here.com & Twitter_
- **HERE.com** is a tech company that specializes in mapping and location services. The data were collected through filters that searched on geographic area and incident type.
- **The Twitter API** offers developers a multitude of ways to engage with the platform. We utilized the Stream and Search functions of the API, in order to collect tweets and a variety of accompanying data points.
	-   Search API - for “Historical” Tweets: allows for selective searching of tweets made up to one week in the past. We queried this history data using keywords and location tags to pull tweets that could be used to train a classification model.
	-   Stream API: allows for the streaming of live tweets. This version of the mapping tool does not integrate the live feed functionality. However, we included executable code and instructions for querying the Stream API in future versions.
    
**Classification Modeling to Determine Relevant Tweets**
We analyzed the text data within each tweet, with the goal of identifying an “ideal” set of tweets. Criteria for “ideal” includes report of a road closure, and specific text references to street intersections where the road was closed. Each tweet in the sample set was labeled as 0, 1, or 2 with 2 being an “ideal” relevant tweet. The labeled tweets dataset was then used to train a classification model to recognize tweets that would be sufficiently descriptive of road closures:

  

-   **0 - Not Relevant** (or uninformative)
    _ex.: “MVHS will remain closed tomorrow due to concerns about road conditions.“_


-   **1 - Relevant, Partial Road Closure Only**
    _ex.: “Road construction. right lanes closed in #Pima on I-10 EB at Ruthrauff Rd”_

-   **2 - Relevant, Full Closure with Complete Location Info**
    _ex.:  “Manchester road off Wayne avenue is closed off by police. Giving traffic delivery updated as I see them”_

**Location Extraction from Tweets**
Relevant tweets can be parsed to yield specific geographic keywords.

**Mapping**
Location data from Twitter and here.com are formatted and mapped using Google Maps API.

Location data processed from Twitter posts is translated from strings that reference street intersections into latitude and longitude coordinates via the Geopy package.

This data can be rendered to an embedded Google Maps display including, if present, label text for the road closures. Closures are rendered using Google Maps Directions API and thus automatically follow road contours, but limit the maximum number of closures that can be mapped at once.

The output is an interactive Google Maps object with closures drawn onto relevant sections of road. Where available, a framework is in place to display simple labels to describe the road closures. Users can interact with the Maps object via mouse to zoom in and out and to scroll the view of the map.

## Future Iterations
While the mapping tool is, in its current state, a working, end-to-end solution, we hope that it lays the framework for future versions that can elaborate on its base functionality. A complete list of guidelines for future iterations of this tool can be found [HERE](https://docs.google.com/document/d/1bDanbwegLJHpVv45dwmxIbQlV2FokHKHYS0JOE4anNs/edit?usp=sharing). _Also included are links for future developers to quickly find where to get required API credentials._


## Sources
-   Documentation:
	-   [Twitter Developer](https://developer.twitter.com/en/docs.html) 
	-   [Tweepy API](http://docs.tweepy.org/en/v3.5.0/index.html) 
	-   [HERE Developer](https://developer.here.com/)
	- [Jupyter Gmaps](https://jupyter-gmaps.readthedocs.io/en/latest/)
	-   [GeoPy](https://geopy.readthedocs.io/en/stable/) _(also referenced within the Jupyter Gmaps examples)_


-   Articles:
	-   [http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/](http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/)
	-   [https://www.youtube.com/watch?v=wlnx-7cm4Gg](https://www.youtube.com/watch?v=wlnx-7cm4Gg)
    

-   GitHub Repos:
	-   [https://github.com/Celis1/Project-5](https://github.com/Celis1/Project-5) _(project repo, previous DSI cohort)_

## Team

Brian Brakefield | [https://linkedin.com/in/brianbrakefield/](https://linkedin.com/in/brianbrakefield/)

Veronica Giannotta | [https://www.linkedin.com/in/vgiannotta/](https://www.linkedin.com/in/vgiannotta/)

Bala Krishnamoorthy | [https://www.linkedin.com/in/balakrishnamoorthy/](https://www.linkedin.com/in/balakrishnamoorthy/)

Amy Taylor | [https://www.linkedin.com/in/amy-taylor-24999574/](https://www.linkedin.com/in/amy-taylor-24999574/)
