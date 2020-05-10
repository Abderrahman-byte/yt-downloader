import os

def presente(info):
    try :
        print("*" * 40)
        print("Status:", info['status'])
        print("Video Id:", info['player_response']['videoDetails']['videoId'])
        print("Video Title:", info['player_response']['videoDetails']['title'])
        print("Author:", info['player_response']['videoDetails']['author'])
        print("Length:", info['player_response']['videoDetails']['lengthSeconds']+'s')
        print("*" * 40, '\n')
    except :
        print("[!] Connection error Try again")

def getUrl(info) :
    try :
        url = info['player_response']['streamingData']['formats'][1]['url']
        return url
    except :
        return None

def getPath(dir_name, title, ext) :
    try :
        return os.path.join(dir_name, title + "." + ext)
    except :
        return None

def getTitle(info):
    try :
        title = info['player_response']['videoDetails']['title']
        title = title.replace(' ', '_')
        title = title.replace('-', '_')
        title = title.replace('__', '_')
        return title
    except :
        return None