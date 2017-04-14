

$(function(){

    $("#menu1 li a").click(function(){

      // $(".btn:first-child").text($(this).text());
      // $(".btn:first-child").val($(this).text());
      $('#filename').val($(this).html());

   });

});


function boundingBox(){
	// alert("bbox");
	var e = $("#filename").val();

	if(e == ""){
    alert('Please select a file !');
    exit();
  }
	var path1 = "files/Feature-1/O1/"+e;
	alert(path1);
	
	var color = fileloc_index(e);

  var lat_array = [];
  var lng_array = [];
  var bounds = [];

	var getInformation = function() { 
	var path = path1;
	var informationArray= [];
	$.ajax({
	         url: path,
	         async: false,
	         dataType: 'text',
	         success: function(response) {
	         	// alert(response);

            response = response.replace('markers=[', '');
            response = response.replace(']', '');
            response = response.substring(0,response.lastIndexOf(','));
            response +='';
            // alert(response);
            var json_obj = $.parseJSON('[' + response + ']');
            // alert(JSON.stringify(response));
            // alert(json_obj.length);
            for (var i = 0; i < json_obj.length; i++) { 
                // alert(json_obj[i].lat);
                if(i%2!=0){ // for SW , NE
                  lat_array[i] = json_obj[i].lat;
                  lng_array[i] = json_obj[i].lng;
                } else {  //for NW, SE
                  lat_array[i] = json_obj[i].lat;
                  lng_array[i] = json_obj[i].lng;
                }           
              }

	         $.each(json_obj.items,
	         function(item) {
	         	// alert("2");
	         informationArray.push(item);
	         });
	         informationArray.push("success");
	         }
	         }); 
          bounds = [[lat_array[1], lng_array[1]], [lat_array[3], lng_array[3]]];
	   return bounds; 


   }

	   var bounds = getInformation();

	// var bounds = [[lat_array[1], lng_array[1]], [lat_array[3], lng_array[3]]];

	// create an orange rectangle
	var boundingBox = L.rectangle(bounds, {color: color, opacity: 0.4, weight: 1});
	map.addLayer(boundingBox);

}



function plotTraces_f1(){
	
	// clearMap();

  var fileName = $("#filename").val();
  //alert(fileName);
  if(fileName == null){
    alert('Please upload a file !');
    exit();
  }

  array = fileName.split('.'),
  file_extension = array[1];
  if(file_extension == 'geojson') {
      plotTraceGeoJSON_f1();
  } else if(file_extension == 'json'){
      plotTraceJSON_f1();
  }


}

//to plot from json file format
function plotTraceJSON_f1(){
     // alert("plotTraceJSON_f1() called");

    var fileName = $("#filename").val();
    var URL = "files/Feature-1/I1/"+fileName;
    // alert(URL);
   
   var color = fileloc_index(fileName);
	
	
	
     getInformation_feature1(URL, color);



}

var fileloc_index = function(key){
	
	var file_names = ['03-877.json', '03-5964.json','09-7949.json' ,'011-5619.json' ,'011-7082.json'];
	var color_pallete = ['green', 'red', 'blue', 'yellow', 'black'];
	//alert(key);
	for (var i =0; i< file_names.length; i++){
		if(file_names[i]==key)
			return color_pallete[i];
	}
	
}

var getInformation_feature1 = function(filepath, color) { 
  var path = filepath;
  var informationArray= [];
  $.ajax({
           url: path,
           async: false,
           dataType: 'text',
           success: function(response) {
            // alert(response);

            response = response.replace('markers=[', '');
            response = response.replace(']', '');
            response = response.substring(0,response.lastIndexOf(','));
            response +='';
            // alert(response);
            var json_obj = $.parseJSON('[' + response + ']');
            // alert(JSON.stringify(response));
            //alert(json_obj.length);
            
                for ( var i=0; i < json_obj.length-1; ++i ) 
                {
                   // L.marker( [json_obj[i].lat, json_obj[i].lng] )
                   //    .bindPopup( '<a href="' + json_obj[i].url + '" target="_blank">' + json_obj[i].name + '</a>' )
                   //    .addTo( map );


                      var pointA = new L.LatLng(json_obj[i].lat , json_obj[i].lng);
                      // alert(pointA);
                      var pointB = new L.LatLng(json_obj[i+1].lat , json_obj[i+1].lng);
                      // alert(pointB);
                      var pointList = [pointA,pointB];
                      var firstpolyline = new L.Polyline(pointList, {
                        color: color,
                        weight: 3,
                        opacity: 0.5,
                        smoothFactor: 1
                      });
                      firstpolyline.addTo(map);
                      

                }        
              

           $.each(json_obj.items,
           function(item) {
            // alert("2");
           informationArray.push(item);
           });
           informationArray.push("success");
           }
           }); 
     return informationArray; 


   }

//to plot from geojson file format
function plotTraceGeoJSON_f1(){

    // alert("plotTraceGeoJSON() called");
    //alert(global_uploadFileName.name);
    var polylines = new L.geoJson();
    polylines.addTo(map);

    var fileName = $("#filename").val();
    var URL = "files/Feature-1/i1/"+fileName;

    $.ajax({
    dataType: "json",
    url: URL,
    success: function(data) {
        $(data.features).each(function(key, data) {
            polylines.addData(data);
        });
    }
    }).error(function() {});

}


function clearMap(){
	map.removeLayer(map);
	
// document.getElementById('map').innerHTML = "<div id='map' style='width: <?php echo $this->width; ?>; height: <?php echo $this->height; ?>;'></div>";

}