const int stepPin = 3;
const int dirPin  = 4;
const int enPin   = 5;
const int potPin  = A0;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enPin, OUTPUT);

  digitalWrite(enPin, LOW);   // enable driver (LOW usually means enabled)
  digitalWrite(dirPin, HIGH); // set initial direction
}

void loop() {
  int potVal = analogRead(potPin);  // reads 0–1023

  // Map potentiometer value to pulse delay (µs).
  // Higher pot value = shorter delay = faster rotation
  int delayTime = map(potVal, 0, 1023, 500, 1);

  digitalWrite(stepPin, HIGH);
  delayMicroseconds(delayTime);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(delayTime);
}
