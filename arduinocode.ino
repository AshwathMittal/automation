void setup() {
  pinMode(9, OUTPUT);
  pinMode(8, INPUT);
}

void loop() {
  digitalRead(8);
  if (digitalRead(8) == HIGH) {
    // turn Fan on:
    digitalWrite(9, HIGH);
  } else {
    // turn Fan off:
    digitalWrite(9, LOW);
  }
}
