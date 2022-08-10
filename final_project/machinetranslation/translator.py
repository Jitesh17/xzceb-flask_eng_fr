import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')


def englishToFrench(text):
    if text is None:
        return None
    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    return translation.get("translations")[0].get("translation")


def frenchToEnglish(text):
    if text is None:
        return None
    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    return translation.get("translations")[0].get("translation")
