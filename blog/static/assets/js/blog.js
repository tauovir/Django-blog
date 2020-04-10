$(document).ready(function() {
	
	/* ======= Highlight.js Plugin ======= */ 
    /* Ref: https://highlightjs.org/usage/ */     
  

	/**
	 * @ Description: This function check weather email is valid or not
	 * @param {*} email 
	 */
	function isEmail(email) {
		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		return regex.test(email);
	  }

	  /**
	   * Description:
	   * On button click,it take email address and csrf toek(It is required as we are making Post request)
	   * If email is incorrect, error message will be generated,else ajax call will be sent
	   * 
	   */
	$('#subscribe-btn').click(function(){

		email = $("input[name=semail]").val();
		csrf = $("input[name=csrfmiddlewaretoken]").val();
		 is_email = isEmail(email)
		if (is_email == false)
		{
			$(".errorClass1" ).html("Please enter valid email!" )
				return 
		 }

		$.ajax
		({ 
			url: 'subscribe/',
			data: {"emial": email,'csrfmiddlewaretoken':csrf},
			type: 'post',
			success: function(result)
			{
				if (result.code == 200){
				$(".errorClass1").empty();
				$('#exampleModalCenter').modal('show');
				}
				else{
				$(".errorClass1" ).html(result.message)
				}
			}
		});
	});

/**
 * Remove error message from while typing in input
 */
$( "#semail" ).keypress(function() {
		console.log( "Handler for .keypress() called." );
		$(".errorClass1").empty();
});



}) // End Document