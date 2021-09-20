#-*- coding:utf-8 -*-
import time
import threading

import log

if "g_Manager" not in globals():
    g_Manager = None

class CManager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.m_Item = {}

    def AddItem(self, sName, obj):
        self.m_Item[sName] = obj

    def DelItem(self, sName):
        if sName not in self.m_Item:
            return None
        obj = self.m_Item[sName]
        del self.m_Item[sName]
        return obj

    def run(self):
        while True:
            time.sleep(5)
            self.OnCall()

    def OnCall(self):
        for sTaskName in self.m_Item:
            try:
                self.m_Item[sTaskName].OnCall()
            except:
                log.StdErrLog()

class CTask(object):
    def __init__(self, sName):
        self.m_Name = sName
    
    def OnCall(self):
        pass

    def TestOP(self, iOP):
        if iOP == 100:
            return """
101-show all tasks
"""
        elif iOP == 101:
            pass

        return "illegal optional id"

def Init():
    global g_Manager
    if g_Manager:
        return
    g_Manager = CManager()
    g_Manager.setDaemon(True)

    import task.test

    g_Manager.AddItem("test", task.test.SubTask("test"))

    g_Manager.start()
    log.log_file("system", "task moudle done")


