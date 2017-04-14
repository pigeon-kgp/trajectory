<div class="panel panel-warning">  <!-- accordion 3 -->
	
        <div class="panel-heading">
          <h4 class="panel-title"> <!-- title 3 -->
            <a data-toggle="collapse" data-parent="#accordion" href="#accordionThree">
              Feature 3 : Find Out Alternate route  
            </a>
          </h4>
        </div> 
		
        <div id="accordionThree" class="panel-collapse collapse in">
          <!-- panel body -->
          <div class="panel-body">
          	<div class="well">
				<div class="btn-group">
    					<button class="btn">Upload Input Data</button>
    					<button class="btn dropdown-toggle" data-toggle="dropdown">
        				<span class="caret"></span>
    					</button>
    					<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu" id="menu2">
       						<li><a>Data1-input.json</a></li>
    					</ul>
				</div>
				<br><br><input type="TextBox" disabled ID="f1" Class="form-control"></input><br/>
				<div class="row">
					  
						<div class="col-lg-12">
								
								<!--input type="button" value="Plot" onclick="plotTraces()" class="btn btn-primary"-->
							  <!-- <button type="button" onclick="plotTraceJSON()" class="btn btn-primary">	 -->
							  <button type="button" onclick="plotTraces_f3()" class="btn btn-primary">
								<span class="glyphicon glyphicon-map-marker"></span> &nbsp;Plot Input
							  </button>

							  <!-- <br><br> -->

							  <!--  <button type="button" onclick="clearMap()" class="btn btn-primary">
								<span class="glyphicon glyphicon-map-marker"></span> &nbsp;Clear Map
							  </button> -->

						</div>
					  </div>
				<br>
				<div class="btn-group">
    					<button class="btn">Upload Output Data</button>
    					<button class="btn dropdown-toggle" data-toggle="dropdown">
        				<span class="caret"></span>
    					</button>
    					<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu" id="menu3">
       						<li><a tabindex="-1" >Data2-output.json</a></li>
    					</ul>
				</div>
				<br><br><input type="TextBox" disabled ID="f2" Class="form-control"></input><br>
				<div class="row">
					  
						<div class="col-lg-12">
								
								<!--input type="button" value="Plot" onclick="plotTraces()" class="btn btn-primary"-->
							  <!-- <button type="button" onclick="plotTraceJSON()" class="btn btn-primary">	 -->
							  <button type="button" onclick="plotTraces_f4()" class="btn btn-primary">
								<span class="glyphicon glyphicon-map-marker"></span> &nbsp;Plot Output
							  </button>

							  <!-- <br><br> -->

							  <!--  <button type="button" onclick="clearMap()" class="btn btn-primary">
								<span class="glyphicon glyphicon-map-marker"></span> &nbsp;Clear Map
							  </button> -->

						</div>
					  </div>
			</div>
        </div>
		
     </div>
	 
 </div>