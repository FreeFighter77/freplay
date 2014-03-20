import urllib
import xml.dom.minidom

url_base='http://replay.gulli.fr/layout/set/rss/RSS'
def list_shows(channel,folder):
    shows=[]
    d=dict()
    dom = xml.dom.minidom.parse(urllib.urlopen(url_base))
    ITEM=dom.getElementsByTagName('item')
    for nodeITEM in ITEM:
        TITLE=nodeITEM.getElementsByTagName('title')
        for nodeTITLE in TITLE:
                title= nodeTITLE.firstChild.data.encode('utf-8')
                title=title[:title.index(' - ')]
                if title not in d:
                    shows.append( [channel,title,title,'','shows'] )
                    d[title]=title        
    return shows
        
def list_videos(channel,show_title):
    videos=[] 
    dom = xml.dom.minidom.parse(urllib.urlopen(url_base))
    ITEM=dom.getElementsByTagName('item')
    for nodeITEM in ITEM:
        TITLE=nodeITEM.getElementsByTagName('title')
        for nodeTITLE in TITLE:
                title= nodeTITLE.firstChild.data.encode('utf-8')
                title=title[:title.index(' - ')]
                if title == show_title:
                    subtitle=nodeTITLE.firstChild.data.encode('utf-8')
                    subtitle=subtitle[subtitle.index(' - ')+3:]
                    LINK=nodeITEM.getElementsByTagName('title')
                    for nodeLINK in LINK:
                            url= nodeLINK.firstChild.data.encode('utf-8')
                    videos.append( [url, subtitle, ''] )
    return videos