/**
 * Created by wcx on 15/4/28.
 */

$(document).ready(function(){
    $('#application-data-table').DataTable({
        dom: 'R<"row"<"#vm-count.col-sm-6"<"#vm-count-label">><"col-sm-6"f>>rt<"row"<"col-sm-6"l><"col-sm-6"p>>',
        ajax: '/get_my_applications/',
        columns:[
            {'data': 'submissionTime'},
			{'data': 'parameter'},
			{'data': 'type'},
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
            vm_type = data.parameter.vm_type;
            osset = ['ubuntu 14.04 LTS'];
            memoryset = ['1024M', '2048M'];
            vm_typeset = ['普通虚拟机', 'OpenStack 控制器', 'OpenStack 存储器'];
            if(data.type=='new'){
                var parameterhtml = '<div><strong>vm_type:</strong>' + vm_typeset[vm_type - 1] + '<br><strong>os:</strong>' + osset[os - 1] + '<br><strong>memory:</strong>' +  memoryset[memory - 1] + '</div>';
            }
            else{
                parameterhtml = '<div><strong>uuid:</strong>'+ data.parameter.uuid+'</div>'
            }
            var states = ["1.已申请", "2.已通过", "3.已拒绝", "4.正在执行", "5.执行完毕", "6.执行异常"];
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