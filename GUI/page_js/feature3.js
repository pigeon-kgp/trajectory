

$(function(){

    $("#menu2 li a").click(function(){

      // $(".btn:first-child").text($(this).text());
      // $(".btn:first-child").val($(this).text());
      $("#f1").val($(this).html());

   });

});

function plotTraces_f3(){
	
	// clearMap();

  var fileName = $("#f1").val();
  //alert(fileName);
  if(fileName == null){
    alert('Please upload a file !');
    exit();
  }

  array = fileName.split('.'),
  file_extension = array[1];
  if(file_extension == 'geojson') {
      plotTraceGeoJSON_f3();
  } else if(file_extension == 'json'){
      plotTraceJSON_f3();
  }


}

//to plot from json file format
function plotTraceJSON_f3(){
     // alert("plotTraceJSON_f1() called");

    var fileName = $("#f1").val();
    var URL = "files/Feature-3/"+fileName;
    //alert(URL);
   
   var color = fileloc_index_3(fileName);
	
	
	
     getInformation_feature3(URL, color);



}

var fileloc_index_3 = function(key){
	
	var file_names = ['Data1-input.json', 'Data2-output.json'];
	var color_pallete = ['green', 'red'];
	//alert(key);
	for (var i =0; i< file_names.length; i++){
		if(file_names[i]==key)
			return color_pallete[i];
	}
	
}

var getInformation_feature3 = function(filepath, color) { 
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

function clearMap3(){
	map.removeLayer(map);
	
// document.getElementById('map').innerHTML = "<div id='map' style='width: <?php echo $this->width; ?>; height: <?php echo $this->height; ?>;'></div>";

}