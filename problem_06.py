"""problem_06.py

The first hint to this problem is in a comment in the page's source: <!-- <!--zip --> 
With this knowledge, we can traverse to zip.html, which tells us to 'find the zip'.

From there, we'll navigate to the original page (channel) and navigate to '.zip'
instead of '.html'. This will trigger a download of a zip file, which we'll then
extract to find a large number of files.

One of the files from the zip folder is a readme, which will tell us which file to
start reading from first.
"""
import webbrowser
import requests
from zipfile import ZipFile, ZipInfo

webpage = 'http://www.pythonchallenge.com/pc/def/channel.html'
zip_page = webpage.replace('html', 'zip')

zip_content = requests.get(zip_page).content
zip_file_name = 'channel.zip'
with open(zip_file_name, 'wb') as fp:
    fp.write(zip_content)

start_file_name = ''
with ZipFile(zip_file_name) as zf:
    with zf.open('readme.txt') as fp:
        lines = [x.decode('utf-8').strip() for x in fp.readlines()]
        hint_line = lines[2]
        print(lines)
        start_file_name = f'{hint_line.split()[-1]}.txt'

    secret_message = b''
    current_file_name = start_file_name
    while current_file_name.split('.')[0].isnumeric():
        with zf.open(current_file_name) as fp:
            secret_message += zf.getinfo(current_file_name).comment
            line = fp.readline().decode('utf-8').strip()
            current_file_name = f'{line.split()[-1]}.txt'
    print(line)
    print(secret_message.decode('utf-8'))

webbrowser.open(webpage.replace('channel', 'oxygen'))

