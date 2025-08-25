metodo_pagamento = input('Escolha o método de pagamento (cartao/boleto): ')

if metodo_pagamento == 'cartao':
    print('Processando pagamento no cartão...')
elif metodo_pagamento == 'boleto':
    print('Gerando boleto bancário...')
else:
    print('Método de pagamento não reconhecido.')

