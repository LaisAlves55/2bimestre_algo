
import time    

ligado= False
tempo= 0
temperatura= 0

def ligar(novo_tempo, nova_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado= True
        tempo= novo_tempo
        temperatura= nova_temperatura
        print(f'Maquina louça ligada por {tempo} segundos com temperatura {temperatura} graus')
        iniciar_cronometro(tempo)
        desligar()#desligar automaticamente
    else:
        print('Maquina louça ja está ligada!')
        
def desligar():
    global ligado
    if ligado:
        ligado= False
        print('Maquina louça desligada')
    else:
        print('Maquina louça ja estava desligada')
        
def status():
    if ligado:
        print(f'Tempo: {tempo} segundos \n temperatura: {temperatura}') 
    else:
        print('Maquina louça desligada')
    
def iniciar_cronometro(segundos):
    while tempo > 0:
        print( f' segundos restantes: {segundos}segundos', end="\r")
        time.sleep(1)
        segundos -= 1  #segundos= segundos-1
    print(' \n  tempo esgotado')
    
def vidro():
    vidro(180 , 100)
    
def plastico():
    plastico(60,21)
    
def metal():
    metal(180,30)
    
int(input('digite 1 para vidro, 2 para plastico e 3 para metal'))
if input == 1:
        vidro()
elif input == 2:
        plastico()
elif input == 3:
        metal()
else:
        print('digite um numero valido')
