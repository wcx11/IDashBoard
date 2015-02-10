/**
 * Created by daiyue on 14-12-17.
 */

function refreshHomePage() {
    jQuery.post('/refreshHomePage/', JSON.stringify({abc: {h:5, g:['jstr', 'lala']}, de: {f:[24, 36]}}), postCallback, 'json');
}

$(document).ready(function(){
    setInterval(refreshHomePage, 2000);
});

function postCallback(data) {
    //alert(data.returns);
    //alert(data.ActiveVMs.length)
    var fragment = document.createDocumentFragment();
    for (ActiveVM in data.ActiveVMs)
    {
        var vm = data.ActiveVMs[ActiveVM];

        var tbody = "";
        i = 1;
        for(var key in vm.stateInfo){
            if(key != "Top"){
                tbody += '<tr >'+
                    '<td>'+i+'</td>'+
                    '<td>'+key+':</td>'+
                    '<td>'+vm.stateInfo[key]+'</td>'+
                    '</tr>';
                i ++;
            }
        }
        var top = vm.stateInfo["Top"];
        var lines = top.split('\n');
        for(l in lines){
            if(l < 10 && l != 0){
                if(lines[l] == ""){
                    break;
                }
                var values = lines[l].split(':');
                for(var index = 2; index < values.length; index++){
                    values[1]+=":"
                    values[1]+=values[index];
                }
                tbody += '<tr class="top">'+
                    '<td>'+i+'</td>'+
                    '<td>'+values[0]+':</td>'+
                    '<td>'+values[1]+'</td>'+
                    '</tr>';
                i ++;
            }
        }
        tbody = tbody.replace(/\n/g, "<br/>");//s.replace(/\./g, "!" )
        tbody = tbody.replace(/\s/g, "&nbsp;&nbsp;");

        var t = $(
            '<div class = "panel panel-warning">'+
                '<div class="panel-heading">VM &nbsp;&nbsp;'+data.ActiveVMs[ActiveVM]['IPAddress']+' >> '+data.ActiveVMs[ActiveVM]['stateInfo']['HostName']+'</div>'+'<div class="panel-body">'+
                '<table class = "table table-striped table-bordered table-responsive"  style="background-color: #d5d5d5">'+
                '<thead>'+
                '<tr>'+
                    '<th>#</th>'+
                    '<th>item</th>'+
                    '<th>value</th>'+
                '</tr>'+
                '</thead>'+
                '<tbody>'+
                tbody+
                '</tbody>'+
                '</table>'+
                '</div>'+
            '</div>'
        );
        $(fragment).append(t);
    }

    $(".vms").empty();
    $(".vms").append(fragment);

}