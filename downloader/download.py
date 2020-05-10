import requests
import sys

from .info import getInfo
from .utils import presente, getUrl, getPath, getTitle

def wget(url, title) :
    print("start installing ...\n")
    myfile = requests.get(url)
    open(title, 'wb').write(myfile.content)
    print("check in :", title)

def download(url, location) :
    print('fetching data from', url, '\n')
    video_info = getInfo(url)
    file_url = ''
    title = ''

    if video_info is None :
        sys.stderr.write("[!] video id doesn\'t exist\n")
        sys.exit()

    file_url = getUrl(video_info)
    title = getTitle(video_info)

    presente(video_info)
    wget(file_url, getPath(location, title, 'mp4'))

    print("Installing Done !")