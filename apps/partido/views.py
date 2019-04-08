from django.shortcuts import render

# Create your views here.

import http.client
import json


### Juegos Jugados ####

def JugadosTodasLasLigas(request):
    espana =  Juegos_Jugados_liga("PD")
    inglaterra = Juegos_Jugados_liga("PL")
    italia = Juegos_Jugados_liga("SA")
    alemania = Juegos_Jugados_liga("BL1")
    partidos = espana,'/',inglaterra,'/',italia,'/',alemania
    return render(request, 'partido/partido.html',{'partidos':partidos})

def JuegosJugadosLigaEspaña(request):
	partidos = Juegos_Jugados_liga("PD") # PD: Liga española
	return render(request, 'partido/partido.html',{'partidos':partidos})


def JuegosJugadosLigaInglesa(request):
	partidos = Juegos_Jugados_liga("PL") # PL: Premiere League Inglesa
	return render(request, 'partido/partido.html',{'partidos':partidos})

def JuegosJugadosLigaItaliana(request):
	partidos = Juegos_Jugados_liga("SA") # SA: Serie A italiana
	return render(request, 'partido/partido.html',{'partidos':partidos})

def JuegosJugadosLigaAlemana(request):
	partidos = Juegos_Jugados_liga("BL1") # BL1: Bundes liga alemana primera division
	return render(request, 'partido/partido.html',{'partidos':partidos})

#### Juegos Programados ####
def JuegosProgramadosLigaEspaña(request):
	partidos = Juegos_programados_liga("PD") # PD: Liga española
	return render(request, 'partido/partido.html',{'partidos':partidos})

def JuegosProgramadosLigaInglesa(request):
	partidos = Juegos_programados_liga("PL") # PL: Premiere league inglesa
	return render(request, 'partido/partido.html',{'partidos':partidos})

def JuegosProgramadosLigaItaliana(request):
	partidos = Juegos_programados_liga("SA") # SA: Serie A italiana
	return render(request, 'partido/partido.html',{'partidos':partidos})

def JuegosProgramadosLigaAlemana(request):
	partidos = Juegos_programados_liga("BL1") # SA: Serie A italiana
	return render(request, 'partido/partido.html',{'partidos':partidos})

### Funciones para las consultas desde la API

#Descripción: funcion que devuelve la cantidad de fechas programadas programadas de una liga
#Entrada: el codigo de la liga ejemplo : String: "PD" - Primera division española 
#Salida: int cant_fechas un entero con la cantidad de fechas programdas de esa liga
def cantidad_fechas_prog_liga(liga):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'ccecd76c9c7f40f09ae18781d1c8f46d' }
    connection.request('GET', '/v2/competitions/'+liga+'/matches', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    listaMatchday = []
    cantElementos = response['count']
    for i in range(0, cantElementos):
        listaMatchday.append(response['matches'][i]['matchday'])
    Ordenada_listaMatchday = sorted(listaMatchday)
    cant_fechas = Ordenada_listaMatchday[len(Ordenada_listaMatchday)-1]             
    return cant_fechas

#Descripción: devuelve los datos de un part('Deportivo Alavés', 'CD Leganés', None, None, 31, '2019-04-07T10:00:00Z', None)ido consultado por el id del partido
#Entrada: string id corresponde al id del partido 
#Salida: lista con nombrelocal,nombrevisitante,goleslocal,golesvisitante,jornada,fechahora,ganador 
#        ejemplo: ('FC Barcelona', 'Deportivo Alavés', 3, 0, 1, '2018-08-18T20:15:00Z', 'HOME_TEAM')
def partidoPorID(id):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'ccecd76c9c7f40f09ae18781d1c8f46d' }
    connection.request('GET', '/v2/matches/'+id, None, headers )
    response = json.loads(connection.getresponse().read().decode())    
    equipoLocal = response['match']['homeTeam']['name']
    equipoVisitante = response['match']['awayTeam']['name']
    golesLocal = response['match']['score']['fullTime']['homeTeam']
    golesVisitante = response['match']['score']['fullTime']['awayTeam']
    jornada = response['match']['matchday']
    fechaHora = response['match']['utcDate'] 
    ganadorPartido = response['match']['score']['winner']    
    partido = equipoLocal,equipoVisitante,golesLocal,golesVisitante,jornada,fechaHora,ganadorPartido
    return partido 

#Descripción: funcion que devuelve que devuelve los partidos que se han jugado de una liga hasta la ultima fecha disputada
#Entrada: el codigo de la liga ejemplo : String: "PD" - Primera division española 
#Salida: La lista de los partidos jugados [(string namelocal,string namevisitante,int goleslocal,int golesvisitante,int jornada, string ganador)]
#ejemplo: 
# [('Villarreal CF', 'Rayo Vallecano de Madrid', 3, 1, 28, 'HOME_TEAM'),('Real Betis Balompié', 'FC Barcelona', 1, 4, 28, 'AWAY_TEAM')]
# HOME_TEAM (gano el local) ; AWAY_TEAM (gano el visitante) ; DRAW (el partido termino empatado)
def Juegos_Jugados_liga(liga):
    listaJugados = []
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'ccecd76c9c7f40f09ae18781d1c8f46d' }
    connection.request('GET', '/v2/competitions/'+liga+'/matches?status=FINISHED', None, headers )
    response = json.loads(connection.getresponse().read().decode()) 
    for i in range(0,1):
        equipoLocal = response['matches'][i]['homeTeam']['name'] 
        equipoVisitante = response['matches'][i]['awayTeam']['name']   
        golesLocal = response['matches'][i]['score']['fullTime']['homeTeam']
        golesVisitante = response['matches'][i]['score']['fullTime']['awayTeam']
        jornadaLiga = response['matches'][i]['matchday']
        ganadorPartido = response['matches'][i]['score']['winner']  # HOME_TEAM (gana equipoLocal), AWAY_TEAM ( gana equipoVisitante), DRAW (Empate)
        fechaHora = response['matches'][i]['utcDate']
        idLocal = response['matches'][i]['homeTeam']['id']
        idVisitante = response['matches'][i]['awayTeam']['id']
        idPartido = response['matches'][i]['id']
        partidoJugado = liga,equipoLocal,equipoVisitante,golesLocal,golesVisitante, jornadaLiga,ganadorPartido,fechaHora,idLocal,idVisitante,idPartido
        listaJugados.append(partidoJugado)

    return listaJugados

#Descripción: funcion que devuelve los partidos programadas de todas las fechas que aun no se han jugado
#Entrada: el codigo de la liga ejemplo : String: "PD" - Primera division española 
#Salida: una lista  con [(String namelocal,string namevisitante, int jornada)]
#ejemplo: [('Villarreal CF', 'SD Huesca', 35), ('CD Leganés', 'RC Celta de Vigo', 35)]

def Juegos_programados_liga(liga):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'ccecd76c9c7f40f09ae18781d1c8f46d' }
    connection.request('GET', '/v2/competitions/'+liga+'/matches?status=SCHEDULED', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    lista_partidos_disputar = []
    for i in range(0,len(response['matches'])):
        equipoLocal = response['matches'][i]['homeTeam']['name']
        equipoVisitante = response['matches'][i]['awayTeam']['name']
        jornadaLiga = response['matches'][i]['matchday']
        fechaHora = response['matches'][i]['utcDate']
        idLocal = response['matches'][i]['homeTeam']['id']
        idVisitante = response['matches'][i]['awayTeam']['id']
        idPartido = response['matches'][i]['id']
        partidoDisputar = equipoLocal,equipoVisitante,jornadaLiga,fechaHora,idLocal,idVisitante,idPartido
        lista_partidos_disputar.append(partidoDisputar)
    
    return lista_partidos_disputar



# Descripción: Función encargada de consultar los partidos que estan en estado SCHEDULED o programados
#              segun la liga especificada
# Entrada: string liga, numero_fecha 
#          posibles valores - codigos ligas: 
#                             Bundes Liga - BL1
#                             Champions league - CL
#                             Premiere League - PL
#                             Serie A italiana - SA
#                             Primera Division española - PD
# Salida: 
# todos los partidos en estado programado de la liga especificada, en la jornada especificada con las llaves
# ['competition', 'count', 'matches', 'filters']
#{'matches': ['lastUpdated', 'utcDate', 'matchday', 'status', 'score', 'homeTeam', 'id', 'awayTeam', 'group', 'stage', 'season', 'referees']}
#{'homeTeam': ['id', 'name']}
# salida: [(namelocal,namevisitante),(namelocal,namevisitante),....]
def Juegos_Programados_liga_jornada(liga,fecha):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'ccecd76c9c7f40f09ae18781d1c8f46d' }
    connection.request('GET', '/v2/competitions/'+liga+'/matches?status=SCHEDULED', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    fecha_actual = fecha
    lista_partidos_disputar = []
    for i in range(0,len(response['matches'])):
        if (fecha_actual == response['matches'][i]['matchday']):
            partidoDisputar = (response['matches'][i]['homeTeam']['name'],response['matches'][i]['awayTeam']['name'])
            lista_partidos_disputar.append(partidoDisputar)
    return lista_partidos_disputar