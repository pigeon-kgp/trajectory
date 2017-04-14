<!DOCTYPE HTML>
<html lang="en-US" xmlns="http://www.w3.org/1999/xhtml">
   <head profile="http://gmpg.org/xfn/11">
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

      <link rel="stylesheet" type="text/css" href="css/leaflet.css" />
	     <!-- Bootstrap -->
      <link href = "css/bootstrap.min.css" rel = "stylesheet">
      
        
      <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
      <!--<script src = "https://code.jquery.com/jquery.js"></script> -->
      <script src = "js/jquery.js"></script>
	  <script src = "js/bootstrap.min.js"></script>
	  
      
      <script type='text/javascript' src='js/jquery.min.js'></script>
      <script type='text/javascript' src='js/leaflet.js'></script>
	  <script type='text/javascript' src='js/leaflet.geojsoncss.min.js'></script>
	  <!--
	  <script type='text/javascript' src='js/leaflet.ajax.min.js'></script>
	  
	  <link rel="stylesheet" href="http://yandex.st/bootstrap/3.0.3/css/bootstrap.min.css">
	<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />
	<script src="http://yandex.st/jquery/2.0.3/jquery.min.js"></script>
	<script src="http://yandex.st/bootstrap/3.0.3/js/bootstrap.min.js"></script>
	<script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet-src.js"></script>
	<script src="../leaflet.geojsoncss.js"></script>
	-->
	
   </head>

   <body>
   <div class="container">
	  <div class="jumbotron">
		<h1>MacTrackz</h1> 	
	  </div>	  
		<div class="row">
		  <div class="col-lg-4" align="center">
				<strong><h3>Upload File (.geojson / .json)</h3></strong>

<div class="panel-group" id="accordion"> <!-- accordion 1 -->
   <div class="panel panel-primary">
   
        <div class="panel-heading"> <!-- panel-heading -->
            <h4 class="panel-title"> <!-- title 1 -->
            <a data-toggle="collapse" data-parent="#accordion" href="#accordionOne">
              Feature 1 : Generating Bounding-Box/Segmentation region
            </a>
           </h4>
        </div>
		<!-- panel body -->
        <div id="accordionOne" class="panel-collapse collapse in">
          <div class="panel-body">
                    

 <div class="btn-group">
    <button class="btn">Upload GPS Footprints</button>
    <button class="btn dropdown-toggle" data-toggle="dropdown">
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu" id="menu1">
       <li><a tabindex="-1" href="#">03-877.json</a></li>
       <li><a tabindex="-1" href="#">03-5964.json</a></li>
       <li><a tabindex="-1" href="#">09-7949.json</a></li>
       <!-- <li class="divider"></li> -->
       <li><a tabindex="-1" href="#">011-5619.json</a></li>
       <li><a tabindex="-1" href="#">011-7082.json</a></li>
    </ul>
</div>

<br/><br/><input type="TextBox" disabled ID="filename" Class="form-control"></input><br/>


<div class="row">
					  
						<div class="col-lg-12">
								
								<!--input type="button" value="Plot" onclick="plotTraces()" class="btn btn-primary"-->
							  <!-- <button type="button" onclick="plotTraceJSON()" class="btn btn-primary">	 -->
							  <button type="button" onclick="plotTraces_f1()" class="btn btn-primary">
								<span class="glyphicon glyphicon-map-marker"></span> &nbsp;Plot Input
							  </button>

							  <!-- <br><br> -->

							  <!--  <button type="button" onclick="clearMap()" class="btn btn-primary">
								<span class="glyphicon glyphicon-map-marker"></span> &nbsp;Clear Map
							  </button> -->

						</div>
					  </div>

<br>
<button type="button" onclick="boundingBox()" class="btn btn-primary">
								<span class="glyphicon glyphicon-map-marker"></span> &nbsp;Output
							  </button>
          </div>
        </div>
  </div>
  
   <div class="panel panel-success">  <!-- accordion 2 -->
	  
          <div class="panel-heading"> 
          <h4 class="panel-title"> <!-- title 2 -->
            <a data-toggle="collapse" data-parent="#accordion" href="#accordionTwo">
              Feature 2 : Visualization of Congested Paths

            </a>
          </h4>
          </div>
		 <!-- panel body -->
        <div id="accordionTwo" class="panel-collapse collapse in">
          <div class="panel-body">



		  Select Range : 
          	<div class="btn-group btn-group-lg" data-toggle="buttons">
			    <label class="btn btn-primary"  >
			        <input type="radio" name="q12_3" value="1"> 1
			    </label>
			    <label class="btn btn-primary" >
			        <input type="radio" name="q12_3" value="2"> 2
			    </label>
			    <label class="btn btn-primary"  >
			        <input type="radio" name="q12_3" value="3"> 3
			    </label>
			    <label class="btn btn-primary"  >
			        <input type="radio" name="q12_3" value="4"> 4
			    </label>
			    <label class="btn btn-primary"  >
			        <input type="radio" name="q12_3" value="5"> 5
			    </label>
				
			</div>
			
			<br><br>
				<button type="button" class="btn btn-primary" id="submit">Submit</button>

			<br><br>
			<input type="TextBox" disabled ID="radio_filename" Class="form-control"></input><br/>
 

          </div>
        </div>
		
   </div>
   
    <?php /*include 'feature3.php';*/?>


</div>
		  </div>
		  <div class="col-lg-8">
					
				<div id="map" style="height: 440px; border: 1px solid #AAA;"></div>
	  
		  </div>
		</div>
	  
	  
   </div>
	   
	  	  
      <script type='text/javascript' src='files/markers.json'></script>
      <script type='text/javascript' src='js/file_uploader.js'></script>
      <script type='text/javascript' src='js/create_output.js'></script>
	  <script type='text/javascript' src='page_js/parseGeoJSON.js'></script>
	  <script type='text/javascript' src='page_js/feature1.js'></script>
	  <script type='text/javascript' src='page_js/feature2.js'></script>
	  <script type='text/javascript' src='page_js/feature3.js'></script>
	  <script type='text/javascript' src='page_js/feature4.js'></script>
   </body>
</html>
   