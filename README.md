# WORK IN PROGRESS

## Requirements for path planning
* Python 2
* SUMO

------------------------

* Generate `.net.xml` file from `.osm` by issuing  
`netconvert --osm-files <osm file name>.osm -o <output file name>.net.xml`

* Convert the `.net.xml` files to `.json` with randomly generated traffic by  
`cd Vis && python Vis/net_to_json.py` making sure the path to the `.net.xml` file is adjusted in the code.  
In subsequent steps, the edge id may be referred from `Vis/out.json`.

* Generate routing tables for hotspots using  
`python table_gen.py` making sure the directory has been switched to `Vis`.  
The edge ids for hotspot would be demanded from `stdin` during execution.

* Generate path by issuing  
`python path_predict.py`  
The edge ids for source and destinantion would be demanded from `stdin` during execution.  
The path would be generated in `out_path`.  

A Flask based model for the path planner is present as `~/back.py`.

-----------------------------

## Requirements for data segregation
* Python 2
* Postgres
* psycopg2

------------------------

>Details to be updated.	