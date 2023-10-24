#include "Servo.h"
//declare re-usable input variable
char input;
const int delay_period = 250;

//declare servos
Servo rightServo;
Servo leftServo;
Servo midServo;

void setup() {
  //initalize serial port and print welcome message
  Serial.begin(115200); 
  delay(50); 
  Serial.println("BOE is Ready");
}
 
void loop() {
  // runs if serial available 
  if(Serial.available()){
    //gather input
    input = Serial.read();

    //moves robot forward
    if (input == 'w'){
      rightServo.attach(13);
      leftServo.attach(12);
      rightServo.write(180);
      leftServo.write(0);
      delay(delay_period);
      rightServo.detach();
      leftServo.detach();
    }

    //moves robot backwards
    if (input == 's'){
      rightServo.attach(13);
      leftServo.attach(12);
      rightServo.write(0);
      leftServo.write(180);
      delay(delay_period);
      rightServo.detach();
      leftServo.detach();
    }

    // pivots robot to the right
    if (input == 'd'){
      leftServo.attach(13);
      leftServo.write(180);
      delay(delay_period);
      leftServo.detach();
    }

    // pivots robot to the left
    if (input == 'a'){
      rightServo.attach(12);
      rightServo.write(0);
      delay(delay_period);
      rightServo.detach();
    }

    //pivots middle servo to the right
    if (input == 'l'){
      midServo.attach(11);
      midServo.write(0);
      delay(delay_period);
      midServo.detach();
    }
    //pivots middle servo to the left
    if (input == 'k'){
      midServo.attach(11);
      midServo.write(180);
      delay(delay_period);
      midServo.detach();
    }
  }
}