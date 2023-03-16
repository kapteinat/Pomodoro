
import time

#converter o tempo para minutos
def conversor(t):
    return t * 60


#faz o minuto chegar a 0 
def contador(t,x):
    while t:
        min, sec = divmod(t,60)
        print(f"{x}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1) 
        t -=1
        
#funçao principal do codigo
def pomodoro(estudo, descanso):
    estd = conversor(estudo)
    desc = conversor(descanso)
    contador(estd,"estudo")
    contador(desc,"descanso")



#criando as variaveis
estudo = int(input("Tempo para estudo(min): " ))
descanso = int(input("Tempo para descanso(min): "))

pomodoro(estudo, descanso) 