#-*- coding:utf-8 -*-
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import log
import update

if "g_WatchdogCount" not in globals():
    g_WatchdogCount = 0

class FileEventHandler(FileSystemEventHandler):
    def on_moved(self, event):
        pass

    def on_created(self, event):
        pass

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        if event.src_path[-3:] != ".py":
            log.log_file("update", "fail auto update {0}".format(event.src_path))
            return
        global g_WatchdogCount
        if g_WatchdogCount % 2: #watchdog 检测修改会检测备份文件，所以会操作更新两次
            sFile = event.src_path[:-3].replace("./", "")
            sFile = sFile.replace("\\", ".")
            log.log_file("update", "auto update {0}".format(sFile))
            update.UpdateModule(sFile)
        g_WatchdogCount += 1

def Init():
    log.log_file("system", "mywatchdog init done")

    observer = Observer()
    dirs = [r'./task',]
    for sDir in dirs:
        event_handler = FileEventHandler()
        observer.schedule(event_handler, sDir, True)
    observer.start()
