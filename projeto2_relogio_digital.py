
# importa o Tkinter 

from cProfile import label
from tkinter import * # O asterisco * seginifica que vamos selecionar tudo essa biblioteca tkinter
import tkinter
from datetime import datetime # biblioteca datetime é onde voce pega as horas pc e configura para seu app.


from pyglet import font
font.add_file('wwDigital.ttf')
action_man = font.load('wwDigital.ttf')


# Vamos criar as cores

cor1 = '#3d3d3d' # preto
cor2 = '#fafcff' # branco 
cor3 = '#21c25c' # verde
cor4 = '#eb463b' # vermelha 
cor5 = '#dedcdc' # cinza
cor6 = '#3080f0' # azul

fundo = cor1 # cor de fundo relogio 
cor = cor2  # cor dos numeros                   

#Tela do relogio 
janela=Tk()
janela.title('⏳ Watch By WeLL ⏳') # titulo do relogio
janela.geometry('400x180') #   largura 400x180altura tamanho da janela do relogio
janela.resizable(width=FALSE,height=FALSE)
janela.config(bg=cor1)


#Configurando as horas

def relogio(): # Funcão relogio

    tempo=datetime.now()

    hora=tempo.strftime('%H:%M:%S') # H segfinifica HORA, M= MINUTOS, S=SEGUNDOS 
    dia_semana=tempo.strftime('%A') # A = DIA DA SEMANA,
    dia=tempo.day
    mes=tempo.strftime('%B') #B = MÊS.
    ano=tempo.strftime('%Y') #Y = ANO.  

    l1.config(text=hora) # Configuração hora
    l1.after(200, relogio)# configuração deixar o relogio dinamico (Depois 200 milésimo,ele irá rodar nosso relogio()  )
    l2.config(text=dia_semana + ' ' + str(dia) + '/' + str(mes) + '/' + str(ano)) # configuração semana, dia, mes, ano, 

#Criando uma Label

l1=Label(janela,text='',font='wwDigital 70',bg=fundo,fg=cor6)
l1.grid(row=0,column=0,sticky=NW,padx=5)

l2=Label(janela,text='',font='wwDigital 25',bg=fundo,fg=cor6)
l2.grid(row=5,column=0,sticky=NW,padx=5)

relogio()
janela.mainloop()



