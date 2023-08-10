import os
import html2markdown
from bs4 import BeautifulSoup, Doctype
from markdownify import markdownify

directory = './dataset/'
for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith('.html'):
            fname = os.path.join(root, filename) #print('Filename: {}'.format(fname))
            file = open(fname, "r").read() # file = open("./index.html", "r").read()
            html = markdownify(file, heading_style="ATX")
            newfile = open(fname, "w")
            newfile.write(html)
            newfile.close()
