void setup()
{
    //Configurar un pin como entrada
    pinMode(A0, INPUT);
    //Iniciar comunicación serial
    Serial.begin(9600);
}
void loop()
{
    //Leer el valor analógico del pin A0
    int valor = analogRead(A0);
    //Enviar el valor leído por el puerto serial
    Serial.println(valor);
    //Esperar 500 milisegundos 
    delay(500);
}