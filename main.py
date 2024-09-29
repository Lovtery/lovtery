print("приветствую тебя в игре квиз! ")
points = 0

if input("земля круглая? ") == ("да"): points += 1
else: points -= 1

if input("2+2 == 4? ") == ("да"): points += 1
else: points -= 1

if input("паук - это насекомое? ") == ("да"): points += 1
else: points -= 1

if input("20//4 == 5? ") == ("да"): points += 1
else: points -= 1

print(f"ваше количество очков: {points}")

if points >= 4: print("поздравляю! вы победили! ")
elif points >= 2: print("вы могли справится лучше! ")
elif points >= 0: print("вы старались...... ")
else: print("вы проиграли,попробуйте снова!")
