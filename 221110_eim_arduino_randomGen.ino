long randNumber;
float randTemp;
int x;

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  
  randNumber = random(90,110);
  randTemp = random(19.0,22.0);
  Serial.print(randNumber);
  Serial.print(",");
  Serial.println(randTemp);

  delay(50);
  
  if (x>100) {
    randNumber = random(0,150);
    Serial.print(randNumber);
    Serial.print(",");
    Serial.println(randTemp);

    x = 0;
  };
  x = x+1;
}