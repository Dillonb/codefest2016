// This is some custom jQuery to help determine how to create an event (user or club)
$( document ).ready(function() {
	// Initialize the club select to hidden
	$("#id_club").hide();
	// If the club button is selected, show the selector html
	$("#club_event_button").click(function(){
		$("#id_club").show();
	});   
	// If the user button is selected, hide the selector html
	$("#individual_event_button").click(function(){
		$("#id_club").hide();
	});   

});

