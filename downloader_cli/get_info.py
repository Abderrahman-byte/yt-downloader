import requests
import urllib.parse as parser
from urllib.parse import parse_qs
import json

def getParam(url, param) :
    parsed = parser.urlparse(url)
    params = parse_qs(parsed.query)

    return params.get(param)[0]

def getInfo(url) :
    video_id = getParam(url, 'v')

    if video_id is not None :
        info_url = f'https://www.youtube.com/get_video_info?video_id={video_id}'
        
        try :
            req = requests.get(info_url)
            content = str(req.content)
            video_info = parse_qs(content)
            video_info['player_response'][0] = json.loads(video_info.get('player_response')[0])

            for entry in video_info :
                video_info[entry] = video_info[entry][0]

            with open('info.json', 'w') as fp :
                fp.write(json.dumps(video_info, indent=4))

            return video_info
            
        except Exception as ex:
            print(ex)
            return None
    else :
        return None