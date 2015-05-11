/**
 * Created by wcx on 15/5/4.
 */
$(document).ready(function () {
	$('#apply-form').validate({
		rules: {
			password: {
				required: true,
				minlength: 6
			},
			pwd_confirm: {
				required: true,
				equalTo: "#password"
			}
		}
	});
});