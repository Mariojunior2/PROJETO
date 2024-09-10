import random  # Para escolher perguntas aleatórias
import json  # Para salvar e carregar o progresso do usuário e banco de perguntas
import unicodedata  # Para normalizar e remover acentuação das strings
from difflib import SequenceMatcher  # Para comparar similaridade entre respostas


quiz = {
    "":"",
    "":"",
    "":"",
    "":"",
    "":""
}