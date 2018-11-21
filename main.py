# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:54:34 2018

@author: malik
"""

from bs4 import BeautifulSoup
import requests
import re
import en_core_web_sm

def getPeintrePeinture():
    dict_artiste_oeuvre={} 
    
    urlPage='https://www.moma.org/collection/works?locale=fr&utf8=%E2%9C%93&q=&classifications=9&date_begin=Pre-1850&date_end=2018&include_uncataloged_works=1'
    le_document = requests.get(urlPage).text
    #utilisation de beautifulSoup pour parser la page
    soup = BeautifulSoup(le_document,'html.parser')
    all_artistes_oeuvres=soup.findAll('h2',attrs={'class':'tile__caption tile__caption--3lines center'} )
    for artiste_oeuvre in all_artistes_oeuvres:
        artiste=artiste_oeuvre.text.split('\n')[1]
        oeuvre=artiste_oeuvre.text.split('\n')[3]
        dict_artiste_oeuvre.setdefault(artiste,[]).append(oeuvre)
        
    return dict_artiste_oeuvre


def getMusifilcienMusique():
    dict_musicien_chanson={} 
    
    urlPage='https://www.cs.ubc.ca/~davet/music/list/Best2.html'
    le_document = requests.get(urlPage).text
    #utilisation de beautifulSoup pour parser la page
    soup = BeautifulSoup(le_document,'html.parser')
    table = soup.find('table', attrs={'class':'music'})
    table_body = table.find('tbody')
    les_lignes = table_body.find_all('tr')
    for ligne in les_lignes:
        colonnes = ligne.find_all('td')
        musicien_chanson = [elt.text.strip() for elt in colonnes]
        musicien=musicien_chanson[2]
        chanson=musicien_chanson[3]
        if musicien !='ARTIST': #pour ne pas ajouter ARTIST qui est un nom de colonne  
            dict_musicien_chanson.setdefault(musicien,[]).append(chanson)
    return dict_musicien_chanson

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    soup2 = soup.find("div", {"class": "col-middle"}).find_all("ul")[1]
    for script in soup2(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup2.get_text()))
s

def getFilmsActeurs():
    url_film = 'http://www.allocine.fr/films/'
    nlp = en_core_web_sm.load()
    source = url_to_string(url_film)
    phrases = source.split('.')
    
    acteurs = []
    films = []
    relation = []
    
    for phrase in phrases:
        doc = nlp(phrase)
        persons = [ x for x in doc.ents if x.label_ == 'PERSON']
        art_work = [ x for x in doc.ents if x.label_ == 'WORK_OF_ART']
        for person in persons:
            if person not in acteurs:
                acteurs.append(person)
        for work in art_work:
            if work not in films:
                films.append(person)
        if len(persons)+len(art_work) > 1:
            relation.append(persons + art_work )
            
    return acteurs, films, relation

acteurs, films, relation = getFilmsActeurs()
musicienMusique = getMusicienMusique()
peintrePeinture = getPeintrePeinture()

datas = {
    'musicien-musique' : musicienMusique,
    'peintre-peinture' : peintrePeinture,
    'films' : films,
    'acteurs' : acteurs,
    'relationFilms' : relation,
    }


