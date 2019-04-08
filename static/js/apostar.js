
var infoPar=[];
var vector = almacen[0].split("cc");
//console.log(vector[0]);
var area = document.getElementsByClassName("equipos");

for (var i = 0; i < area.length; i++) 
{
    area[i].addEventListener('click', printDetails);
}

var referencia;
function printDetails() 
{
    var counter = 0;
    var areaf = document.getElementById(this.id);
    var pos = areaf.getAttribute("name");
    pos -= 0;

    var informacion = vector[pos];
    infoPar.push(informacion);
    console.log(infoPar);
    referencia = window.open("http://127.0.0.1:8000/apuestas/apuesta", "Apuestas", "width=500,height=500,scrollbars=NO");
    referencia.focus();
    
    //referencia.getElementById("id_idApuesta").value = informacion;
    //console.log(apuesta);
}

function name() 
{
    return infoPar;    
}
