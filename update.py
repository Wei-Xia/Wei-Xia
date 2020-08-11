#!/usr/local/bin/python3

import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://weixia.info/feed.xml').content
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''
<h3 align="center"> Hi there, I'm [Wei Xia](https://weixia.dev/) 👋</h3>

<p align="center">
<p align="center">
    <a href="https://weixia.dev/linkedin.html">LinkedIn</a> •
    <a href="https://twitter.com/weixia812">Twitter</a> •
    <a href="https://weixia.dev/github.html">GitHub</a> •
    <a href="https://weixia.dev/zhihu.html">知乎</a> •
    <a href="https://weixia.dev/xueqiu.html">雪球</a>
</p>
</p>

<br/>
<br/>

I am a Full Stack Developer working at IBM. I speak JavaScript.


## My Recent Blog Posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        print(text)
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://weixia.info/archives/)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=Wei-Xia&hide=contribs,prs&count_private=true&show_icons=true)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=Wei-Xia&hide=Groff&layout=compact)
''')
