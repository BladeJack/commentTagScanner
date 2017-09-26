import sys
from bs4 import BeautifulSoup, Comment
import urllib.request


def commentScan(x):
    soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'lxml')
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))

    print(comments)

def main():
    argv = sys.argv[1]
    commentScan(argv)


if __name__ == "__main__":
    main()



