import logging
import os
import numpy as np
from re import split
from numpy.ma.core import empty
from sympy.core.numbers import E
from sympy.ntheory.factor_ import udivisor_count
from sympy.polys.polyoptions import Method
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, message, bot
import matplotlib.pyplot as plt
from metod import play

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class Bot: 

    #constructor: metodos privados empiezan con "_" 
    def __init__(self):
            pass

    #Metodo inicio 
    def start (self, update, context):
        uname =update.message.chat.username
        logger.info(f"El usuario {uname} ha iniciado el bot...")
        name = update.message.chat.first_name
        lname = update.message.chat.last_name
        update.message.reply_text(f"M: Hola, {name} {lname}, si necesitas ayuda,\npuedes consultar el comando /help")
    
    #Pedir ayuda 
    def help (self, update, context):
        uname =update.message.chat.username
        logger.info(f"El usuario {uname} ha solicitado ayuda...")
        msg = """
                Markov: 
            Hola\!, esta es una lista de mis comandos:

            \- /help:   
            Pedirme ayuda

            \- /lhcc:   
            Imprimir relación de recurrencia LHCC\.\n
            Ingrese los coeficientes del polinomio caracteristico\.\n
            Ejemplo:\n
            /lhcc \[1,\-2,\-1,2\]

            \- /cbase:  
            Mostrar expresión con los casos bases\.\n
            Ingresar los coeficientes del polinomio y sus casos base\.\n
            Ejemplo:\n
            /cbase \[1,\-2,\-1,2\]\;\[0,1,2\]


            \- /mkovv:  
            Modelo predictivo de markov; proporcionar link 
            de sitio web\.
            Ejemplo: /mkovv https://\.\.\.
            
            \- /graff:  
            Generar un grafo simple no dirigido, indicar número
            de aristas, vertices y grado máximo\.
            Ejemplo: /graff 1\, 2\, 3
                        
                
                Para mas información, consultar mi documentación\!       
            """

        update.message.reply_text(msg, parse_mode='MarkdownV2')


    #ECUACIÓN DE RECURRENCIA LHCC   
    def lhcc(self, update, context):
        uname = update.message.chat.username
        logger.info(f"El usuario {uname} ha solicitado una RRLHCC...")
        text = update.message.text
        text = text.replace("/lhcc", "").strip()
        try:
            res=eval(text); 
            err=play.play_RRLHCC(res); print(err)
            if (err != ""):
                update.message.reply_text(err)
            else:
                update.message.reply_text("""
                Markov: 
                Esta es la relación re recurrencia generada:\n
                """)
                img = open("src/rrlhcc.png", "rb")
                chat_id = update.message.chat.id
                update.message.bot.sendPhoto(chat_id=chat_id, photo=img)
                img.close()
        except Exception as e:
            print(e)
            logger.info("Error: Revisar parametros de la secuencia...")
            update.message.reply_text(
                "Markov:\nParece que ha habido un error, revisa\n los parametros de nuevo...")

       
    #CASOS BASES
    def cbase(self, update, context):
        uname= update.message.chat.username
        logger.info(f"El usuario {uname} solició casos bases")
        text = update.message.text         
        text = str(text.replace("/cbase","").strip())
        text = (''.join(x for x in text)).split(";")
        new= []
        for i in range(len(text)): new.append(eval(text[i]))
        try:
            res = play.play_CBASE(np.array(new[0]), np.array(new[1]), 0) 
        
            update.message.reply_text(f"""
            Markov: 
            Esta es la ecuación final aplicando sus casos base:
            {res}
            """)
            img = open("src/cbase.png", "rb")
            chat_id = update.message.chat.id
            update.message.bot.sendPhoto(chat_id=chat_id, photo=img)
            
        except Exception as e:
            print(e)
            logger.info("Error: Revisar los parametros de la secuencia...")
            update.message.reply_text("Markov:\n Ha habido un error, revisa nuevamente los parametros\n...")

    #MODELO DE MARKOV PARA PREDICCIÓN DE TEXTO
    def mkovv(self, update, context):
        uname = update.message.chat.username
        logger.info(f"El usuario {uname} ha solicitado markov...")
        info = update.message.text
        info = info.replace("/mkovv", "").strip() #obtener link
        chat_id=update.message.chat.id
        
        try: 
            text = play.play_markv(info)
            print("here---")
            update.message.reply_text(f"""
            Markov: 
            Hola de nuevo!, Este es el texto generado de la url \n{info}:

            "{text}"

            Si desea visualizaro completo, consulte el siguiente documento:
            """)
            doc = open("src/gtext.txt")
            update.message.bot.sendDocument(chat_id=chat_id, document=doc, timeout=400)
            doc.close()
        except Exception as e:
            logger.info("Error: Intente con otra url o revise los comandos...")
            print(e)
            update.message.reply_text("Markov: \nOps!, Parece que ha habido un error, intenta con otra url\n o revisa los parametros...")

    #GENERADOR DE GRAFOS
    def graff(self, update, context):
        uname = update.message.chat.username
        logger.info(f"El usuario {uname} solició dibujar un grafo...")
        info = update.message.text 
        info = info.replace("/graff", "").strip()#Reemplazar y quitar espacios en blanco 
        
        try:
            vals = eval(info)
            if len (vals)>3:
                update.message.reply_text("Markov: \nHay un error en sus parametros, revise e intente")
            else:
                vert = vals[0]
                arist = vals[1]
                grad = vals[2]
                
                play.play_graph(vert, arist, grad)
                img=open("src/nodo.png", 'rb')
                chat_id= update.message.chat.id
                update.message.reply_text("Cargando grafo...")
                update.message.bot.sendPhoto(chat_id=chat_id, photo=img)
                update.message.reply_text(f"Aristas: {arist}, Vertices: {vert}, Grado: {grad}")
                img.close()

        except Exception as e:
            logger.info("Error: No se puede generar el grafo...")
            print(e)
            update.message.reply_text("Markov: \nOps!, Parece que ha habido un error, verifica los parametros...")
        

           
    