from zipfile import ZipFile
from bs4 import BeautifulSoup
import requests, os, sys

def get_current_version():
    x = os.listdir(to_dir)
    for thing in x:
        thing = thing.lower()
        if thing.startswith("lolskin"):
            return thing.split()[1]

if os.path.exists(os.curdir+"\\config.txt"):
    with open("config.txt", "r") as f:
        to_dir = f.read()
    print("Autofound path %s"%to_dir)
else:
    new_path = input("No default path set! Choose the main folder. (It will create the directory in this folder.)\nPlease write out the full path. (C:\\Wow\\My\\Full\\Path\\Is\\Long)\n> ")
    with open("config.txt", "w") as f:
        f.write(new_path)
    print("Path written!")
    to_dir = new_path

ver = get_current_version()

x = requests.get('http://leagueskin.net/p/download-mod-skin-2020-chn')

soup = BeautifulSoup(x.text, features="html.parser")

new_ver = soup.find(id='name_button_download3').get_text().split()[3]

if ver == new_ver:
    print("Already the newest version.")
    input("Any key to exit...")
    sys.exit()

link = soup.find(id="link_download3").get('href')
download = requests.get(link)
open('new.zip', 'wb').write(download.content)

if os.path.isdir(to_dir+"\\LOLSKIN %s"%ver):
    os.rmdir(to_dir+"\\LOLSKIN %s"%ver)
    print("Removed old path.")

os.mkdir(to_dir+"\\LOLSKIN %s"%new_ver)

with ZipFile("new.zip") as zipObj:
    zipObj.extractall(to_dir+"\\LOLSKIN %s"%new_ver)

print("Success!")
input("Any key to exit...")