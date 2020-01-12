
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 10, 5, 4, 6, 2);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void loop() {
  // Print a message to the LCD.
  pill = user.getpill();
  lcd.print("the pill you must take now is " + pill);
}


