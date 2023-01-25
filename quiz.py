def checarResposta (resposta, resposta_usuario):
    if resposta == resposta_usuario:
        return True

def calcularScore (qntPerguntas, qntAcertos):
    return qntAcertos / qntPerguntas * 100

print('Olá, bem-vindo ao quiz do João')
comecar = input('Deseja começar o quiz? (S/N) ')

if comecar != 'S':
    quit()

score = 0

pergunta_1 = "\n1: Qual a operação contrária a potenciação? \n a) Divisão \n b) Radiciação \n c) Adição \n d) Multiplicação "
resposta_1 = "b"

pergunta_2 = "\n2: O Brasil foi colônia de qual país? \n a) Portugal \n b) Itália \n c) França \n d) Inglaterra "
resposta_2 = "a"

pergunta_3 = "\n3: Qual físico produziu três leis que levaram seu nome na sua denominação? \n a) Einsten \n b) Newton \n c) Karl Marx \n d) Rosseau "
resposta_3 = "b"

pergunta_4 = "\n4: Qual destes países não se localiza na América do sul? \n a) Angola \n b) Bolívia \n c) Suriname \n d) Guiana "
resposta_4 = "a"

pergunta_5 = "\n5: 'Comer' é um: \n a) Artigo \n b) Adjetivo \n c) Verbo \n d) Pronome "
resposta_5 = "c"

print(pergunta_1)
resposta_usuario = input("Resposta: ")
if checarResposta(resposta_1, resposta_usuario) == True:
    score += 1

print(pergunta_2)
resposta_usuario = input("Resposta: ")
if checarResposta(resposta_2, resposta_usuario) == True:
    score += 1

print(pergunta_3)
resposta_usuario = input("Resposta: ")
if checarResposta(resposta_3, resposta_usuario) == True:
    score += 1

print(pergunta_4)
resposta_usuario = input("Resposta: ")
if checarResposta(resposta_4, resposta_usuario) == True:
    score += 1

print(pergunta_5)
resposta_usuario = input("Resposta: ")
if checarResposta(resposta_5, resposta_usuario) == True:
    score += 1

scoreFinal = calcularScore(5, score)
print('Quiz finalizado, você acertou '+str(scoreFinal)+'%, parabéns!')