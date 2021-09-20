#-*- coding:utf-8 -*-
import os
import time
import platform
import traceback

def Init():
    if not os.path.exists("log"):
        os.mkdir("log")

def log_file(sFile, sLog):
    fi = open("log/" + sFile + ".txt", "a+")
    fi.write(time.strftime("[%Y%m%d %H:%M:%S]", time.localtime()) + sLog + '\n')
    fi.close()

def StdErrLog():
    msg = traceback.format_exc()
    log_file("err", msg)
    if platform.system() == "Windows":
        print(msg)

