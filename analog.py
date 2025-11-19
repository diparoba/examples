from machine import ADC, Pin
import time

ADC_PIN = 34

pot = Pin(ADC_PIN) 
adc = ADC(pot)
adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)

while True:
    valor_adc = adc.read()
    print(f"Valor ADC : {valor_adc}")
    time.sleep(0.1)
