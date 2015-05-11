/**
 * Created by wcx on 15/4/28.
 */

$(document).ready(function(){
    $('#application-data-table').DataTable({
        dom: 'R<"row"<"#vm-count.col-sm-6"<"#vm-count-label">><"col-sm-6"f>>rt<"row"<"col-sm-6"l><"col-sm-6"p>>',
        ajax: '/get_my_applications/',
        columns:[
            {'data': 'type'},
			{'data': 'parameter'},
			{'data': 'submissionTime'},
            {'data': 'state'}
        ],
        initComplete: function(){
            //$('#vm-count').prepend($('#refresh-button-group'));
        },
        createdRow: function(row, data) {
			// 为每一行赋予一个虚拟机id
			$(row).attr('data-id', data.id);
		},
        rowCallback: function(row, data) {
            memory = data.parameter.memory;
            os = data.parameter.os;
            osset = ['ubuntu 14.04 LTS'];
            memoryset = ['1024M', '2048M'];
            var parameterhtml = '<div><strong>os:</strong>' + osset[os - 1] + '<br><strong>memory:</strong>' +  memoryset[memory - 1] + '</div>';
            var states = ["1.applied", "2.ratified", "3.refused", "4.doing", "5.done", "6.exception"];
            $('td:eq(3)', row).html(states[data.state]);
            $('td:eq(1)', row).html(parameterhtml);
        },
        drawCallback: function () {
            var applicationCount = this.api().data().length;
            $('#vm-count-label').html('<label>I have <strong> ' + applicationCount + ' </strong> historical applications.</label>');
        }
    });
    $('#application-data-table').removeClass('display').addClass('table table-striped table-bordered table-hover');
});