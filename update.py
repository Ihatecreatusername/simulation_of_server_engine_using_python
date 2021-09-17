#-*- coding:utf-8 -*-

if "g_Version" not in globals():
    g_Version = 1

def UpdateCallBefore():
    pass

def UpdateCallBack():
    pass

def UpdateOnce(sCommand):
    sVersion = sCommand.split(" ")[1]
    import log
    if not sVersion.isdigit():
        log.log_file("update", "fail: illegal Version %s %s" % (sVersion, sCommand))
        return

    iVersion = int(sVersion)
    global g_Version
    if iVersion == 0:
        log.log_file("update", "no check version %s %s" % (g_Version, sCommand))
    else:
        if g_Version >= iVersion:
            log.log_file("update", "fail: g_Version %s >= Version %s %s" % (g_Version, iVersion, sCommand))
            return
        log.log_file("update", "update_version %s->%s: %s" % (g_Version, iVersion, sCommand))
        g_Version = iVersion
    sModule = sCommand.split(" ")[2]
    UpdateModule(sModule)

def UpdateModule(sModule):
    exec("""
import importlib

import update
importlib.reload(update)

import %s
update.UpdateCallBefore()
importlib.reload(%s)
update.UpdateCallBack()

""" % (sModule, sModule))

