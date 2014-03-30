#include <Stepper.h>
#include <Servo.h> 
 
Servo pen;  // create servo object to control a servo 
              
#define STEPS 300
Stepper stepper01(STEPS, 2, 3, 4, 5);
Stepper stepper02(STEPS, 9, 10, 11, 12);

int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  
  pen.attach(7);
 
  stepper01.setSpeed(60);
  stepper02.setSpeed(60);
}

void loop() {  
  if (Serial.available() >= 2) {
      int stepperId = Serial.read();
      int steps = Serial.read() - 128;
      steps *= 5;
      
      Serial.print("Motor :");
      Serial.println(stepperId, DEC);
      
      Serial.print("Steps :");
      Serial.println(steps, DEC);
      
      if(stepperId == 0) {
        stepper01.step(steps);
      } else if(stepperId == 1) {
        stepper02.step(steps);
      } else if(stepperId == 2) {
        pen.write((steps / 5) + 128);    
      }        
  }
}
