'''   321Movies   Copyright (C) 2017 The Mister   This program is free software: you can redistribute it and/or modify   it under the terms of the GNU General Public License as published by   the Free Software Foundation, either version 3 of the License, or   (at your option) any later version.   This program is distributed in the hope that it will be useful,   but WITHOUT ANY WARRANTY; without even the implied warranty of   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the   GNU General Public License for more details.   You should have received a copy of the GNU General Public License   along with this program.  If not, see <http://www.gnu.org/licenses/>.'''import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse,base64from t0mm0.common.addon import Addonfrom metahandler import metahandlersfrom resources.lib import repoCheckaddon_id = 'plugin.video.321Movies'selfAddon = xbmcaddon.Addon(id=addon_id)addon = Addon(addon_id, sys.argv)fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))next = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'next.png'))art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/images/'))BASEURL = selfAddon.getSetting('BASEURL')metaset = selfAddon.getSetting('enable_meta')def CATEGORIES():		repoCheck.UpdateRepo()		addDir('Search',BASEURL+'/index.php',3,art+'search.png',fanart)		addDir('Movies','http://ignorme',7,art+'movies.png',fanart)		addDir('TV Shows','http://ignorme',8,art+'tvshows.png',fanart)		xbmc.executebuiltin('Container.SetViewMode(50)')def TVSHOWINDEX():		addDir('All TV Shows',BASEURL+'/anime',2,art+'alltvshows.png',fanart) 		addDir('Recently Added Seasons',BASEURL+'/seasons',9,art+'recently.png',fanart) 		addDir('Recently Added Episode',BASEURL+'/episodes',200,art+'recently.png',fanart) 		addDir('Best Ratings',BASEURL+'/ratings?get=anime',2,art+'best.png',fanart) 		xbmc.executebuiltin('Container.SetViewMode(50)')				def MOVIESINDEX():		addDir('HD Movies',BASEURL+'/quality/hd',16,art+'hd.png',fanart) 		addDir('Movies',BASEURL+'/film',1,art+'movies.png',fanart) 		addDir('Trending Movies',BASEURL+'/trending',11,art+'trending.png',fanart)  		addDir('Genres',BASEURL,5,art+'genres.png',fanart) 		addDir('Realease Year',BASEURL,6,art+'release.png',fanart) 		addDir('Best Ratings',BASEURL+'/ratings?get=movies',1,art+'best.png',fanart)  		xbmc.executebuiltin('Container.SetViewMode(50)')def GETMOVIES(url):	metaset = selfAddon.getSetting('enable_meta')	link = open_url(url)	match=re.compile('<a href="([^"]+)"><img src="([^"]+)" alt="Watch ([^"]+) For Free"></a>[^"]+<div class="rating"><span class="icon-star2"></span> ([^"]+)</div>[^"]+<span class="quality">([^"]+)</span>',re.DOTALL).findall(link)	for url, img, name, rating, quality in match:			try:				name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-')				name = name + ":" + " " + "Quality:" + " " + "[COLOR dodgerblue]" + " " + quality + "[/COLOR]" + " " + "|" + " " + " " + "Rating:" "[COLOR dodgerblue]" + " " + rating + "[/COLOR]"				addDir(name,url,12,img,fanart)			except:pass	try:		np=re.compile("<link rel='next' href='(.+?)'", re.DOTALL | re.IGNORECASE).findall(link)[0]		name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'		addDir(name,np,1,next,fanart)	except:pass	xbmc.executebuiltin('Container.SetViewMode(50)')def GETHD(url):	metaset = selfAddon.getSetting('enable_meta')	link = open_url(url)	match=re.compile('<a href="([^"]+)".*?src="([^"]+)" alt="Watch ([^"]+) For Free".*?',re.DOTALL).findall(link)	for url, img, name in match:			try:				name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')				name = name + ":" + " " + "Quality:" + " " + "[COLOR dodgerblue]" + " " + "HD" + "[/COLOR]"				addDir(name,url,12,img,fanart)			except:pass	try:		np=re.compile("<link rel='next' href='(.+?)'", re.DOTALL | re.IGNORECASE).findall(link)[0]		name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'		addDir(name,np,16,next,fanart)	except:pass	xbmc.executebuiltin('Container.SetViewMode(50)')def GETTRENDING(url, name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<a href="([^"]+)"><img src="([^"]+)" alt="Watch ([^"]+) For Free"></a>[^"]+<div class="rating"><span class="icon-star2"></span> ([^"]+)</div>[^"]+<span class="quality">([^"]+)</span>',re.DOTALL).findall(link)        for url, img, name, rating, quality in match:			try:				name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')				name = name + ":" + " " + "Quality:" + " " + "[COLOR dodgerblue]" + " " + quality + "[/COLOR]" + " " + "|" + " " + " " + "Rating:" "[COLOR dodgerblue]" + " " + rating + "[/COLOR]"				addDir(name,url,12,img,fanart)			except:pass	try:		np=re.compile('<a href="https://321movies.cc/trending/page(.+?)"', re.DOTALL | re.IGNORECASE).findall(link)[0]		np = BASEURL + '/trending/page' + np		name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'		addDir(name,np,11,next,fanart)	except:pass	xbmc.executebuiltin('Container.SetViewMode(50)')	def GETTV(url,name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<div class="poster">[^"]+<a href="([^"]+)"><img src="([^"]+)" alt="([^"]+)"></a>[^"]+<div class="rating"><span class="icon-star2"></span> ([^"]+)</div>[^"]+</div>',re.DOTALL).findall(link)        for url, img, name, rating in match:			name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')			name = name + ":" + " " + "Rating:" + " " + "[COLOR dodgerblue]" + " " + rating + "[/COLOR]"			addDir(name,url,4,img,fanart='')	try:		np=re.compile("<link rel='next' href='(.+?)'", re.DOTALL | re.IGNORECASE).findall(link)[0]		name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'		addDir(name,np,2,next,fanart)	except:pass	xbmc.executebuiltin('Container.SetViewMode(50)')def GETTV1(url,name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<img src="([^"]+)" alt="([^"]+)">[^"]+<div class="season_m animation-1">[^"]+<a href="([^"]+)"',re.DOTALL).findall(link)        for img, name, url in match:			name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')			addDir(name,url,10,img,fanart='')	try:		np=re.compile("<link rel='next' href='(.+?)'", re.DOTALL | re.IGNORECASE).findall(link)[0]		name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'		addDir(name,np,9,next,fanart)	except:pass	xbmc.executebuiltin('Container.SetViewMode(50)')	def GETEPISODE(url,name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<img src="([^"]+)"></a></div>[^"]+<div class="numerando">([^"]+) - ([^"]+)</div>[^"]+<div class="episodiotitle">[^"]+<a href="([^"]+)">([^"]+)</a>',re.DOTALL).findall(link)        for  img, season, episode, url, name in match:			name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')			name = "Season:" + " " + "[COLOR dodgerblue]" + " " + season + "[/COLOR]" + " " + "|" + " " + " " + "Episode:" "[COLOR dodgerblue]" + " " + episode + "[/COLOR]" + ":   " + name			addDir(name,url,12,img,fanart)	xbmc.executebuiltin('Container.SetViewMode(50)')def GETEPISODE1(url,name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<img src="([^"]+)"></a></div>[^"]+<div class="numerando">([^"]+)x([^"]+)</div>[^"]+<div class="episodiotitle">[^"]+<a href="([^"]+)">([^"]+)</a>',re.DOTALL).findall(link)        for  img, season, episode, url, name in match:			name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')			name = "Season:" + " " + "[COLOR dodgerblue]" + " " + season + "[/COLOR]" + " " + "|" + " " + " " + "Episode:" "[COLOR dodgerblue]" + " " + episode + "[/COLOR]" + ":   " + name			addDir(name,url,12,img,fanart)	xbmc.executebuiltin('Container.SetViewMode(50)')def GETEPISODE2(url,name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<img src="([^"]+)" alt="([^"]+) [^"]+">[^"]+<div class="season_m animation-1">[^"]+<a href="([^"]+)">[^"]+<span class="b">([^"]+)x([^"]+)</span>',re.DOTALL).findall(link)        for img, name, url, season, episode in match:			name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')			name = name + " " + " " + " " + season + " " + "x" + " " + episode			addDir(name,url,12,img,fanart)	try:		np=re.compile("<link rel='next' href='(.+?)'", re.DOTALL | re.IGNORECASE).findall(link)[0]		name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'		addDir(name,np,200,next,fanart)	except:pass				xbmc.executebuiltin('Container.SetViewMode(50)')	def GETGENRES(url,name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<a href="([^"]+)" title="[^"]+">([^"]+)</a>',re.DOTALL).findall(link)        for url, name in match:		if "&" in name:			pass		else:			name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#039;','`')			addDir(name,url,1,iconimage,fanart='')	xbmc.executebuiltin('Container.SetViewMode(50)')def GETRELEASE(url,name):        metaset = selfAddon.getSetting('enable_meta')        link = open_url(url)        match=re.compile('<a href="https://321movies.cc/release/([^"]+)">([^"]+)</a>',re.DOTALL).findall(link)        for url, name, in match:		if "Movies" in name:			pass		else:			url = BASEURL + "/release/" + url			addDir(name,url,1,iconimage,fanart='')	xbmc.executebuiltin('Container.SetViewMode(50)')def GETSOURCE(name,url):	metaset = selfAddon.getSetting('enable_meta')	link = open_url(url)	url = re.compile('<iframe class="metaframe rptss" src="(.+?)"',re.DOTALL).findall(link)	for url in url:		if 'youtube' in url:			addLink('[B][COLOR dodgerblue]YouTube:[/COLOR][COLOR red] Trailer[/COLOR][/B]',url,201,iconimage,fanart)		elif 'openload' in url:			addLink('[B][COLOR dodgerblue]OpenLoad:[/COLOR][COLOR red] Full Version[/COLOR][/B]',url,201,iconimage,fanart)	xbmc.executebuiltin('Container.SetViewMode(50)')		def cleanHex(text):    def fixup(m):        text = m.group(0)        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')        else: return unichr(int(text[2:-1])).encode('utf-8')    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))def SEARCH_MOVIES(url):	search_entered = ''	keyboard = xbmc.Keyboard(search_entered, 'Search 321Movies.co')	keyboard.doModal()	if keyboard.isConfirmed():		search_entered = keyboard.getText().replace(' ','+')	if len(search_entered)>1:		url = url + '?s=' + search_entered		progress = xbmcgui.DialogProgress()		GETSEARCHMOVIES(url)def GETSEARCHMOVIES(url):	metaset = selfAddon.getSetting('enable_meta')	link = open_url(url)	match=re.compile('class="image">.*?href="([^"]+)">[^"]+"([^"]+)"[^"]+"([^"]+)"', re.DOTALL | re.IGNORECASE).findall(link)	for url, img, name in match:			try:				if name.startswith('Watch '): 					name = re.compile("Watch (.*?) For Free", re.DOTALL | re.IGNORECASE).findall(name)[0]					name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#215;','x')					url = BASEURL + '/film/' + url					addDir(name,url,12,img,fanart)				elif '/anime/' in url:					name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#215;','x')					url = BASEURL + '/anime/' + url					addDir(name,url,4,img,fanart)				elif '/seasons/' in url:					name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#215;','x')					url = BASEURL + '/seasons/' + url					addDir(name,url,10,img,fanart)				elif '/episodes/' in url:					name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-').replace('&#215;','x')					url = BASEURL + '/episodes/' + url					addDir(name,url,12,img,fanart)			except:pass	try:		np=re.compile('<a href="http://321movies.co/page/([^"]+)"', re.DOTALL | re.IGNORECASE).findall(link)[0]		if '2' in np:			np = BASEURL + '/page/' + np			name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'			addDir(name,np,17,next,fanart)		elif '3' in np:			np = BASEURL + '/page/' + np			name = '[COLOR dodgerblue]' + 'Next Page >>' + '[/COLOR]'			addDir(name,np,17,next,fanart)	except:pass	xbmc.executebuiltin('Container.SetViewMode(50)')	def resolve(name,url,iconimage):	progress = xbmcgui.DialogProgress()	progress.create('321Movies', 'Opening Stream:')	progress.update(10, "", name, "" )	try: 		url = urlresolver.resolve(url)		liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)		liz.setProperty('IsPlayable','true')		xbmc.Player ().play(url, liz, False)	except:pass	xbmcplugin.endOfDirectory(int(sys.argv[1]))def get_params():        param=[]        paramstring=sys.argv[2]        if len(paramstring)>=2:                params=sys.argv[2]                cleanedparams=params.replace('?','')                if (params[len(params)-1]=='/'):                        params=params[0:len(params)-2]                pairsofparams=cleanedparams.split('&')                param={}                for i in range(len(pairsofparams)):                        splitparams={}                        splitparams=pairsofparams[i].split('=')                        if (len(splitparams))==2:                                param[splitparams[0]]=splitparams[1]        return paramdef addDir(name,url,mode,iconimage,fanart,description=''):    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)    ok=True    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )    liz.setProperty('fanart_image', fanart)    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)    return okdef addLink(name,url,mode,iconimage,description=''):    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)    ok=True    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )    liz.setProperty('fanart_image', fanart)    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)    return ok        def open_url(url):    req = urllib2.Request(url)    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')    response = urllib2.urlopen(req)    link=response.read()    response.close()    return linkdef setView(content, viewType):    if content:        xbmcplugin.setContent(int(sys.argv[1]), content)    if selfAddon.getSetting('auto-view')=='true':        xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )        params=get_params(); url=None; name=None; mode=None; site=None; iconimage=Nonetry: site=urllib.unquote_plus(params["site"])except: passtry: url=urllib.unquote_plus(params["url"])except: passtry: name=urllib.unquote_plus(params["name"])except: passtry: mode=int(params["mode"])except: passtry: iconimage=urllib.unquote_plus(params["iconimage"])except: passif mode==None or url==None or len(url)<1: CATEGORIES()elif mode==1: GETMOVIES(url) elif mode==2: GETTV(url,name) elif mode==3: SEARCH_MOVIES(url) elif mode==4: GETEPISODE(url,name) elif mode==5: GETGENRES(url,name) elif mode==6: GETRELEASE(url,name) elif mode==7: MOVIESINDEX() elif mode==8: TVSHOWINDEX() elif mode==9: GETTV1(url,name) elif mode==10: GETEPISODE1(url,name) elif mode==11: GETTRENDING(url,name) elif mode==12: GETSOURCE(name, url) elif mode==16: GETHD(url) elif mode==17: GETSEARCHMOVIES(url)elif mode==18: GETTVSHOWLINK(url)elif mode==200: GETEPISODE2(url,name) elif mode==201: resolve(name,url,iconimage) xbmcplugin.endOfDirectory(int(sys.argv[1]))