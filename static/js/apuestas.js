
//Extraccion de la informacion enviada desde el Backend
var informacionR = document.getElementById("informacionPartidos").innerHTML;
var lista = document.getElementById("lista");


var ruta = window.location;
var reference = ruta.href;


// Quito todos los caracteres que no hacen parte de la informacion
//solo la primera posicion del arreglo es informacion
var informacion = informacionR.split("<");

//Guardo la informacion en una variable
informacion = informacion[0];

iniciar();

function iniciar()
{
    var info = informacion;
    var infoDepurada;
    var arregloPartidos;

    if(reference == "http://127.0.0.1:8000/partidos/JugadosTodasLigas")
    {
        document.getElementById("jornada").style.display = "none";
        var ligaUna = ligas(info);
        for(i=0; i<ligaUna.length; i++)
        {  
            infoDepurada = depurarTexto(ligaUna[i]);
            arregloPartidos = partidosOrdenar2(infoDepurada);

            cargarLigas(arregloPartidos);
            console.log(arregloPartidos);
            
        }
    }
    else
    {
        infoDepurada = depurarTexto(info);
        arregloPartidos = partidosOrdenar(infoDepurada);
        document.getElementById("Button").onclick = cargar;
        principio2();
        function cargar()
        {
            cargarPartidos(arregloPartidos, arregloPartidos.length, 4)
        }
    }
}


function partidos(informacioBruto)
{
    var infoDepurada = depurarTexto(informacioBruto);
    var arregloPartidos = partidosOrdenar(infoDepurada);
    crearSelect(arregloPartidos, 2);
    return arregloPartidos;
}




function depurarTexto(inf)
{
    //Estandarizamos la informacion para que solo un caracter separe los partidos y los datos de los partidos
    inf = inf.replace(/'/gi, '');
    inf = inf.replace(/, /gi, ',');
    inf = inf.replace(/  /gi, '');
    inf = inf.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/gi, "c");
    inf = inf.replace("c", '');
    return inf;
}

function extrarProximaTemporada(par)
{
    par = par[0].split(",");
    par = par[2];
    return par;
}


function partidosOrdenar(info)
{
    //Creamos un arreglo de los partidos
    var info = info.split("cc");
    return info;
}

function partidosOrdenar2(info)
{
    //Creamos un arreglo de los partidos
    var info = info.split("c,c");
    return info;
}


function crearSelect(info, pos)
{
    var mayor = 0;
    for(var i = 0 ; i < info.length ; i++)
    {
        
        var partido = info[i];
        partido = partido.split(",");

        if(mayor < partido[pos])
        {
            mayor = partido[pos];
            //console.log(mayor);
            lista.innerHTML += "<option>" + mayor + "</option>";
            //console.log(lista);
        }
    }
}


function principio()
{
    var informacionR = document.getElementById("informacionPartidos").innerHTML;
    var lista = document.getElementById("lista");

    // Quito todos los caracteres que no hacen parte de la informacion
    //solo la primera posicion del arreglo es informacion
    var informacion = informacionR.split("<");

    //Guardo la informacion en una variable
    informacion = informacion[0];

    var tempo;
    document.write("<br>");
    document.write("<div class='container'>");
    document.write("<h1 class='titulo-formulario1'>Proxima Temporada</h1>");
    document.write("</div>");
    crearSelect(depurarTexto(informacion), 2);
    tempo = extrarProximaTemporada(partidos(informacion));
    console.log(tempo)
    cargarPartidos(partidos(informacion), 4, tempo);
}

function cargarPartidos(arregloDePartidos, tam)
{
    var pos = lista.options[lista.selectedIndex].value;
    console.log(pos);

    for( var i = 0 ; i < tam ; i++)
    {
        var arrgloDetalles = arregloDePartidos[i].split(",");
        if(arrgloDetalles[2] == pos)
        {
            imprimirPartidos(arrgloDetalles);
        }
    }      
}

function imprimirPartidos(arrgloDetalles)
{
    var horario = arrgloDetalles[3].split("T");
    var fecha = horario[0];
    fecha = fecha.replace(/c/gi ,'/' );
    var hora = horario[1];
    

    document.write("<div class='container col-sm-10 col-lg-10 col-md-10'>")
    document.write("    <div class='partido container onclick'>")
    document.write("        <div class='equipos'>");
    document.write("            <div class='enfrentamiento'>" )
    document.write("                <div class='container col-lg-5 col-md-5 col-sm-5 equipo1 col-5'>")
    document.write("                    <p class='informacion'>" + arrgloDetalles[0] + "</p>")
    document.write("                </div>")
    document.write("                <div class='container col-lg-2 col-md-2 col-sm-2 equipo2 col-2 vs'>")
    document.write("                    <p class='informacion'>" + " VS " + "</p>")
    document.write("                </div>")
    document.write("                <div class='container col-lg-5 col-md-5 col-sm-5 equipo2 col-5'>")
    document.write("                    <p class='informacion'>" + arrgloDetalles[1] + "</p>")
    document.write("                </div>")
    document.write("            </div>")
    document.write("            <div class='temporada container'>" )
    document.write("               <p class='informacion informacion3'> Temporada: "+ arrgloDetalles[2] + "</p>")
    document.write("            </div>")
    document.write("            <div class='horario container'>" )
    document.write("                <p class='informacion informacion2'>")
    document.write("                    <a><i class='fa fa-calendar inf'></i>" + fecha + "<i class='far fa-clock inf'></i>" + hora + "</a>")
    document.write("                </p>")
    document.write("            </div>")
    document.write("        </div>")
    document.write("    </div>")
    document.write("</div>")
    document.write(                      )
    document.write("")
    //console.log(arregloDePartidos[i]);   
    
}

//--------------------------------------------------------------------------------------------



function principio2()
{
    var informacionR = document.getElementById("informacionPartidos").innerHTML;
    var lista = document.getElementById("lista");

    // Quito todos los caracteres que no hacen parte de la informacion
    //solo la primera posicion del arreglo es informacion
    var informacion = informacionR.split("<");

    //Guardo la informacion en una variable
    informacion = informacion[0];

    var tempo;
    document.write("<br>");
    document.write("<div class='container'>");
    document.write("<h1 class='titulo-formulario1'>Proxima Temporada</h1>");
    document.write("</div>");
    crearSelect(depurarTexto(informacion), 2);
    tempo = extrarProximaTemporada(partidos(informacion));
    console.log(tempo)
    cargarPartidos2(partidos(informacion));
}


function cargarPartidos2(arregloDePartidos)
{
    for( var i = 0 ; i < arregloDePartidos.length ; i++)
    {
        var arrgloDetalles = arregloDePartidos[i].split(",");
        imprimirPartidos(arrgloDetalles);
    }      
}


function ligas(info)
{
    info = info.split(" / ");
    
    return info;
}


function cargarLigas(arregloDePartidos)
{
    for( var i = 0 ; i < arregloDePartidos.length ; i++)
    {
        var arrgloDetalles = arregloDePartidos[i].split(",");
        //console.log(arregloDePartidos[i]);
        imprimirLigas(arrgloDetalles);
    }      
}

function imprimirLigas(arrgloDetalles)
{
    var ligaIm = arrgloDetalles[0].split(',');
    console.log(ligaIm);
    ligaIm = ligaIm[0];
    var gLocal = arrgloDetalles[3];
    var gVisit = arrgloDetalles[4];
    var horario = arrgloDetalles[7].split("T");
    var fecha = horario[0];
    fecha = fecha.replace(/c/gi ,'/' );
    var hora = horario[1];

    var ligaEs ;
    ligaEs = ligaIm[3]+ligaIm[4];

    if(ligaEs == "PD" || ligaEs == "cPD")
    {
        document.write("<div class='botonera'>");
        document.write("<h2 class='titulo-formulario2 container'>Liga Española</h2>");
        document.write("<p>     ");
        document.write("    <a type='submit' class='btn btn-success btn-block textoFormulario btn-marcador' href = 'JugadosEspaña'> Ver mas Marcadores </a>")
        document.write("</p>     ");
        document.write("</div>");
    }
    if(ligaIm == " PL" || ligaIm == " cPL")
    {
        document.write("<div class='botonera'>");
        document.write("<h2 class='titulo-formulario2 container'>Premiere League Inglesa</h2>");
        document.write("<p>     ");
        document.write("    <a type='submit' class='btn btn-success btn-block textoFormulario btn-marcador' href = 'JugadosInglaterra'> Ver mas Marcadores </a>")
        document.write("</p>     ");
        document.write("</div>");
        console.log(ligaIm);
    }
    if(ligaIm == " SA" || ligaIm == " cSA")
    {
        document.write("<div class='botonera'>");
        document.write("<h2 class='titulo-formulario2 container'>Serie A italiana</h2>");
        document.write("<p>     ");
        document.write("    <a type='submit' class='btn btn-success btn-block textoFormulario btn-marcador' href = 'JugadosItalia'> Ver mas Marcadores </a>")
        document.write("</p>     ");
        document.write("</div>");
        console.log(ligaIm);
    }
    if(ligaIm == " BL1" || ligaIm == " cBL1")
    {
        document.write("<div class='botonera'>");
        document.write("<h2 class='titulo-formulario2 container'>Bundes liga alemana primera division</h2>");
        document.write("<p>     ");
        document.write("    <a type='submit' class='btn btn-success btn-block textoFormulario btn-marcador' href = 'JugadosAlemania'> Ver mas Marcadores </a>")
        document.write("</p>   ");
        document.write("</div>");
        console.log(ligaIm);

    }
    document.write("<div class='container col-sm-10 col-lg-10 col-md-10 containerLigas'>")
    document.write("    <div class='partido container onclick'>")
    document.write("        <div class='equipos'>");
    document.write("            <div class='enfrentamiento'>" )
    document.write("                <div class='container col-lg-5 col-md-5 col-sm-5 equipo1 col-5'>")
    document.write("                    <p class='informacion'>" + arrgloDetalles[1] + "</p>")
    document.write("                </div>")
    document.write("                <div class='container col-lg-2 col-md-2 col-sm-2 equipo2 col-2 vs'>")
    document.write("                    <p class='informacion'>" + " VS " + "</p>")
    document.write("                </div>")
    document.write("                <div class='container col-lg-5 col-md-5 col-sm-5 equipo2 col-5'>")
    document.write("                    <p class='informacion'>" + arrgloDetalles[2] + "</p>")
    document.write("                </div>")
    document.write("            </div>")
    document.write("            <div >" )
    document.write("                <div class='marcador container col-lg-5 col-md-5 col-sm-5 equipo1 col-5'>")
    document.write("                    <p class='informacion'>" + gLocal + "</p>")
    document.write("                </div>")
    document.write("                <div class='marcador container col-lg-5 col-md-5 col-sm-5 equipo2 col-5'>")
    document.write("                    <p class='informacion'>" + gVisit + "</p>")
    document.write("                </div>")
    document.write("            </div>")
    document.write("            <div class='temporada container'>" )
    document.write("               <p class='informacion informacion3'> Temporada: "+ arrgloDetalles[3] + " (Terminado)" + "</p>")
    document.write("            </div>")
    document.write("            <div class='horario container'>" )
    document.write("                <p class='informacion informacion2'>")
    document.write("                    <a><i class='fa fa-calendar inf'></i>" + fecha + "<i class='far fa-clock inf'></i>" + hora + "</a>")
    document.write("                </p>")
    document.write("            </div>")
    document.write("        </div>")
    document.write("    </div>")
    document.write("</div>")
 
    //console.log(arregloDePartidos[i]);   
    
}