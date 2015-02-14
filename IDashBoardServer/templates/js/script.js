$(document).ready(function() {
	var table = $('#main-data-table').DataTable({
		ajax: '/js/data.json',
			columns: [
			{'data': 'ip'},
			{'data': 'os'},
			{'data': 'status'},
			{'data': 'mem'},
			{'data': 'time'},
			{'data': 'remark'}
		],
		dom: 'R<"row"<"#vm-count.col-sm-6"><"col-sm-6"f>>rt<"row"<"col-sm-6"l><"col-sm-6"p>>',
		responsive: true
	});
	$('#main-data-table').removeClass('display').addClass('table table-striped table-bordered table-hover');
	// new $.fn.dataTable.FixedHeader(table); // DataTable插件的FixedHeader扩展，响应式表现较差

	$('#main-data-table tbody').on('click', 'tr', function() {
		console.log($('td', this).eq(0).text());
	});

	$('#vm-count').css('line-height', '30px').html('Now there are <strong>5</strong> virtual machines online');

});