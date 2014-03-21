import zipfile
import simplejson as json
import globalvar
import os.path
import urllib

CATALOG_PATH        = os.path.join(globalvar.CACHE_DIR,'PluzzMobileCatalog.zip')
jsonmobilecatalog   = "http://webservices.francetelevisions.fr/catchup/flux/flux_main.zip"
catalogconffilename = "message_FT.json"
catalogcatfilename  = "categories.json"
url_base_videos= "http://medias2.francetv.fr/catchup-mobile"
url_base_images= "http://www.pluzz.fr"
    
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
            shows.append( [channel,cat['titre'].encode('utf-8'), cat['titre'].encode('utf-8'),'','folder'] )
    else:
        zf          = zipfile.ZipFile(CATALOG_PATH)
        data        = zf.read('catch_up_' + globalvar.channels[channel][1] + '.json')
        jsoncatalog = json.loads(data)
        programmes  = jsoncatalog['programmes']
        d=dict()
        for programme in programmes :
            video_cat = programme['rubrique'].encode("utf-8")
            if video_cat == folder:
                video_name  = programme['titre'].encode("utf-8")
                if video_name not in d :
                    d[video_name]=video_name
                    video_url   = ''
                    video_image = ''
                    video_infos = {}
                    if programme['accroche'] :
                        video_infos['Plot']  = programme['accroche'].encode("utf-8")
                    if programme['realisateurs'] :
                        video_infos['Cast']      = programme['acteurs'].encode("utf-8")
                    if programme['realisateurs'] :
                        video_infos['Director']  = programme['realisateurs'].encode("utf-8")
                    if programme['format'] :
                        video_infos['Genre']     = programme['format'].encode("utf-8")
                    shows.append( [channel,video_name,video_name,'','shows'] )
    return shows    

def getVideoURL(channel,video_URL):
    return video_URL

def list_videos(channel,show_title):
    videos=[] 
    
    zf          = zipfile.ZipFile(CATALOG_PATH)
    data        = zf.read('catch_up_' + globalvar.channels[channel][1] + '.json')
    jsoncatalog = json.loads(data)
    programmes  = jsoncatalog['programmes']
    for programme in programmes :
        video_name  = programme['titre'].encode("utf-8")
        if video_name == show_title : 
            if programme['sous_titre'] != "" :
                video_name  = video_name +' : '+programme['sous_titre'].encode("utf-8") 
            video_url   = url_base_videos+programme['url_video'].encode("utf-8")
            video_image = url_base_images+programme['url_image_racine'].encode("utf-8")+'.'+programme['extension_image'].encode("utf-8")
            video_infos = {}
            if programme['accroche'] :
                video_infos['Plot']      = programme['accroche'].encode("utf-8")
            if programme['realisateurs'] :
                video_infos['Cast']      = programme['acteurs'].encode("utf-8")
            if programme['realisateurs'] :
                video_infos['Director']  = programme['realisateurs'].encode("utf-8")
            if programme['rubrique']:
                video_infos['Genre'] = programme['rubrique'].encode("utf-8")
            if programme['format'] != '' :
                video_infos['Genre']     = video_infos['Genre']+' - '+programme['format'].encode("utf-8")
            if programme['genre_simplifie'] != '' :
                video_infos['Genre']     = video_infos['Genre']+' - '+programme['genre_simplifie'].encode("utf-8")
            if programme['duree'] :
                video_infos['Duration']  = programme['duree'].encode("utf-8")
            if programme['date'] :
                video_infos['Year']      = int(programme['date'].split('-')[0].encode("utf-8"))
                video_infos['Date']      = str(programme['date'].split('-')[2])+'-'+str(programme['date'].split('-')[1])+'-'+str(programme['date'].split('-')[0])
                video_infos['Premiered'] = video_infos['Date'] 
                video_name               = video_name+" : "+video_infos['Date']
            videos.append( [video_url, video_name, video_image] )

    
    return videos