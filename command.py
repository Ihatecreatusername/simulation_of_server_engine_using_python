#-*- coding:utf-8 -*-
import platform
import log

__all__ = ['man', 'showall', 'quit', 'update', 'readcommand']

def _stdout(func):
    def wrapstdout(*arg, **kwargs):
        sResult = func(*arg, **kwargs)
        if sResult:
            print(sResult)
    return wrapstdout

@_stdout
def man(sCommand):
    """
    example:
        man update
        man showall
    """
    import command
    sFunc = sCommand.split(" ")[1]
    if sFunc not in command.__all__:
        return "no function found"
    return getattr(command, sFunc).__doc__
    
@_stdout
def showall(sCommand):
    """
    show all avaliable function
    """
    import command
    return command.__all__

def quit(sCommand):
    """
    kill process
    example:    quit
    """
    log.log_file("system", "quit")
    import os
    import signal
    os.kill(os.getpid(), signal.SIGINT)

def update(sCommand):
    """
    update module
    example:    update 0 task.test
    """
    import update
    update.UpdateOnce(sCommand)

def readcommand():
    """
    read command from file
    """
    import pandas
    if platform.system() == "Windows":
        #read from input
        sCommand = input()
        sWriteInfo = pandas.DataFrame([['admin',sCommand],], columns=['userid', 'command'])
        sWriteInfo.to_csv('command.csv', index=False)
    try:
        lstcommand = pandas.read_csv('command.csv')
    except FileNotFoundError:
        return
    result = []
    for i in range(len(lstcommand)):
        sUser, sCommand = lstcommand['userid'][i], lstcommand['command'][i]
        log.log_file("command", "read {0} {1}".format(sUser, sCommand))
        result.append((sUser, sCommand))

    if result:
        sWriteInfo = pandas.DataFrame(None, columns=['userid', 'command'])
        sWriteInfo.to_csv('command.csv', index=False)
    return result

