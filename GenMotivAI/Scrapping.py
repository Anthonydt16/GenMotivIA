import time

import requests
import urllib as urllib
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

class Scrapping:
    """
    Scrapping class
    :param urlRecherche: URL de la recherche emploie
    :param urlHtml: url of the web page
    :param urlCV: url of the CV
    :param urlLinkdin: url of the linkdin profile

    """

    # constructor
    def __init__(self, urlRecherche, urlHtml, urlLinkdin, urlCV = None):
        self.urlRecherche = urlRecherche
        self.urlCV = urlCV
        self.urlHtml = urlHtml
        self.urlLinkdin = urlLinkdin
        self.profileLinkdin = None
        self.CV = None
        self.htmlEmploies = None
        self.htmlEmploie = None
        self.html = None

    def getHtml(self) -> str:
        """
        This method is used to get the html code of a web page
        :return: html code of a web page
        """
        response = requests.get(self.urlHtml)
        html_content = response.content
        # Créer une instance de BeautifulSoup pour le contenu HTML
        soup = BeautifulSoup(html_content, "html.parser")
        #si ça dépasse les 3500 token un token vaut un mot de 4 lettres alors on coupe
        if len(soup.get_text()) > 3500:
            self.html = soup.get_text()[:3500]
        else:
            self.html = soup.get_text()

        return self.html

    def getprofileLinkdin(self):
        ##charger le fichier json
        with open(os.getenv('PROFILE')) as f:
            self.profileLinkdin = json.loads(f.read().encode('utf-8').decode('utf-8-sig'))


    def getEmploieWild(self)->str:
        """
        This method is used to get the html code of a web page
        :return: html code of a web page
        """
        # with urllib.request.urlopen(self.urlRecherche) as response:
        #     self.htmlEmploies = response.read()


        # URL de la page que vous souhaitez extraire le contenu


        # Récupérer le contenu HTML de la page
        response = requests.get(self.urlRecherche)
        html_content = response.content

        # Créer une instance de BeautifulSoup pour le contenu HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Extraire le texte sans balises HTML
        text_content = soup.get_text()

        # Afficher le contenu texte
        self.htmlEmploies = text_content

        return self.htmlEmploies
