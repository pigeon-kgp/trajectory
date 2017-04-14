function writeToFile(){
	$.ajax({
		type: 'POST',
		url: 'output_text.php',
		success: function(data) {
			// alert("Output File Created");
			alert(data);
		}
	});
}