spent = int(input("how many games she bought this month: "))
preco_total = 0.0
for i in range(spent):
    preco_jogo = float(input("Preço do jogo: "))
    preco_total = preco_total + preco_jogo
print("Gertie spent ", preco_total, "euros in games")
if preco_total > 100 :
    print("Gertie has issues")