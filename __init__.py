#-*- coding:utf-8 -*-
import traceback
import log

def OnlineUpdate(sCommand):
    sModule = sCommand.split(" ")[1]
    import update
    log.log_file("update", "update_version %s: %s" % (update.g_Version, sCommand))
    update.g_Version += 1

    exec("""
import importlib

import update
importlib.reload(update)

import %s
update.UpdateCallBefore()
importlib.reload(%s)
update.UpdateCallBack()

""" % (sModule, sModule))

def Quit(sCommand):
    log.log_file("start", "quit")
    import os
    import signal
    os.kill(os.getpid(), signal.SIGINT)

if __name__ == "__main__":
    log.Init()
    log.log_file("start", "start")

    dCommandHandleFunc = {
        "update"    :   OnlineUpdate,
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

