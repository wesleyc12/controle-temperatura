import time
temp_atual = 20.0
# Assume-se uma temperatura inicial de 20°C, representando uma condição ambiente padrão.
temp_desejada = float(input("Digite a temperatura desejada (°C):" ))
aquecedor_ligado = False

def controlador(temp_atual, temp_desejada):
    if temp_atual < temp_desejada:
        return True #Liga o aquecedor
    else:
        return False #Desliga o aquecedor

def atualizar_temp(temp_atual, aquecedor):
    if aquecedor:
        return temp_atual + 0.5 #Se o aquecedor estiver ligado, a temperatura ambiente aumenta em 0.5°C por ciclo
    else:
        return temp_atual - 0.1 #Se o aquecedor estiver desligado, a temperatura diminui em 0.1°C por ciclo
#Essa variação representa uma simplificação do mundo real.

while True:
    aquecedor_ligado = controlador(temp_atual, temp_desejada)
    temp_atual = atualizar_temp(temp_atual, aquecedor_ligado)

    if aquecedor_ligado:
        estado = "Ligado"
    else:
        estado = "Desligado"

    print("Temperatura atual:", round(temp_atual, 2), "°C")
    print("Aquecedor:",estado)

    time.sleep(1)    