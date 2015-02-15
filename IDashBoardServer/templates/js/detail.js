var refreshInterval = 0;
var clockId = -1;

$(document).ready(function() {

	// 刷新表格数据按钮
	$('#refresh-button').click(refreshData);
	
	// 初始化数据
	refreshData();
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
 * 刷新虚拟机数据
 */
function refreshData() {
	console.log('reload start');

	// var url = $(location).attr('href').replace(/\/detail\//, '/get-detail/');
	var url = '/js/detail.json';

	$.post(url, function(json) {
		// 在这里更新表格数据
		var data = json;

		$('#td-os').text(data.uName);
		$('#td-cpu-info').text(data.cpuInfo);
		$('#td-total-mem').text(data.memory);
		$('#td-total-swap').text(data.swap);

		$('#td-cpu-load').text(data.cpuLoad);
		$('#td-mem-load').text(data.memory);
		$('#td-swap-load').text(data.swap);
		$('#td-task-info').text(data.tasks);
		$('#td-user').text(data.userName);
		
		$('#td-ipv4').text(data.ipv4);
		$('#td-ipv6').text(data.ipv6);
		$('#td-broadcast').text(data.broadcast);
		$('#td-mask').text(data.mask);
		$('#td-dns').text(data.dns);

		// 更新完毕
		console.log('reload complete');
	}, 'json');
}
