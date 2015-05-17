/**
 * Created by wcx on 15/4/28.
 */
$(document).ready(function(){
    $('#myVMs-data-table').DataTable({
        dom: 'R<"row"<"#vm-count.col-sm-6"<"#vm-count-label">><"col-sm-6"f>>rt<"row"<"col-sm-6"l><"col-sm-6"p>>',
        ajax: '/get_my_VMs/',
        columns:[
            {'data': 'uuid'},
            {'data': 'state'},
			{'data': 'parameter'},
            {'data': 'treatment'}
        ],
        initComplete: function(){
            //$('#host-count').prepend($('#refresh-button-group'));
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
            osset = ['ubuntu 14.04 LTS'];
            memoryset = ['1024M', '2048M'];
            var states = ["online", "offline", "savestate"];
            var parameterhtml = '<div><strong>os:</strong>' + osset[os - 1] + '<br/><strong>hostname:</strong>'
                + hostname + '<br><strong>username:</strong>' + username + '<br><strong>memory:</strong>' +  memoryset[memory - 1] + '</div>';

            var treatmenthtml = '<div><button class = "btn btn-success startVM">start</button><button class = "btn btn-success shutdownVM">shutdown</button><button class = "btn btn-success savestateVM">savestate</button><button class="btn btn-danger deleteVM" data-toggle="modal" data-target="#deleteModal">delete</button></div>';
            $('td:eq(3)', row).html(treatmenthtml);
            $('td:eq(2)', row).html(parameterhtml);
            $('td:eq(1)', row).html(states[data.state]);
        },
        drawCallback: function () {
            var myVMCount = this.api().data().length;
            $('#vm-count-label').html('<label>I have <strong> ' + myVMCount + ' </strong> Virtual Machines.</label>');
            if (myVMCount != 0) {
                // 单击单元格跳转到详细信息
                $('#myVMs-data-table tr').on('click', 'button.startVM', function () {
                    var id = $(this).parentsUntil('tbody').last().attr('data-id');
                    $(this).parentsUntil('tr').last().html("please wait...");
                    json_obj = {'id': id}
                        $.post('/start_apply/', JSON.stringify(json_obj), function(data){
                        }
                    );
                });
                $('#myVMs-data-table tr').on('click', 'button.shutdownVM', function () {
                    var id = $(this).parentsUntil('tbody').last().attr('data-id');
                    $(this).parentsUntil('tr').last().html("please wait...");
                    json_obj = {'id': id}
                        $.post('/stop_apply/', JSON.stringify(json_obj), function(data){
                        }
                    );
                });
                $('#myVMs-data-table tr').on('click', 'button.savestateVM', function () {
                    var id = $(this).parentsUntil('tbody').last().attr('data-id');
                    $(this).parentsUntil('tr').last().html("please wait...");
                    json_obj = {'id': id}
                        $.post('/savestate_apply/', JSON.stringify(json_obj), function(data){
                        }
                    );
                });
                $('#myVMs-data-table tr').on('click', 'button.deleteVM', function () {
                    $("#deleteModal").attr("data-id", $(this).parentsUntil('tbody').last().attr('data-id'))
                });
            }
        }
    });
    $('#myVMs-data-table').removeClass('display').addClass('table table-striped table-bordered table-hover');
});

function confirmDelete(data_id){
    json_obj = {'id': $('#deleteModal').attr('data-id')}
    $('#myVMs-data-table').find('tr[data-id='+$('#deleteModal').attr('data-id')+"]").find('td').last().html("please wait...");
    $.post('/delete_apply/', JSON.stringify(json_obj), function(data){
        }
    );
}