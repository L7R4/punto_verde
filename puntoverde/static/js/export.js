const button_export = document.getElementById('button_export')
const input_start_date = document.getElementById('start_date')
const input_end_date = document.getElementById('end_date')

input_start_date.addEventListener("change",()=>{
    let value = input_start_date.value
    console.log(value)
    console.log(typeof(value))
})


fetch('/admin/',{
    method: 'get',
    headers: {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json'}
    
}).then(
    function(response){
        return response.json()
    }
).then(data =>{
    console.log(data)
    const EXCEL_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8';
    const EXCEL_EXTENSION = '.xlsx';
    button_export.addEventListener("click", downloadExcel)

    function downloadExcel() {
        const worksheet = XLSX.utils.json_to_sheet(data);
        const workbook = {
            Sheets:{
                'data': worksheet
            },
            SheetNames: ['data']
        };
        const excelBuffer = XLSX.write(workbook,{bookType: 'xlsx', type:'array'});
        saveExcel(excelBuffer,'miArchivo')
    }

    function saveExcel(buffer, filename) {
        const data = new Blob([buffer], {type:EXCEL_TYPE});
        saveAs(data,filename+'_export_'+new Date().getTime()+EXCEL_EXTENSION);
    }
})




// var xlsx = require('xlsx')
// const jsonObject = require('./dataJ.json')
// var workBook = xlsx.utils.book_new()
// var workSheet = xlsx.utils.json_to_sheet(jsonObject)
// xlsx.utils.book_append_sheet(workBook,workSheet)
// xlsx.writeFile(workBook,"convertedJsontoExcel.xlsx")