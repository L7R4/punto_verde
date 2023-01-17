const button_export = document.getElementById('button_export')
const input_start_date = document.getElementById('start_date')
const input_end_date = document.getElementById('end_date')
const message_1 = document.querySelector(".message_1")
const message_2 = document.querySelector(".message_2")
let value_input_start_date="";
let value_input_end_date ="";
let dates_to_download ={}



fetch('/admin/',{
    method: 'get',
    headers: {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json'}
    
}).then(
    function(response){
        return response.json()
    }
).then(data =>{
    const EXCEL_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8';
    const EXCEL_EXTENSION = '.xlsx';

    input_start_date.addEventListener("change",()=>{
        let value = input_start_date.value
        value_input_start_date = reorderDatePicker(value);
    })

    input_end_date.addEventListener("change",()=>{
        let value = input_end_date.value
        value_input_end_date = reorderDatePicker(value);
    })

    button_export.addEventListener("click", () =>{
        if (value_input_start_date > value_input_end_date) {
            clearClassShow()
            message_1.classList.add("show")
            
        }else if(value_input_start_date == "" || value_input_end_date ==""){
            clearClassShow()
            message_2.classList.add("show")
        }
        else{
            downloadExcel()
        }
    })
    

    function downloadExcel() {
        try{
            if (value_input_start_date < value_input_end_date) {
                dates_to_download = data.filter(e =>  dateToNumber(e.date) >= value_input_start_date && dateToNumber(e.date) <= value_input_end_date)
            }else if(value_input_start_date == value_input_end_date){
                dates_to_download = data.filter(e =>  dateToNumber(e.date) == value_input_start_date)
            }
    
            const worksheet = XLSX.utils.json_to_sheet(dates_to_download);
            const workbook = {
                Sheets:{
                    'data': worksheet
                },
                SheetNames: ['data']
            };
            const excelBuffer = XLSX.write(workbook,{bookType: 'xlsx', type:'array'});
            saveExcel(excelBuffer,'planilla_votos')
        }catch(err){
            if (err.name == "TypeError") {
                clearClassShow()
                message_2.classList.add("show")
            }
        }
    }

    function saveExcel(buffer, filename) {
        const data = new Blob([buffer], {type:EXCEL_TYPE});
        saveAs(data,filename+EXCEL_EXTENSION);
    }
    
})

function reorderDatePicker(date) {
    let fecha_separada = date.split("-");
    let fecha_invertida = fecha_separada.reverse();
    let fecha_unida = parseInt(fecha_invertida.join(""));
    return fecha_unida;
}

function dateToNumber(date) {
    let clear_dates = date.split("/")
    let unir_dates = parseInt(clear_dates.join(""))
    return unir_dates;
}

function clearClassShow() {
    let class_show = document.querySelectorAll(".show")
    class_show.forEach(e => e.classList.remove("show"))
}