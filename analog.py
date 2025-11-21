from machine import ADC, Pin 
import time

POT_PIN = 32 # Pin conectado al potenciómetro

pot = Pin(POT_PIN) # Configurar el pin como entrada ADC
adc_pot = ADC(pot) # Crear objeto ADC
adc_pot.width(ADC.WIDTH_12BIT) # Configurar de 0 a 4095
adc_pot.atten(ADC.ATTN_11DB) # Rango de voltaje de 0 a 3.6V

while True:
    valor_pot = adc_pot.read() # Leer valor del potenciómetro
    print(f"Valor POT : {valor_pot}") # Imprimir valor leído
    time.sleep(0.1) # Esperar 100 ms antes de la siguiente lectura
