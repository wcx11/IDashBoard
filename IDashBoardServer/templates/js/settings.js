$(document).ready(function () {
	$('#user-info-form').validate({
		rules: {
			username: "required",
			email: {
				required: true,
				email: true
			}
		}
	});

	$('#password-form').validate({
		rules: {
			password: "required",
			newpassword: {
				required: true,
				minlength: 6
			},
			confirmpassword: {
				required: true,
				equalTo: "#password"
			}
		}
	});
});
