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
import resources.libs.favourites as favourites

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def add_Channel(idChannel,nameChannel,label):
    url = build_url({'mode': 'folder', 'channel': idChannel, 'param':'none'})
    li = xbmcgui.ListItem(label, iconImage=os.path.join( globalvar.MEDIA, nameChannel+".png"))
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)
        
def notify(text,channel):
    time = 3000  #in miliseconds 
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('FReplay',text, time, os.path.join( globalvar.MEDIA, globalvar.channels[channel][1]+".png")))

    
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
        for chan,folder_param, folder_title, folder_icon, mode in globalvar.channels[channel][3].list_shows(channel,param):
            url = build_url({'mode': mode, 'channel': chan, 'param':folder_param})
            li = xbmcgui.ListItem(folder_title, iconImage='DefaultFolder.png')
            #Contextual Menu
            li.addContextMenuItems([], replaceItems=True)
            if mode=='shows' and channel!=0:
                li.addContextMenuItems([ ('Add to FReplay Favourites', 'XBMC.RunPlugin(%s?mode=bkm&action=add&channel=%s&param=%s&display=%s)' % (sys.argv[0],chan,folder_param,folder_title)),
                         ], replaceItems=True)
            if mode=='shows' and channel==0:
                li.addContextMenuItems([ ('Remove from Favourites', 'XBMC.RunPlugin(%s?mode=bkm&action=rem&channel=%s&param=%s&display=%s)' % (sys.argv[0],chan,folder_param,folder_title)),
                         ], replaceItems=True)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)
    elif mode[0]=='shows':
        for video_url, video_title, video_icon in globalvar.channels[channel][3].list_videos(channel,param):
            li = xbmcgui.ListItem(video_title, iconImage=video_icon,thumbnailImage=video_icon)
            li.setInfo( type='Video', infoLabels={ "Title": video_title } )            
            li.setProperty('IsPlayable', 'true')
            li.addContextMenuItems([ ('Download', 'XBMC.RunPlugin(%s?mode=dl&channel=%s&param=%s&name=%s)' % (sys.argv[0],200,video_url.encode('utf-8'),video_title)),
                         ], replaceItems=True)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=video_url,listitem=li, isFolder=False)
            xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_NONE)
            xbmcplugin.setPluginCategory(addon_handle, 'show' )
            xbmcplugin.setContent(addon_handle, 'movies')
    elif mode[0]=='bkm':
        if args['action'][0]=='add':#Add to Favourites
            display = args['display'][0]
            result=favourites.add_favourite(channel,param,display)
        else:
            result=favourites.rem_favourite(channel,param)
        notify(result,channel)
    elif mode[0]=='dl':
        name = args['name'][0]
        url = args['param'][0]
        utils.download_video(name, url)
    xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True, updateListing=False)