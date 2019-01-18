# Data Dictionaries
 
## Tweets Data 

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**tweed_id**|*int*|df|The unique identifier for the Tweet.|
|**rating**|*int*|df|Relevance rating of Tweet text. 0 = Not Relevant, 1 = Relevant, partial road block, 2 = Relevant, full road closure.|
|**tweet**|*object*|df|The actual UTF-8 text of the status update.|

  
## HERE.Maps Data 

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**city**|*object*|df| City of origin of the data point.|
|**source**|*object*|df| Data source.|
|**criticality**|*object*|df|Severity of the incident. Range, from most severe to least severe = Critical, Major, Minor, lowImpact.|
|**intersection**|*object*|df|Location of the reported incident.|
|**start_lat_long**|*tuple of floats*|df|Starting coordinates of the reported incident.|
|**end_lat_long**|*tuple of floats*|df|Ending coordinates of the reported incident.|
|**start_time**|*datetime object*|df|Starting time of the reported incident.|
|**end_time**|*datetime object*|df|Ending time of the reported incident.|
|**entry_time**|*datetime object*|df|Timestamp of when the incident was received int he HERE.Maps database.|
|**bbox_top_left**|*tuple of floats*|df|Bounding box coordinates for the area of the reported incident.|
|**bbox_top_right**|*tuple of floats*|df|Bounding box coordinates for the area of the reported incident.|
|**date_requested**|*datetime object*|df|Date of API query.|


## Google Maps Data 

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**start**|*tuple of floats*|df|Coordinates of closure start points in latitude, longitude format. Formats switched between tuple and list over the course of the project, but the final input into the render_closure functions will be tuples.|
|**end**|*tuple of floats*|df|Coordinates of closure end points in latitude, longitude format. Formats switched between tuple and list over the course of the project, but the final input into the `render_closure` functions will be tuples.|
|**text**|*object*|df|Text decription of the reason for road closure, to be applied as a label on the map output by `render_closures`.|