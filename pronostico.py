import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(url):
    link = requests.get(url) # extraemos la url
    soup = BeautifulSoup(link.content, 'html.parser') # creamos el objeto soup
    return soup


def transform(sportytrader):
    partidos = sportytrader.find_all('span', {'class': "font-medium w-full lg:w-1/2 text-center dark:text-white"}) # extraemos los partidos y cuotas
    cuotas= sportytrader.find_all('span', {'class': 'px-1 h-booklogosm font-bold bg-primary-yellow text-white leading-8 rounded-r-md w-14 md:w-18 flex justify-center items-center text-base'})
    equipos = []
    lista_cuotas = []
    
    for partido in partidos:
        equipo = partido.find('a').text # extraemos los partidos
        equipos.append(equipo[1:-1]) # para eliminar los \n  
    for cuota in cuotas:
        cuota_partido = cuota.text # extraemos las cuotas
        lista_cuotas.append(cuota_partido) 
    cuotas_partido = []
    for i in range (0,len(lista_cuotas),2):
        cuota_primera = lista_cuotas[i] 
        cuota_segunda = lista_cuotas[i+1] 
        pronostico = cuota_primera + ' x '+ cuota_segunda # creamos una cuota para cada partido
        cuotas_partido.append(pronostico) # añadimos las cuotas a una lista
        favoritos = []
    for i in range (len(cuotas_partido)):
        equipos_partido = equipos[i].split(' - ') # creamos una lista con los equipos de cada partido
        cuotas = cuotas_partido[i].split(' x ')
        if cuotas[0] < cuotas[1]: # comparamos las cuotas para ver cual es el favorito
            favoritos.append(equipos_partido[0])
        else:
            favoritos.append(equipos_partido[1])
    return equipos, cuotas_partido, favoritos

def load(equipos, cuotas, favoritos): # imprime los resultados
    for i in range (len(equipos)):
        print('Partido:', equipos[i])
        print('Cuotas:',cuotas[i])
        print('Favorito a ganar el partido según la casa de apuestas:', favoritos[i])

   
    


if __name__ == '__main__':
    url = 'https://www.sportytrader.es/cuotas/baloncesto/usa/nba-306/'
    sportytrader = extract(url) # formato etl
    equipos, cuotas, favoritos = transform(sportytrader)
    load(equipos, cuotas, favoritos)
