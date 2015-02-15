var refreshInterval = 0;
var clockId = -1;

$(document).ready(function() {

	// 数据表插件初始化
	$('#main-data-table').DataTable({
		responsive: true,
		dom: 'R<"row"<"#vm-count.col-sm-6"><"col-sm-6"f>>rt<"row"<"col-sm-6"l><"col-sm-6"p>>',
		ajax: '/js/data.json',
			columns: [
			{'data': 'ip'},
			{'data': 'os'},
			{'data': 'status'},
			{'data': 'mem'},
			{'data': 'time'},
			{'data': 'remark'}
		],
		initComplete: function() {
			console.log('init complete');
			// 显示在线虚拟机数量
			$('#vm-count').html('<label><strong> ' + this.api().data().length + ' </strong> virtual machines online.</label>');
			// 添加刷新按钮组
			$('#vm-count').prepend($('#refresh-button-group'));
		},
		createdRow: function(row, data) {
			$(row).attr('data-id', data.id);
		}
	});

	// 为datatable插件应用bootstrap样式
	$('#main-data-table').removeClass('display').addClass('table table-striped table-bordered table-hover');
	
	// // DataTable插件的FixedHeader扩展，响应式表现较差，暂不使用
	// new $.fn.dataTable.FixedHeader($('#main-data-table').DataTable());

	// 单击单元格跳转到详细信息
	$('#main-data-table tbody').on('click', 'tr', function() {
		console.log($(this).attr('data-id'));
		$(location).attr('href', '/detail/' + $(this).attr('data-id') + '/');
	});

	// 刷新表格数据按钮
	$('#refresh-button').click(refreshData);
});

/**
 * 设置自动刷新时间
 */
function setRefreshOption(interval, index) {
	clearInterval(clockId);
	if (interval > 0) {
		clockId = setInterval(refreshData, interval * 1000);
	}
	console.log('interval set to ' + interval);
	// 更新UI
	$('#refresh-option-menu span.glyphicon-check').removeClass('glyphicon-check').addClass('glyphicon-unchecked');
	$('#refresh-option-menu span').eq(index).removeClass('glyphicon-unchecked').addClass('glyphicon-check');
}

/**
 * 刷新DataTable数据
 */
function refreshData() {
	console.log('reload start');
	$('#main-data-table').DataTable().ajax.reload(function() {
		console.log('reload complete');
	}, false);
}
