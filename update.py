#!/usr/local/bin/python3

import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://weixia.info/feed.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''
```
 _   _      _                                                                                      _
| \ | | ___| |_ ___ __ _ _ __     ___  _ __    _ __  _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___ (_)_ __   __ _
|  \| |/ _ \ __/ __/ _` | '_ \   / _ \| '_ \  | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
| |\  |  __/ || (_| (_| | | | | | (_) | | | | | |_) | | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
|_| \_|\___|\__\___\__,_|_| |_|  \___/|_| |_| | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
                                              |_|              |___/                                       |___/
```

## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://weixia.info/archives/)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=Wei-Xia&hide=contribs,prs&count_private=true&show_icons=true)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=Wei-Xia&hide=Groff&layout=compact)
''')
