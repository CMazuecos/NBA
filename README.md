# NBA
Este repositorio contiene dos archivos de python. 
### Archivos necesitados
- 'philadelphia76ers_analisis.py': archivo python que consigue las estadísticas a través de una api de cada jugador del equipo Philadelphia 76ers.
- 'config.txt': archivo txt con la clave para acceder a la api.
- 'pronostico.py': archivo de python que da los favoritos de la casa de apuestas sportytrader a ganar cada partido de la jornada de la nba
- 'requirements.txt': contiene todos las librerías necesarias para el correcto funcionamiento del programa.
- 'logo.png': imagen para el pdf
### Forma de ejecución de philadelphia76ers_analisis.py
- Descargamos el requirements.txt, config.txt y el archivo python en una misma carpeta.
- Ejecutar en la terminal 'pip install requirements.txt'.
- Ejecutar 'philadelphia76ers_analisis.py' y automáticamente se ejecutará el programa. 
- En primer lugar, se extraen los datos de la url.
- Posteriormente, se guardan en un csv
- Finalmente, se seleccionan las estadísticas que el COO considera más importantes para cada jugador y se imprimen en un pdf.
### Outputs
- Fichero 'philadelphia.pdf': archivo pdf con las estadísticas de los jugadores.
- Fichero 'philadelphia.csv': fichero csv donde está toda la información de la api sobre los jugadores.
### Forma de ejecución de pronostico.py
- Descargamos el requirements.txt y el archivo python en una misma carpeta.
- Ejecutar en la terminal 'pip install requirements.txt'.
- Ejecutar 'pronostico.py' y automáticamente se ejecutará el programa. 
- El programa extraerá las cuotas para los partidos de la jornada de la nba.
- Se analizarán los datos y el que menor cuota tenga, será el favorito para la casa de apuestas.
### Outputs
- Partidos, cuotas de cada equipo y favorito a ganar cada encuentro.
Para más aclaraciones, código explicado en el texto.
