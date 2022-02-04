import urllib.request
import re
import urllib
import json
import os
import ffmpeg

search_keyword=input("Enter the video to be searched")
main_search_keyword=search_keyword.replace(" ","+")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + main_search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
for i in range(0,10):
    #change to yours VideoID or change url inparams
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_ids[i]}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        print(i,data['title'])

a=int(input("Enter the index number of the youtube video you want to download"))

os.system("youtube-dl -F https://www.youtube.com/watch?v=" + video_ids[a])
b=int(input("Enter th code of the video you want to download or assamble"))
c=int(input("Enter the code of the audio you to download or assamble with the video"))
d=str(b)
e=str(c)
os.system("youtube-dl -f "+d+"+"+e+" https://www.youtube.com/watch?v=" + video_ids[a])
