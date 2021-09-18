#-*- coding:utf-8 -*-
import log

__all__ = ['man', 'showall', 'quit', 'update']

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
