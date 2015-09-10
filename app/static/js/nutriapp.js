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
		url = globals.baseUrl + "/profile/" + fid.toString();
		$.getJSON(url, function (data) {
			newHtml = "<h3> First name =" 
					  + data["profile_data"]["first_name"]
					  + "</h3>"			
			// alert(newHtml);
			panelContent = $("#panelcontent");
			// alert(panelContent.text());
			panelContent.html(newHtml);
			panelContainer.show();
		});		
	});

});