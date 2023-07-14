score1 = float(input("Write your first score: "))
score2 = float(input("Write your second score: "))
average_score = (score1 + score2)/2

if average_score < 5.0:
    print("REPROVADO")
elif 5.0 > average_score > 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
