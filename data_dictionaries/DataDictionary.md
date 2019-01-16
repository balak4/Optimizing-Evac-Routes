
## Tweets Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|**coordinates**|*float*|df|Represents the geographic location of the Tweet as reported by the user or client application. The inner coordinates array is formatted as geoJSON (longitude first, then latitude).|
|**created_at**|*object*|df|UTC time when this Tweet was created.|
|**full_text**|*object*|df|The actual UTF-8 text of the status update.|
|**id**|*int*|df|The integer representation of the unique identifier for the Tweet. .|
|**place**|*object*|df|Places are specific, named locations with corresponding geo coordinates. When users decide to assign a location to their Tweet, they are presented with a list of candidate Twitter Places. Tweets associated with Places are not necessarily issued from that location but could also potentially be about that location.|
|**place.bounding_box.coordinates**|*Array of Array of Array of Float*|df|A series of longitude and latitude points, defining a box which will contain the Place entity this bounding box is related to. Each point is an array in the form of [longitude, latitude]. Points are grouped into an array per bounding box.|
|**user**|*object*|df|The User object contains public Twitter account metadata and describes the user of the Tweet.|
