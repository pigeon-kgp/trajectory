<?php
//	$pyscript = 'python map_matching/map_matcher.py "host=10.14.90.158 port=5432 dbname=road_network user=postgres password=postgres " ROAD_TABLE_NAME < 366_short.txt';
//	echo exec($pyscript);
	$txt_file    = fopen('map_matching/output.txt','r');
	echo $txt_file;
	$output_file    = fopen('map_matching/output_plot.txt','w');
	while (!feof($txt_file)) {
		$line_of_text = fgets($txt_file);
		if (trim($line_of_text) == '') {
			continue;
		}
		$parts = explode(':', $line_of_text);
		if(strcmp(trim($parts[0]), "Matche d coordinate") == 0) {
			$data = $parts[1];
			fwrite($output_file, trim($data));
			fwrite($output_file, "\n");
		}
	}
	fclose($txt_file);
	fclose($output_file);
	$text = fopen( "map_matching/output_plot.txt", "r" );
	$csv = fopen( "map_matching/sample.csv", "w" );
	while(($line = fgets($text)))
	{
		fputcsv($csv, explode(" ", $line));
    	echo $line;
	}
	$pyscript = 'python map_matching/csvToGeoJSON.py';
	echo exec($pyscript);
?>