import random

# Lista de citações de Shakespeare
citations = [
    "Ser ou não ser, eis a questão.",
    "O amor deixa sua marca no coração, não na mente.",
    "As palavras são fáceis, como o vento; a fé verdadeira é sólida como pedra.",
    "O mundo inteiro é um palco, e todos os homens e mulheres meramente atores.",
    "Tudo o que termina bem é bom, e se não estiver bem, não é o fim.",
    "Amor deixa a mente ser mudada, e muda-se para onde está a verdadeira vontade.",
    "O amor não vê com os olhos, mas com a mente; portanto, é alado Cupido pintado cego.",
    "Uma rosa por qualquer outro nome cheiraria tão doce.",
    "A tristeza de hoje e alegria de amanhã.",
    "Os covardes morrem muitas vezes antes de suas mortes; O valente nunca prova da morte, exceto uma vez.",
]

def get_random_citation():
    return random.choice(citations)

if __name__ == "__main__":
    print(get_random_citation())
