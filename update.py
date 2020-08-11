#!/usr/local/bin/python3

import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://weixia.info/feed.xml').content
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''
### Hi there, I'm [Wei Xia](https://weixia.dev/) 👋

<a href="https://www.linkedin.com/in/weixia812/">
  <img align="left" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://twitter.com/weixia812">
  <img align="left" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />
</a>
<a href="https://www.zhihu.com/people/weixia812">
  <img align="left" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/zhihu.svg" />
</a>

<br/>
<br/>

I am a Full Stack Developer working at IBM. I speak JavaScript.


## My Blog Posts
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
