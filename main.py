import GenMotivAI
from GenMotivAI.ChatGPT import ChatGPT
from GenMotivAI.Scrapping import Scrapping
import os
from dotenv import load_dotenv
#import GenMotivAI.ChatGPT as ChatGPT
load_dotenv()
print(" ██████  ███████ ███    ██ ███    ███  ██████  ████████ ██ ██    ██    ██  █████")
print("██       ██      ████   ██ ████  ████ ██    ██    ██    ██ ██    ██    ██ ██   ██")
print("██   ███ █████   ██ ██  ██ ██ ████ ██ ██    ██    ██    ██ ██    ██    ██ ███████")
print("██    ██ ██      ██  ██ ██ ██  ██  ██ ██    ██    ██    ██  ██  ██     ██ ██   ██")
print(" ██████  ███████ ██   ████ ██      ██  ██████     ██    ██   ████   ██ ██ ██   ██")
print("____________________________________________________________________________________")
print("By Anthony Douat alias (anthonydt16)")
print("____________________________________________________________________________________")
print("")
print("")
input ("Press Enter to continue...")
url = input("Entrer l'url de l'annonce d'emploie:")

print("Vous avez entrer l'url suivante: " + url)

sur = input("Voulez vous continuer? (y/n)")
if sur == "y":
    print("Chargement de l'annonce...")
    scrap = Scrapping(None,
                      url,
                      None )

    scrap.getprofileLinkdin()
    scrap.getHtml()
    print("Annonce chargé")
    print("____________________________________________________________________________________")
    print("Envoie de l'annonce à l'IA...")
    api_key = os.getenv('API_KEY')
    chat = ChatGPT()
    chat.apiKey = api_key
    chat.profileLinkedin = scrap.profileLinkdin
    chat.html = scrap.html
    print("Annonce envoyé")
    chat.requestOpenIA()
    print("____________________________________________________________________________________")
    print("Réponse sur le fichier reponse.txt Mais attention, une IA n'est pas parfaite, il faut vérifier la réponse")
    print('Bye')



else:
    print("bye")
    exit()













