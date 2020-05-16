import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    return update.message.reply_text("Hola, Geeks!")


def help(update, context):
    return update.message.reply_text("Ayudame!")


def mayus(update, context):
    texto = context.args[0]
    return str(texto).upper()


def alreves(update, context):
    texto = update.message.text
    return texto[::-1]


def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Inicio del Bot"""
    # Colocamos el Token creado por FatherBot
    updater = Updater(
        "1211838854:AAFF-Sdhu6PEbniA4XQtkXM20bHce7E1Bu8", use_context=True)

    # Es el Registro de Comandos a través del dispartcher

    updater.dispatcher.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
