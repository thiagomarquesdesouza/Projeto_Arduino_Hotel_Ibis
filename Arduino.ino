
const int led1 = 2;  // LED 1 no pino digital 2
const int led2 = 3;  // LED 2 no pino digital 3

String comando = "";

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  Serial.begin(9600);
  Serial.println("Arduino pronto para receber comandos.");
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      comando.trim();  // remove espaços extras
      
      if (comando == "acender 1") {
        digitalWrite(led1, HIGH);
        Serial.println("LED 1 aceso");
      } else if (comando == "apagar 1") {
        digitalWrite(led1, LOW);
        Serial.println("LED 1 apagado");
      } else if (comando == "acender 2") {
        digitalWrite(led2, HIGH);
        Serial.println("LED 2 aceso");
      } else if (comando == "apagar 2") {
        digitalWrite(led2, LOW);
        Serial.println("LED 2 apagado");
      } else {
        Serial.println("Comando não reconhecido");
      }

      comando = "";  // limpa o buffer
    } else {
      comando += c;  // acumula os caracteres
    }
  }
}



