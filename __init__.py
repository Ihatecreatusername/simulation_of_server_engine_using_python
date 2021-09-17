#-*- coding:utf-8 -*-
import traceback
import log
import platform

def Quit(sCommand):
    log.log_file("system", "quit")
    import os
    import signal
    os.kill(os.getpid(), signal.SIGINT)

if __name__ == "__main__":
    log.Init()
    log.log_file("system", "system start")

    import update
    import task
    
    task.Init()

    if platform.system() == "Windows":
        import mywatchdog
        mywatchdog.Init()

    log.log_file("system", "system init done")

    dCommandHandleFunc = {
        "update"    :   update.UpdateOnce,
        "quit"      :   Quit,
    }

    while True:
        try:
            sCommand = input()
            lstCommand = sCommand.split(" ")
            oFunc = dCommandHandleFunc.get(lstCommand[0])
            if oFunc:
                oFunc(sCommand)
        except:
            msg = traceback.format_exc()
            print(msg)
            log.log_file("err", msg)

