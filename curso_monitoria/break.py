#Break
'''
A instrução break finaliza a iteração e o Script continua a execução normalmente. O objetivo dessa instrução é fornecer
a capacidade de forçar a interrupção da iteração.

A seguir, temos um código simples que utiliza a instrução break pra finalizar a execução do laço de repetição while,
quando a condição definida com a instrução if retornar verdadeiro.
'''
x = 0
for x in range(0,11):
    x+=1
    if(x==5):
        print("Interrompendo a execução da repetição.")
        break
    print(x)
