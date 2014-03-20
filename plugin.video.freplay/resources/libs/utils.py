import globalvar
import cplus
import pluzz
import arte
import favourites
import gulli

import os
import sys
import SimpleDownloader as simpledownloader

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
            [0, 'favourites', 'Favourites', favourites],
            [1, 'cplus', 'Canal +', cplus],
            [2, 'france1', 'France 1ere', pluzz],
            [3, 'france2', 'France 2', pluzz],
            [4, 'france3', 'France 3', pluzz],
            [5, 'france4', 'France 4', pluzz],
            [6, 'france5', 'France 5', pluzz],
            [7, 'franceO', 'France O', pluzz],
            [8, 'arte', 'Arte', arte],
            [9, 'gulli', 'Gulli', gulli]
            ]    
            
def firstRun():
    if not os.path.exists(globalvar.CACHE_DIR) :
        os.makedirs(globalvar.CACHE_DIR, mode=0777)
        
def download_video(name, url):
    downloader = simpledownloader.SimpleDownloader()
    
    params = { "url": url, "download_path": globalvar.CACHE_DIR }
    downloader.download('test', params)