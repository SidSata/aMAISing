void setup() {
  // put your setup code here, to run once:
pinMode(9, OUTPUT);
pinMode(8, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(9, HIGH);
digitalWrite(8, HIGH);
delay(1000);
digitalWrite(9, LOW);
digitalWrite(8, HIGH);
delay(1000);

}
