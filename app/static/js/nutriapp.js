$(document).ready(function(){

	// Create global variables needed repeatedly
	var globals = {
		baseUrl: "http://10.0.0.7:8080"
	}

	// Hide read-profile-content
	panelContainer = $("#panelcontainer");
	panelContainer.hide();		

	// Handler for read event
	$("#readprofbtn").click(function(){
		var fid = $("#readprofinput").val();
		// alert(fid)
		url = globals.baseUrl + "/profile/" + fid.toString();
		$.getJSON(url, function (data) {
			newHtml = "<h4> Food item =" 
					  + data["food_data"]["display_name"]
					  + "</h4>"	
					  + "<p> Portion size: "
					  + data["food_data"]["portion_amt"]
					  +"</p>"
					  + "<p> Calories: "
					  + data["food_data"]["calories"]
					  +"</p>"
					  + "<p> Added Sugars: "
					  + data["food_data"]["added_sugars"]
					  +"</p>"		
			// alert(newHtml);
			panelContent = $("#panelcontent");
			// alert(panelContent.text());
			panelContent.html(newHtml);
			panelContainer.show();
		});		
	});

});