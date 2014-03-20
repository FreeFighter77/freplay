import urllib2
import CommonFunctions
common = CommonFunctions
from xml.dom import minidom
import globalvar

url_base='http://videos.arte.tv/fr/do_delegate/videos/index--3188626,view,videoSitemap.xml' 

def fix_text(text):
    return text.replace('&amp;','&').encode('utf-8')

def list_shows(channel,folder):
    shows=[]
    d=dict()
    
    if folder=='none':
        xml = urllib2.urlopen(url_base).read()
        url=common.parseDOM(xml, "url")
        for i in range(0, len(url)):
            categoryTab=common.parseDOM(url[i], "video:category")
            if len(categoryTab)>0:
                category=fix_text(categoryTab[0])
                if category not in d:
                    shows.append( [channel,category,category,'','folder'] )
                    d[category]=category
    else:
        xml = urllib2.urlopen(url_base).read()
        url=common.parseDOM(xml, "url")
        for i in range(0, len(url)):
            titleTab=common.parseDOM(url[i], "video:title")
            if len(titleTab)>0:
                title=fix_text(titleTab[0])
            categoryTab=common.parseDOM(url[i], "video:category")
            if len(categoryTab)>0:
                if(fix_text(categoryTab[0])==folder and title not in d):                   
                    shows.append( [channel,title,title,'','shows'] )
                    d[title]=title
    return shows
def getURLVideo(url):
    url=urllib2.unquote(url[url.index('videorefFileUrl')+16:]).decode('utf8')
    xml = urllib2.urlopen(url).read()
    xmldoc = minidom.parseString(xml)
    itemlist = xmldoc.getElementsByTagName('video') 
    for s in itemlist :
        if s.attributes['lang'].value==globalvar.LANG:
            url=s.attributes['ref'].value
    xml = urllib2.urlopen(url).read()   
    xmldoc = minidom.parseString(xml)     
    urlslist = xmldoc.getElementsByTagName('urls')
    for urls in urlslist :
        itemlist = urls.getElementsByTagName('url') 
        for s in itemlist :
            if s.attributes['quality'].value==globalvar.QLTY:
                url=s.firstChild.data
    return url
    
def list_videos(channel,show_title):
    videos=[]
    xml = urllib2.urlopen(url_base).read()
    url=common.parseDOM(xml, "url")
    for i in range(0, len(url)):      
        video_url=''
        name=''
        image_url=''
        date=''
        duration=''
        views=''
        desc=''
        rating=''
        url_vidTab=common.parseDOM(url[i], "video:player_loc")
        if len(url_vidTab)>0:
            video_url=url_vidTab[0]
        descriptionTab=common.parseDOM(url[i], "video:description")
        if len(descriptionTab)>0:
            name=fix_text(descriptionTab[0])
        picTab=common.parseDOM(url[i], "video:thumbnail_loc")
        if len(picTab)>0:
            image_url=picTab[0]
        titleTab=common.parseDOM(url[i], "video:title")
        if len(titleTab)>0:
            title=fix_text(titleTab[0])
        if(title==show_title):          
            videos.append( [getURLVideo(video_url), name, image_url] )
    return videos