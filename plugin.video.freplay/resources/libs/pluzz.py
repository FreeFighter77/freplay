import zipfile
import simplejson as json
import globalvar
import os.path
import urllib

CATALOG_PATH        = os.path.join(globalvar.CACHE_DIR,'PluzzMobileCatalog.zip')
jsonmobilecatalog   = "http://webservices.francetelevisions.fr/catchup/flux/flux_main.zip"
catalogconffilename = "message_FT.json"
catalogcatfilename  = "categories.json"

def list_shows(channel,folder):
    shows=[]
    if folder=='none':
        if os.path.exists(CATALOG_PATH):
            os.remove(CATALOG_PATH)
        urllib.urlretrieve(jsonmobilecatalog,CATALOG_PATH)
        zf          = zipfile.ZipFile(CATALOG_PATH)
        data        = zf.read(catalogcatfilename)
        jsoncat     = json.loads(data.decode('iso-8859-1'))
        categories  = jsoncat['categories']
        for cat in categories :
            shows.append( [cat['titre'].encode('utf-8'), cat['titre'].encode('utf-8'),'','folder'] )
        return shows
    
    
def list_videos(channel,show_title):
    videos=[] 
    return videos