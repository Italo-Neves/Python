#Continue
'''
A instrução break e a instrução continue são ferramentas das estruturas de repetição permitindo a interrupção de um único
 ciclo ou do laço de repetição. É importante saber distinguir ambas instruções, por exemplo, a instrução break interrompe
 não somente o ciclo em execução, mas sim, todo o laço, enquanto que a instrução continue finaliza um único laço, fazendo
 com que o Cursor de execução vá para o cabeçalho da estrutura de repetição.

Então, nunca é demais repetir que instrução contine interrompe somente o ciclo que está sendo executado fazendo com que
o cursor de execução retorne ao cabeçalho da estrutura de repetição para dar início a execução do ciclo seguinte.

Caso não conheças a instrução break para a interrupção de laços, é interessante que o faça! E também, se houver dúvidas
sobre as estrutruras de repetição, estude a aula em que tratamos sobre as mesmas.

No código abaixo construimos um simples exemplo com o único propósito de demonstrar a interrupção da execução de um único
ciclo com a instruçao continue.
'''
x = 0
while(x <= 10):
    x+=1
    if(x % 2):
        continue
    print(x)