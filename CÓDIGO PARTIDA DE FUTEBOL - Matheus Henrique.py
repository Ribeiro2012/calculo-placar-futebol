time1 = input ("Digite o primeiro time: ")
time2 = input ("Digite o segundo time: ")
placar_time1 = int (input("Quantos gols fez o primeiro time: "))
placar_time2 = int (input("Quantos gols fez o segundo time: "))

if placar_time1 > placar_time2:
    print (f"O {time1} venceu!")

elif placar_time2 > placar_time1:
    print (f"O {time2} venceu!")

else:
    print ("A partida deu empate!")