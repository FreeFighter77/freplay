import urllib2
import CommonFunctions
common = CommonFunctions

url_base='http://videos.arte.tv/fr/do_delegate/videos/index--3188626,view,videoSitemap.xml' 

def fix_text(text):
    return text.replace(u'\xe9','e').replace('&amp;','&').replace('&#039;','\'').replace(u'\xe8','e')

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
                    shows.append( [category,category,'','folder'] )
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
                    shows.append( [title,title,'','shows'] )
                    d[title]=title
    return shows
    
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
            video_url=fix_text(url_vidTab[0])
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
            videos.append( [video_url, name, image_url] )
            print video_url
    return videos