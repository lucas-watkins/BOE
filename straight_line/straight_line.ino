#include "Servo.h"

Servo leftServo;
Servo rightServo;
Servo middleServo;

void setup() {
  // put your setup code here, to run once:
  leftServo.attach(13);
  rightServo.attach(12);
  middleServo.attach(11);
}

void loop() {
  // put your main code here, to run repeatedly:
  leftServo.write(180);
  rightServo.write(60);
  for (int i = -270; i < 180; i++){
    delay(50);
    middleServo.write(i);
  }
}
