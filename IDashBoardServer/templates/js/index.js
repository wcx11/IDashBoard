$(document).ready(function () {
	$('#login-form').validate({
		rules: {
			username: "required",
			password: "required"
		}
	});
});
