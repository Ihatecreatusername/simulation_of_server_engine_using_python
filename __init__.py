#-*- coding:utf-8 -*-
import traceback
import platform

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
            sCommand = input()
            lstCommand = sCommand.split(" ")
            oFunc = getattr(command, lstCommand[0])
            if oFunc:
                oFunc(sCommand)
        except:
            msg = traceback.format_exc()
            print(msg)
            log.log_file("err", msg)

