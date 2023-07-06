# pip install pyshorteners
# pip install pyperclip


import pyshorteners
url=input('Enter the url to shorten:')
def shortenurl(url):
    s=pyshorteners.Shortener()
    print("\nShortened url is:",s.tinyurl.short(url))
    
shortenurl(url)