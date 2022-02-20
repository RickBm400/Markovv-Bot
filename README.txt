									MARKOV BOT 
-------------------------------------------------------------------------------------------
Librerías usadas: 
python-telegram-bot
telegram
numpy 
python-dotenv
networkx 
urllib3
beautifulsoup4
requests
matplotlib
sympy
markov
bs4

instalar con pip install -r requirements.txt

Python 3.8.6
-------------------------------------------------------------------------------------------
Main.py: 

Algoritmo principal de la solución; Ejecuta el bot suministrandose un Token de acceso y 
permitiendo realizar solicitudes por medio de los comandos pre establecidos.

\start - Arranca el bot.
\mkovv - Ejecuta función para aplicar modelo de Markov a partir de un link suministrado y haciendo 
	Web Scraping de la pagina. Este programa retorna una cadena de 30 caracteres y un .txt con 
	todo el texto recopilado de la pagina y reorganizado. 
\lhcc - Ejecuta función que retorna una ecuación de recurrencia, el algoritmo verifica si esta es 
	Linealmente homogenea con coeficientes constantes.
\cbase - Dado una relación de recurrencia y sus casos base, retorna la ecuación correspondiente a la 
	solución de dicha relación.
\graff - Dado un numero de vertices, aristas y el grado máximo, retorna el dibujo de un grafo simple.

Markbot.py: 

Ejecuta las funciones del bot dados los comandos anteriormente definidos y sus respectivos
parametros de entrada (Visualizar ejemplos con el comando \help en el bot o mirar función help en el codigo).

Metod.py: 

Contiene todas las operaciones que serán importadas dentro de markbot.py, estas son las encargadas de 
realizar todos los procesos necesarios para que el bot pueda solucionar los problemas planteados.

src: 

Contiene las imagenes y el texto generado por el modelo de markov que posteriormente serán retornados 
por el bot y mostrados por el usuario.
Nota: Cabe aclarar que estos documentos se actualizan cada que el usuario realiza una petición.
------------------------------------------------------------------------------------------
