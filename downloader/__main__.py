import argparse
import os
import sys

from .download import download

def main() :
    cwd = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="Input url of the video to download")
    parser.add_argument('-l', help="the path of the output file", default=cwd)
    
    args = parser.parse_args()
    url = args.url
    
    if not os.path.exists(args.l) :
        os.makedirs(args.l)

    if url.startswith('https://www.youtube.com/watch') :
        pass
    elif url.startswith("http://www.youtube.com/watch") :
        pass
    elif url.startswith("www.youtube.com/watch") :
        pass
    elif url.startswith("youtube.com/watch") :
        pass
    else :
        sys.stderr.write('[!] Invalid url\n')
        sys.exit()

    download(args.url, args.l)

if __name__ == '__main__' :
    main()