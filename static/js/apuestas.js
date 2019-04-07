
//Extraccion de la informacion enviada desde el Backend
var informacion = document.getElementById("informacionPartidos").innerHTML;

// Quito todos los caracteres que no hacen parte de la informacion
//solo la primera posicion del arreglo es informacion
var arregloDeTexto = informacion.split("<");

//Guardo la informacion en una variable
informacionSoloPartidos = arregloDeTexto[0];

//Estandarizamos la informacion para que solo un caracter separe los partidos y los datos de los partidos
informacionSoloPartidos = informacionSoloPartidos.replace(/'/gi, '');
informacionSoloPartidos = informacionSoloPartidos.replace(/, /gi, ',');
informacionSoloPartidos = informacionSoloPartidos.replace(/  /gi, '');
informacionSoloPartidos = informacionSoloPartidos.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/gi, "c");
informacionSoloPartidos = informacionSoloPartidos.replace("c", '');


//console.log(informacionSoloPartidos);

//Creamos un arreglo de los partidos
var arregloDePartidos = informacionSoloPartidos.split("cc");

//console.log(arregloDePartidos[0]);

for( var i = 0 ; i < arregloDePartidos.length ; i++)
{
    var arrgloDetalles = arregloDePartidos[i].split(",");

    document.write("<div class='container col-sm-10 col-lg-10 col-md-10'>")
    document.write("    <div class='partido container'")
    document.write("        <div class='equipos'>");
    document.write("            <p>"+ arrgloDetalles[0]+"</p>")
    document.write("</div></div></div>")
    console.log(arrgloDetalles);   
}

