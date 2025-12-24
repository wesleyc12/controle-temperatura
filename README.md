# controle-temperatura
Simulação de controle de temperatura ON/OFF em Python
# Controle de Temperatura ON/OFF

## Objetivo
Simular um sistema simples de controle de temperatura do tipo ON/OFF, com foco no estudo de lógica de programação e conceitos básicos de sistemas embarcados.

## Descrição do Funcionamento
O sistema compara a temperatura atual com um valor de referência (setpoint).  
Quando a temperatura está abaixo do valor desejado, o aquecedor é ligado.  
Quando atinge ou ultrapassa o setpoint, o aquecedor é desligado.

A temperatura ambiente é simulada, aumentando ou diminuindo de forma gradual a cada ciclo de execução.

## Simplificações do Modelo
- Modelo térmico simplificado.
- Variações de temperatura fixas por ciclo.
- Sensor de temperatura simulado.
- Não considera inércia térmica nem ruído.

## Limitações
- Não possui histerese.
- Não utiliza controle PID.
- Sistema puramente simulado.

## Possíveis Melhorias
- Implementação de histerese.
- Integração com sensores reais.
- Migração para microcontroladores (Arduino/ESP).
