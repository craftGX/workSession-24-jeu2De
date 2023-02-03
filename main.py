import random

jouer = True

while jouer:
    print(random.randint(1, 6))
    re_lancer = input("voulez-vous relancer le dé ? (o/n) : ")
    if re_lancer.lower() == "o":
        continue
    else:
        print("le jeu est terminé ! ")
        break
