

//tests the two dc motors

void setup() {
  //dc motors connected to pins 8 and 9
pinMode(9, OUTPUT);
pinMode(8, OUTPUT);

}

void loop() {
  //starts the motor, then stops it after a second's delay to test it
digitalWrite(9, HIGH);
digitalWrite(8, HIGH);
delay(1000);
digitalWrite(9, LOW);
digitalWrite(8, HIGH);
delay(1000);

}
