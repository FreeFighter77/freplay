import sys
import os, os.path
import urllib
import urlparse

import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon

import resources.libs.globalvar as globalvar
import resources.libs.utils as utils

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'tvshows')

def build_url(query):
    print query
    return base_url + '?' + urllib.urlencode(query)

def add_Channel(idChannel,nameChannel,label):
    url = build_url({'mode': 'folder', 'channel': idChannel, 'param':'none'})
    li = xbmcgui.ListItem(label, iconImage=os.path.join( globalvar.MEDIA, nameChannel+".png"))
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)
    
mode = args.get('mode', None)

utils.init()

if mode is None:
    utils.firstRun()
    for item in globalvar.channels:        
            add_Channel(item[0],item[1],item[2])

    xbmcplugin.endOfDirectory(addon_handle)
else:    
    channel = int(args['channel'][0])
    param = args['param'][0]
    if globalvar.REMOTE_DBG:
        print 'FReplay:'+'mode='+mode[0]+' | channel=' + str(channel)+' | param=' + param
    if mode[0]=='folder':
        for folder_param, folder_title, folder_icon, mode in globalvar.channels[channel][3].list_shows(channel,param):
            url = build_url({'mode': mode, 'channel': channel, 'param':folder_param})
            li = xbmcgui.ListItem(folder_title, iconImage='DefaultFolder.png')
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)
    else:
        for video_url, video_title, video_icon in globalvar.channels[channel][3].list_videos(channel,param):
            li = xbmcgui.ListItem(video_title, iconImage=video_icon,thumbnailImage=video_icon)
            li.setInfo( type='Video', infoLabels={ "Title": video_title } )
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=video_url,listitem=li, isFolder=False)
        
    xbmcplugin.endOfDirectory(addon_handle)