import random  # Para escolher perguntas aleatórias
import json  # Para salvar e carregar o progresso do usuário e banco de perguntas
import unicodedata  # Para normalizar e remover acentuação das strings
from difflib import SequenceMatcher  # Para comparar similaridade entre respostas


quiz = {
    "Qual a capital do Brasil?":"brasilia",
    "Nome do Criador do Jogo":"mario",
    "O presidente atual":"lula",
    "O melhor amigo do patrick":"bob esponja",
    "League of Legends é?":"ruim"
}


primeira_pergunta, primeira_resposta = next(iter(quiz.items()))
print("Pergunta:", primeira_pergunta)
pergunta = input('responda! ')
pergunta = pergunta.lower()
if pergunta in primeira_resposta:
    print('Acertou')
else: 
    print('errou trouxa')
   




