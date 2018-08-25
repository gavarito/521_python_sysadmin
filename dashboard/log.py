#!/usr/bin/python3

import logging

logging.basicConfig(
    filename= 'app.log',
    level= logging.DEBUG,
    format="%(asctime)s [ %(levelname)s ] %(name)s\n \
            [ %(funcName)s ] [ %(filename)s, %(lineno)s] %(message)s",
    datefmt="[ %d/%m/%Y %H:%M:%S ]"
)
CUSTOM = 49
logging.addLevelName(CUSTOM, 'MEULOG')
def alert(self, message, *args, **kwargs):
    if self.isEnabledFor(CUSTOM):
        self._log(CUSTOM, message, args, kwargs)

logging.Logger.custom = alert
logger = logging.getLogger()
logger.custom("Mensagem de log custom")

# logging.debug("mensagem de debug")
# logging.info("mensagem de info")
# logging.warning("mensagem de warning")
# logging.error("mensagem de error")
# logging.critical("mensagem de critical")