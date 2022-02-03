"""Main Module"""
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create Instance of language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2022-02-03', authenticator=authenticator)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """This function translates text in english to french"""
    if english_text == "":
        return ""
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = french_text.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    """This function translates text in french to english"""
    if french_text == "":
        return ""

    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = english_text.get("translations")[0].get("translation")
    return english_text
