preço = float(input("digite o valor do produto:"))
print("digite 1 para a forma de pagamento ser em dinheiro ")
print("digite 2 para a forma de pagamento ser em cartão ")
print("digite 3 para a forma de pagamento ser em 2x no cartão  ")
print("digite 4 para a forma de pagamento ser em 3x no cartão ")
condiçãodepagamento = int(input("digite a condição de pagamento: "))

if condiçãodepagamento == 1 :
    desconto = preço * 10/100
    novo = preço - desconto
    print("voce vai pagar:",novo )
elif condiçãodepagamento == 2:
    desconto = preço * 5/100
    novo = preço - desconto
    print("voce vai pagar:",novo )
elif condiçãodepagamento == 3:
    print("preço normal:", preço)
elif condiçãodepagamento == 4:
    desconto = preço * 20/100
    novo = preço + desconto
    print("voce vai pagar:",novo )