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
			newHtml = "<table class='table table-bordered'>"
					  +"<tr>"
					  +"<th>Food item:"
					  +"</th>"
					  +"<td>"
					  + data["food_data"]["display_name"]
					  +"</td>"
					  + "</tr>"
					  +"<tr>"
					  +"<th>Portion size:"
					  +"</th>"
					  +"<td>"
					  + data["food_data"]["portion_amt"]
					  +"</td>"
					  + "</tr>"
					  +"<tr>"
					  +"<th>Calories:"
					  +"</th>"
					  +"<td>"
					  + data["food_data"]["calories"]
					  +"</td>"
					  + "</tr>"
					  +"<tr>"
					  +"<th>Added Sugars:"
					  +"</th>"
					  +"<td>"
					  + data["food_data"]["added_sugars"]
					  +"</td>"
					  + "</tr>"
					  +"</table>"		
			// alert(newHtml);
			panelContent = $("#panelcontent");
			// alert(panelContent.text());
			panelContent.html(newHtml);
			panelContainer.show();
		});		
	});

});