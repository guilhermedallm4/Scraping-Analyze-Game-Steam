from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options
import json
import unicodedata

# mode headless
chrome_options = Options()
chrome_options.add_argument('--headless')

# Create a conjunt for unique URLS 
unique_links = set()
unique_links_post = set()

vectorCommentary = []

#Settings driver Chrome 
navegador = webdriver.Chrome(options=chrome_options)

def jsonImport(info):
    dados_existentes = []
    archive = 'analiseCS2.json'
    try:
        with open(archive, 'r', encoding="utf-8") as arquivo:
            dados_existentes = json.load(arquivo)
        dados_existentes.append(info)

    except FileNotFoundError:
        dados_existentes = [info]

    with open(archive, 'w', encoding="utf-8") as arquivo:
        json.dump(dados_existentes, arquivo, ensure_ascii=False)
        
    dados_existentes.clear()

def clean_text(text): 
    return ''.join(char for char in text if unicodedata.name(char).isascii())

def getPageSource(url, maxscroll = 1):
    navegador.get(url)

    sleep(5)
    for i in range(0, maxscroll):
            
        navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(10)

    
    html_content = navegador.page_source
    
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    return soup
    
def main():
    
    post = {}
    
    language = 'brazilian'
    
    url = f'https://steamcommunity.com/app/730/reviews/?filterLanguage={language}'
    
    soup = getPageSource(url, 1)
    
    recomendation = soup.find_all('div', class_='apphub_CardContentMain')
    
    for getInfo in recomendation:
        
        recommendProduct = getInfo.find('div', class_='found_helpful')

        awardInforamtion = getInfo.find('div', class_='review_award_aggregated tooltip')

        classificationPost = getInfo.find('div', class_='title')
        
        timeRegistered = getInfo.find('div', class_='hours')
        
        commentaryPost = getInfo.find('div', class_='apphub_CardTextContent')
        
        datePost = getInfo.find('div', class_='date_posted')
        
        authorPost = soup.find('div', class_=re.compile(r'apphub_CardContentAuthorName.*')).find_all('a')
        
        print(authorPost)
        
        for removeTag in awardInforamtion.find_all():
            
            removeTag.extract()
        
        numberAward = awardInforamtion.get_text(strip=True)
        
        for tag in commentaryPost.find_all():
            
            tag.extract()
            
        texto = commentaryPost.get_text(strip=True)
        
        author = authorPost[1].text
        
        urlPerfil = authorPost[1]['href']
        
        if recommendProduct:
            
            recommendProduct = recommendProduct.text
            
            post['recommendProduct'] = recommendProduct
        
        else:
            
            post['recommendProduct'] = 'false'

        if numberAward:
            
            post['numberAward'] = numberAward
        
        else:
            
            post['numberAward'] = 'false'   

        print(classificationPost)
        if classificationPost.text == "Not Recommended":
            
            post['classificationPost'] = 'Não recomendado'

        else:
            
            post['classificationPost'] = 'Recomendado'

        if timeRegistered:
            
            timeRegistered = timeRegistered.text
            
            post['timeRegistered'] = timeRegistered
        
        else:
            
            post['timeRegistered'] = 'false'

        if texto:
            
            post['texto'] = texto
        
        else:
            
            post['texto'] = 'false'

        if author:
            
            post['author'] = author
        
        else:
            
            post['author'] = 'false'

        if urlPerfil:
            
            post['urlPerfil'] = urlPerfil
        
        else:
            
            post['urlPerfil'] = 'false'
        
        jsonImport(post)
        


main()
