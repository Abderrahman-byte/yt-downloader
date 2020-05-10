import requests

def download() :
    url = 'https://r1---sn-p5h-jhor.googlevideo.com/videoplayback?expire=1589123274&ei=asS3XoCRF-2ixN8PsPeEIA&ip=105.154.30.81&id=o-AJ43wG3hsetjn9PBsZdVkKLrCNW-PVanv-ugsfvmJO0j&itag=22&source=youtube&requiressl=yes&mh=ps&mm=31%2C29&mn=sn-p5h-jhor%2Csn-hgn7rnee&ms=au%2Crdu&mv=m&mvi=0&pl=23&initcwndbps=271250&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=18.575&lmt=1541950596141462&mt=1589101596&fvip=5&c=WEB&txp=5431432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AJpPlLswRQIgL3hSDxTxLJm0RAobZnDrkVLdaHJ4o_V9Ur1djpxGsFMCIQCzh7fykreqoYtVHyuZSh651q_ofixR4XY4jn-nkzYN_g%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ALrAebAwRgIhAPaw4FuqTDm1KtIkLFMWYNeMRKqg0S-7Ni7Y5POw6yV-AiEAqzGWatPPSJ1lgQ0ZM_yBM32okybhAbXKutVqgielscc%3D'

    myfile = requests.get(url)

    # open('video.mp4', 'wb').write(myfile.content)
    print(myfile.content)

download()