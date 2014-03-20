import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon

import os

REMOTE_DBG=False
ADDON_NAME='plugin.video.freplay'
ADDON     = xbmcaddon.Addon(ADDON_NAME)
SETTINGS  = ADDON
LANGUAGE  = ADDON.getLocalizedString
ADDON_DIR = ADDON.getAddonInfo( "path" )
RESOURCES = os.path.join( ADDON_DIR, "resources" )
MEDIA     = os.path.join( RESOURCES, "media")
ADDON_DATA= xbmc.translatePath( "special://profile/addon_data/%s/" % ADDON_NAME )
CACHE_DIR = os.path.join( ADDON_DATA, "cache")
FAVOURITES_FILE = os.path.join( ADDON_DATA, "favourites.json")

LANG='fr'
QLTY='hd'

dirCheckList        = (CACHE_DIR,)
channels=[]

