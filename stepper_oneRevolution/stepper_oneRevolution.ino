#include <Stepper.h>

const int stepsPerRevolution = 2048;

// try this order FIRST
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  Serial.begin(9600);
  myStepper.setSpeed(10);  // slow and stable 5 is good
}

void loop() {
  myStepper.step(1);  // continuous smooth rotation 1 is good
}