import urllib
import xml.dom.minidom

def list_shows(channel,folder):
    shows=[]
    
    if folder=='none':
        shows.append( [channel,'emissions', 'Emissions','','folder'] )
        shows.append( [channel,'infodoc', 'Info Doc','','folder'] )
        shows.append( [channel,'humour', 'Humour','','folder'] )
        shows.append( [channel,'excluweb', 'Les Exclus du Web','','folder'] )
    
    if folder=='emissions':
        shows.append( [channel,'nouvelle edition', 'La Nouvelle Edition','','shows'] )
        shows.append( [channel,'before', 'Le Before LGJ','','shows'] )
        shows.append( [channel,'grand journal', 'Le Grand Journal','','shows'] )
        shows.append( [channel,'Petit Journal', 'Le Petit Journal','','shows'] )
        shows.append( [channel,'Le Supplement', 'Le Supplement','','shows'] )
        shows.append( [channel,'Le Tube', 'Le Tube','','shows'] )
        shows.append( [channel,'Les Guignols', 'Les Guignols','','shows'] )
        shows.append( [channel,'Made in Groland', 'Made in Groland','','shows'] )
        shows.append( [channel,'salut terriens', 'Salut Les Terriens','','shows'] )
        shows.append( [channel,'Zapping', 'Zapping','','shows'] )
        shows.append( [channel,'Annee Zapping partie', 'Annee du Zapping','','shows'] )
        
    if folder=='infodoc':
        shows.append( [channel,'Journal des Jeux Video', 'Journal des Jeux Video','','shows'] )
        shows.append( [channel,'Effet papillon', 'Effet Papillon','','shows'] )
        shows.append( [channel,'Le chiffroscope', 'Le chiffroscope','','shows'] )
        shows.append( [channel,'Le JT de CANAL+', 'Le JT de CANAL+','','shows'] )
        shows.append( [channel,'Les Nouveaux Explorateurs', 'Les Nouveaux Explorateurs','','shows'] )
        shows.append( [channel,'Oeil De Links', 'Oeil De Links','','shows'] )
        shows.append( [channel,'Made in France', 'Made in France','','shows'] )
        shows.append( [channel,'Special Investigation', 'Special Investigation','','shows'] )
        
    if folder=='humour':
        shows.append( [channel,'Castings', 'Castings','','shows'] )
        shows.append( [channel,'Catherine et Liliane', 'Catherine et Liliane','','shows'] )
        shows.append( [channel,'Connasse', 'Connasse','','shows'] )
        shows.append( [channel,'Gaspard Proust', 'Gaspard Proust','','shows'] )
        shows.append( [channel,'Dans la bouche', 'Dans la bouche','','shows'] )
        shows.append( [channel,'Eric et Quentin', 'Eric et Quentin','','shows'] )
        shows.append( [channel,'instant Barre', 'instant Barre','','shows'] )
        shows.append( [channel,'La meteo de Doria', 'La meteo de Doria','','shows'] )
        shows.append( [channel,'Le defi Musqua', 'Le defi Musqua','','shows'] )
        shows.append( [channel,'Le Dezapping', 'Le Dezapping','','shows'] )
        shows.append( [channel,'Les Tutos', 'Les Tutos','','shows'] )
        shows.append( [channel,'Oh-Oh de Nora', 'Oh-Oh de Nora','','shows'] )
        shows.append( [channel,'Pendant ce temps', 'Pendant ce temps','','shows'] )
        shows.append( [channel,'Vice-Versa', 'Vice-Versa','','shows'] )
        shows.append( [channel,'Jamel Comedy Club', 'Jamel Comedy Club','','shows'] )
        
    if folder=='excluweb':
        shows.append( [channel,'Clique Playlist', 'Clique Playlist','','shows'] )
        shows.append( [channel,'oeil de Molkhou', 'oeil de Molkhou','','shows'] )
        shows.append( [channel,'Le Boucan', 'Le Boucan de CANAL+','','shows'] )
        shows.append( [channel,'Le Meilleur du Hier', 'Le Meilleur du Hier','','shows'] )
        shows.append( [channel,'Les Kassos', 'Les Kassos','','shows'] )
        shows.append( [channel,'Pepites sur le net', 'Pepites sur le net','','shows'] )
        shows.append( [channel,'Tweet en clair', 'Tweet en clair','','shows'] )

    return shows

def find_categIDs(): 
    srubrique=''
    sunivers=''
    bUnique=True
    sCateg=''
    url_base='http://service.canal-plus.com/video/rest/getMEAs/cplus/'
    
    for i in range(0,1000):
        if bUnique:
            print sCateg
        bUnique=True
        bFirstPass=True
        dom = xml.dom.minidom.parse(urllib.urlopen(url_base+str(i)))
        VIDEO=dom.getElementsByTagName('MEA')
        for nodeVIDEO in VIDEO:
            RUBRIQUAGE=nodeVIDEO.getElementsByTagName('RUBRIQUAGE')
            for nodeRUBRIQUAGE in RUBRIQUAGE:
                RUBRIQUE=nodeRUBRIQUAGE.getElementsByTagName('RUBRIQUE')
                for nodeRUBRIQUE in RUBRIQUE:
                    srubrique= nodeRUBRIQUE.firstChild.data 
                UNIVERS=nodeRUBRIQUAGE.getElementsByTagName('UNIVERS')
                for nodeUNIVERS in UNIVERS:
                    sunivers= nodeUNIVERS.firstChild.data  
            if bFirstPass:
                sCateg= str(i) + '||' + sunivers + '==' + srubrique
                bFirstPass=False
            bUnique=(str(i) + '||' + sunivers + '==' + srubrique)

def url_exists(site):
    return site

def getVideoURL(channel,video_URL):
    return video_URL

def get_video_URL(VIDEOS,show):
    url=''
    bas_debit=''
    haut_debit=''
    hd=''    
    hls=''
    
    for nodeVIDEOS in VIDEOS:
        VIDEOFORMAT=nodeVIDEOS.getElementsByTagName('BAS_DEBIT')
        for nodeVIDEOFORMAT in VIDEOFORMAT:        
            try:   
                bas_debit=url_exists(nodeVIDEOFORMAT.firstChild.data)
            except:
                print 'No BAS_DEBIT'
    for nodeVIDEOS in VIDEOS:
        VIDEOFORMAT=nodeVIDEOS.getElementsByTagName('HAUT_DEBIT')
        for nodeVIDEOFORMAT in VIDEOFORMAT:        
            try:   
                haut_debit=url_exists(nodeVIDEOFORMAT.firstChild.data)
            except:
                print 'No HAUT_DEBIT'
    for nodeVIDEOS in VIDEOS:
        VIDEOFORMAT=nodeVIDEOS.getElementsByTagName('HD')
        for nodeVIDEOFORMAT in VIDEOFORMAT:        
            try:   
                hd=url_exists(nodeVIDEOFORMAT.firstChild.data)
            except:
                print 'No HD'
    for nodeVIDEOS in VIDEOS:
        VIDEOFORMAT=nodeVIDEOS.getElementsByTagName('HLS')
        for nodeVIDEOFORMAT in VIDEOFORMAT:        
            try:   
                hls=url_exists(nodeVIDEOFORMAT.firstChild.data)
            except:
                print 'No HLS'
    if hls!='':
        url=hls
    if bas_debit!='':
        url=bas_debit
    if haut_debit!='':
        url=haut_debit
    if hd!='':
        url=hd
    if show=='connasse':
        return hls
    else:
        return hd
            
def list_videos(channel,show_title):
    videos=[] 
    url_base='http://service.canal-plus.com/video/rest/search/cplus/'   
    dom = xml.dom.minidom.parse(urllib.urlopen(url_base+show_title))
    
    print url_base+show_title
    VIDEO=dom.getElementsByTagName('VIDEO')
    url=''
    title=''
    subtitle=''
    for nodeVIDEO in VIDEO:
        INFOS=nodeVIDEO.getElementsByTagName('INFOS')
        for nodeINFOS in INFOS:
            TITRAGE=nodeINFOS.getElementsByTagName('TITRAGE')
            for nodeTITRAGE in TITRAGE:
                TITRE=nodeTITRAGE.getElementsByTagName('TITRE')
                for nodeTITRE in TITRE:   
                    
                    try:         
                        title= nodeTITRE.firstChild.data
                    except:
                        print 'No Title'
                SOUS_TITRE=nodeVIDEO.getElementsByTagName('SOUS_TITRE')
                for nodeSSTITRE in SOUS_TITRE:      
                    
                    try:   
                        subtitle=' - ' + nodeSSTITRE.firstChild.data 
                    except:
                        print 'No subtitle'
        MEDIA=nodeVIDEO.getElementsByTagName('MEDIA')
        for nodeMEDIA in MEDIA:
            IMAGES=nodeMEDIA.getElementsByTagName('IMAGES')
            for nodeIMAGES in IMAGES:
                GRAND=nodeIMAGES.getElementsByTagName('GRAND')
                for nodeGRAND in GRAND:
                    icon=''
                    try:   
                        icon=nodeGRAND.firstChild.data
                    except:
                        print 'No icon'
            VIDEOS=nodeMEDIA.getElementsByTagName('VIDEOS')
            url=get_video_URL(VIDEOS,show_title)  
        
        videos.append( [url, title + subtitle, icon] )
    return videos

