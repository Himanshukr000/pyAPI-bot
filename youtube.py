import urllib.request
import urllib.parse
import pafy,os,re
import sp_test as sp



def play(inputN):
	query_string = urllib.parse.urlencode({"search_query" : inputN})
	html_cont = urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
	search_res = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
	#print("http://www.youtube.com/watch?v=" + search_res[0])
	url="http://www.youtube.com/watch?v={}".format(search_res[0])
	vid= pafy.new(url)
	#print(vid)
	best = vid.getbestaudio()
	sp.speak("Playing " + vid.title)
	os.system("mplayer "+'"'+best.url+'"'+'> /dev/null 2>&1')
	
