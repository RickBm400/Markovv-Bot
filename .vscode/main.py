from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
from markbot import Bot

load_dotenv()
TOKEN=os.environ.get("TOKEN")


#main function
def main():
    #establecer conexión 
    #print(TOKEN)
    updater = Updater(TOKEN, use_context=True) #Ingresar Token del bot
    dp = updater.dispatcher #Despachador de solicitudes

    #instanciar objeto bot 
    bot = Bot()

    #Establecer comandos 
    dp.add_handler(CommandHandler("start", bot.start))
    dp.add_handler(CommandHandler("help", bot.help))
    dp.add_handler(CommandHandler("lhcc", bot.lhcc))
    dp.add_handler(CommandHandler("cbase", bot.cbase))
    dp.add_handler(CommandHandler("mkovv", bot.mkovv))
    dp.add_handler(CommandHandler("graff", bot.graff))
    
    #Iniciar Bot, escuchar las peticiones del server 
    updater.start_polling()#preguntar si el servidor recibió cambios
    #Mantener el bot ejecutandose hasta que ocurra una interrupción 
    updater.idle()
    


#main code 
if __name__=='__main__':
    main()