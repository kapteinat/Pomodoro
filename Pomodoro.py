
import time


def conversor(t):
    return t * 60

def pomodoro(trabalho, descanso):
    trab = conversor(trabalho)
    desc = conversor(descanso)
    contador(trab,"trabalho")
    contador(desc,"descanso")


def contador(t,x):
    while t:
        min, sec = divmod(t,60)
        print(f"{x}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1)
        t -=1


trabalho = int(input("Tempo para estudo(min): " ))
descanso = int(input("Tempo para descanso(min): "))

pomodoro(trabalho, descanso)