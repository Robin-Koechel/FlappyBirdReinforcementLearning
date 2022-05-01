from bs4 import BeautifulSoup as bs
import requests
import os
import pdfkit
from tqdm import tqdm

#go to mangakakalot.com-> go to your manga chapter overview page and paste the url in:
manga_title = input("What's the tile of the manga? : ")
url_website = input("paste the mangakakalot.com url here: ")

place_to_safe_the_maga = "C:/Users/Robin/Documents/"
path_html_to_pdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

session = requests.Session()

def get_list_of_chapters():
    chapters = []
    html = requests.get(url_website)
    soup = bs(html.content, 'html.parser')

    for tag in soup.find_all('a', href=True):
        href = tag['href']
        if 'chapter' in href:
            chapters.append(href)
    chapters.reverse()
    return chapters

def download_website(path, url, title):
    config = pdfkit.configuration(wkhtmltopdf=path_html_to_pdf)
    pdfkit.from_url(url, path+"/"+title, configuration=config)
    #remove last two pages
    #change_pdf(path+"/output.pdf")

def create_folder_with_all_chapters():
    try: #Check if you have a manger dir... if not create one
        os.mkdir(place_to_safe_the_maga + 'Manga')
    except:
        print("Folder with all the nice manga already exists ^^")

    try:
        folder_name = manga_title

        #create dir for every chapter
        chapters = get_list_of_chapters()
        path = 'C:/Users/Robin/Documents/Manga/' + folder_name + '/'
        os.mkdir(path)
        for c in tqdm(chapters):
            download_website(path, c, str(c).split("/")[-1]+".pdf")
    except:
        print("Vermutlich hast du diesen Manga schon xD")

create_folder_with_all_chapters()