import openai
class ChatGPT:
    """
    This class is used to chat with the GPT-3.5 API
    """

    #constructor for the class
    def __init__(self):
        self.apiKey = None
        self.reponse = None
        self.html = None
        self.CV = None
        self.profileLinkedin = None

    def requestOpenIA(self)-> str:
        """
        This method is used to request the OpenAI API
        :return: Json response from the API
        """
        openai.api_key = self.apiKey
        self.reponse = openai.ChatCompletion.create(
            model=os.getenv('MODEL') or "gpt-4-1106-preview",
            messages= [
                {"role": "user", "content": "je vais te donnée le contenu de mon CV, de mon profile linkedin et la page web de la demande d'emploie et tu va me rédiger un lettre de motivation avec les informations que tu aura trouvé"},
                {"role": "assistant", "content": "ok, je vais faire de mon mieux"},
                {"role": "user", "content": "mon profile linkedin est le suivant: " + self.profileLinkedin.__str__()},
                {"role": "user", "content": "le contenue de la page web est la suivante: " + self.html},
                {"role": "user", "content": "maintenant fais moi une lettre de motivation qui explique mon parcours et pourquoi je veux ce poste et que j'ai les compétences pour ce poste mais n'invente pas de compétences que je n'ai pas. c'est hyper important"},
            ])
        self.reponse = self.reponse.choices[0].message.content
        #crée un fichier .txt avec la réponse
        with open('reponse.txt', 'w') as f:
            f.write(self.reponse)