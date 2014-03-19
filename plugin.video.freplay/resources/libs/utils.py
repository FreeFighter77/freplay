import globalvar
import cplus
import pluzz
import arte

import os
import sys

def init():
    # append pydev remote debugger
    if globalvar.REMOTE_DBG:
        # Make pydev debugger works for auto reload.
        # Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
        try:
            import pysrc.pydevd as pydevd
        # stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
            pydevd.settrace('localhost', stdoutToServer=True, stderrToServer=True)
        except ImportError:
            sys.stderr.write("Error: " +
                "You must add org.python.pydev.debug.pysrc to your PYTHONPATH.")

    
    globalvar.channels = [
            [0, 'cplus', 'Canal +', cplus],
            [1, 'france1', 'France 1ere', pluzz],
            [2, 'france2', 'France 2', pluzz],
            [3, 'france3', 'France 3', pluzz],
            [4, 'france4', 'France 4', pluzz],
            [5, 'france5', 'France 5', pluzz],
            [6, 'franceO', 'France O', pluzz],
            [7, 'arte', 'Arte', arte]
            ]
            
def firstRun():
    if not os.path.exists(globalvar.CACHE_DIR) :
        os.makedirs(globalvar.CACHE_DIR, mode=0777)