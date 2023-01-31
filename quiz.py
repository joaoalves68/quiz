import pandas as pd

def checarResposta (resposta, resposta_usuario):
    if resposta == resposta_usuario:
        return True

def calcularScore (qntPerguntas, qntAcertos):
    return int(qntAcertos) / int(qntPerguntas) * 100

print('Olá, bem-vindo ao quiz do João')

comecar = input('Deseja começar o quiz? (S/N) ').lower()  
if comecar != 's':
    print('\nOk, até a próxima!')
    quit()

score = 0

questions = pd.read_excel(r'C:\Users\JOAO\Desktop\quiz\questions.xlsx')

quantidadePerguntas = int(input('Quantas perguntas deseja responder? (MAX: '+str(questions['QUESTIONS'].count())+') '))
if quantidadePerguntas > questions['QUESTIONS'].count():
    quit()

for x in range(quantidadePerguntas):
    print('\n'+questions['QUESTIONS'][x].replace("||", "\n"))
    respostaUsuario = input("Resposta: ").lower()
    if checarResposta(questions['ANSWERS'][x], respostaUsuario) == True:
        score += 1

scoreFinal = calcularScore(quantidadePerguntas, score)
print('\n\nQuiz finalizado, você acertou '+str(scoreFinal)+'%, parabéns!')