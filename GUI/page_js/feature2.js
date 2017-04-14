 
 $(function(){
    $("#submit").click(function(){      
        var range = $('input[name=q12_3]:checked').val();
		var txt = document.getElementById('radio_filename');
		//alert(range);
		if(range != ""){
				txt.value = "Range : "+range;
		} else {
			alert("Select Range");
		}
		var color_pallete = ['green', 'red', 'blue', 'yellow', 'black'];
		for(var i=1; i<=range; i++) {			
			//alert("Range : "+range +" plotted successfully !");
			var fileName = "C"+i+".json";
			//var fileName = "C2.json";
			var URL = "files/Feature-2/"+fileName;
			range_plot(URL, color_pallete[i-1]);			
			
		}		
    });
 });

 
 
 var range_plot = function(filepath, plot_color) { 
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
                      var pointA = new L.LatLng(json_obj[i].lat , json_obj[i].lng);
                      // alert(pointA);
                      var pointB = new L.LatLng(json_obj[i+1].lat , json_obj[i+1].lng);
                      // alert(pointB);
                      var pointList = [pointA,pointB];
                      var firstpolyline = new L.Polyline(pointList, {
                        color: plot_color,
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

