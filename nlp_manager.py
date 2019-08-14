import spacy
from log_manager import logger


def load_nlp_model():
    return spacy.load("en_core_web_lg")


logger.info("Loading NLP Model")
nlp = load_nlp_model()
logger.info("NLP Model loaded")
