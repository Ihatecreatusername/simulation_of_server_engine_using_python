#-*- coding:utf-8 -*-
import task

class SubTask(task.CTask):
    def __init__(self, sName):
        super().__init__(sName)

    def OnCall(self):
        OnCall()

    def TestOP(self, iOP):
        if iOP == 100:
            return "test in task"
        return super().TestOP(iOP)

def OnCall():   #when update, function can be transformed to new function, but that situation cannot work on class equally.
    pass
