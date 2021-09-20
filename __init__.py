#-*- coding:utf-8 -*-
import platform
import time

from numpy.lib.function_base import sort_complex

import log
import command

def Quit(sCommand):
    log.log_file("system", "quit")
    import os
    import signal
    os.kill(os.getpid(), signal.SIGINT)

if __name__ == "__main__":
    log.Init()
    log.log_file("system", "system start")

    import task
    
    task.Init()

    if platform.system() == "Windows":
        import mywatchdog
        mywatchdog.Init()

    log.log_file("system", "system init done")

    while True:
        try:
            lstWaiting = command.readcommand()
            if lstWaiting:
                for sUser, sCommand in lstWaiting:
                    lstCommand = sCommand.split(" ")
                    oFunc = getattr(command, lstCommand[0])
                    if oFunc:
                        log.log_file("command", "{0} exec: {1}".format(sUser, sCommand))
                        oFunc(sCommand)
        except:
            log.StdErrLog()
        time.sleep(0.1)

