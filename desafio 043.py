preço = float(input("digite o valor do produto:"))
print(''' formas de pagamento
      [1] a vista dinheiro/cheque
      [2] a vista cartão 
      [3] 2x no cartão
      [4] 3x no cartão''')
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