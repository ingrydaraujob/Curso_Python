times = ("Atlético Mineiro", "Botafogo", "Corinthians", "Cruzeiro" , "Flamengo", "Fluminense", "Grêmio" , "Internacional", "Palmeiras","Santos" , "São Paulo" , "Vasco da Gama" , "bahia" , "nautico" , "vitória" , "atletico paranaense" , "chapecoense" , "fortaleza", "bragantino","cuiabá")
posiçao = times.index("chapecoense")
print("-=-"*18)
print(f"os 5 primeiros times são:{times[0:5]}")
print("-=-"*18)
print(f"os 4 ultimos times são: {times[-5:-1]}")
print("-=-"*18)
print(f"os times em ordem alfabetica {sorted(times)}")
print("-=-"*18)
print(f"a posição da chapecoense é: {posiçao+1}")
