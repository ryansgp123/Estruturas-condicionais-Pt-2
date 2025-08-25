tipo_entrega = input("Escolha o tipo de entrega (padrão/expresso): ")

if tipo_entrega == "padrão":
    print("Custo da entrega: R$10,00.")
elif tipo_entrega == "expresso":
    print("Custo da entrega: R$20,00.")
else:
    print("Opção de entrega inválida.")

