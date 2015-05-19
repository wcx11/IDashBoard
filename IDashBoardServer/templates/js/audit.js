/**
 * Created by wcx on 15/4/27.
 */
$(document).ready(function(){
    $('#audit-data-table').DataTable({
        dom: 'R<"row"<"#vm-count.col-sm-6"<"#vm-count-label">><"col-sm-6"f>>rt<"row"<"col-sm-6"l><"col-sm-6"p>>',
        ajax: '/get_untreated_applications/',
        columns:[
            {'data': 'applicant'},
            {'data': 'type'},
			{'data': 'parameter'},
			{'data': 'submissionTime'},
            {'data': 'treatment'}
        ],
        initComplete: function(){
            $('#vm-count').prepend($('#refresh-button-group'));
        },
        createdRow: function(row, data) {
			// 为每一行赋予一个虚拟机id
			$(row).attr('data-id', data.id);
		},
        rowCallback: function(row, data) {
            hostname = data.parameter.hostname;
            username = data.parameter.username;
            memory = data.parameter.memory;
            os = data.parameter.os;
            var parameterhtml = '';
            if(data.type=="new"){
                parameterhtml = '<div><strong>os:</strong>' + os + '<br/><strong>memory:</strong>' +  memory + '</div>';
            }
            else{
                parameterhtml = '<div><strong>uuid:</strong>'+data.parameter.uuid +'</div>'
            }

            var treatmenthtml = '<div><button class = "btn btn-success">ratify</button><button class="btn btn-danger">refuse</button></div>';
            $('td:eq(4)', row).html(treatmenthtml);
            $('td:eq(2)', row).html(parameterhtml);
        },
        drawCallback: function(){
            console.log('draw complete');
			var applicationCount = this.api().data().length;
            $('#vm-count-label').html('<label><strong> ' + applicationCount + ' </strong> untreated applications.</label>');
            if (applicationCount != 0) {
				// 单击单元格跳转到详细信息
				$('#audit-data-table tr').on('click', 'button.btn-success',function() {
                    $(this).parent().find("button").attr("disabled", true);
                    var data_id = $(this).parentsUntil('tbody').last().attr('data-id');
                    var td = $(this).parentsUntil('tr');
					console.log(data_id);
                    var json = {'id': data_id};
                    $.post('/ratify_application/', json, function(data){
                        td.html(data);
                    })
					//$(location).attr('href', '/detail/' + $(this).attr('data-id') + '/');
				});
                $('#audit-data-table tr').on('click', 'button.btn-danger',function() {
                    $(this).parent().find("button").attr("disabled", true);
                    var data_id = $(this).parentsUntil('tbody').last().attr('data-id');
                    var td = $(this).parentsUntil('tr');
					console.log(data_id);
                    var json = {'id': data_id};
                    $.post('/refuse_application/', json, function(data){
                        td.html(data);
                    })
					//$(location).attr('href', '/detail/' + $(this).attr('data-id') + '/');
				});

			}
        }
    });
    $('#audit-data-table').removeClass('display').addClass('table table-striped table-bordered table-hover');
    $('#refresh-button').click(refreshData);
    $('#ratify-button').click(ratifyAll);
    $('#refuse-button').click(refuseAll);
});

function refreshData() {
	console.log('reload start');
	$('#audit-data-table').DataTable().ajax.reload(function() {
		console.log('reload complete');
	}, false);
}

function ratifyAll() {
    var url = "/ratify_all/";
    $.post(url, function(json){
        refreshData();
    });
}

function refuseAll() {
    var url = "/refuse_all/";
    $.post(url, function(json){
        refreshData();
    });
}