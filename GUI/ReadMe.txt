

Feature 1:  "Generating Bounding-Box/Segmentation region"
Input-button: Upload GPS footprints  (create dropdown menu, list - files/Feature1/I1/<file lists in JSON> ) - 
It will plot .json files 
Output-button : Create Bounding box  (take .json files from files/Feature1/O1/<file lists in JSON )
The four points of the BBOx are in the order (NW,SW,SE,NE) in 4 consecutive lines of .json. Create the rectangular bbox from these points.  There will be background color for the rect BBOX
Note - User may select multiple files in Input Button; in that case background color of those bounding boxes will be different!  

Feature 2: "Visualization of Congested paths
Input - there will be 1-5 range, 
if I choose range 1, files/Feature2/C1.json will be uploaded. If I choose range 2; both C1.json and C2.json will be uploaded, but will have diff colors. Similarly, if range 5 is chosen, then all the files with diff colors will be plotted. 

Feature 3:​ "Find Out Alternate route" 
Input :  plot .json file 
Output : plot .json file



