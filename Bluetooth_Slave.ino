
 *                 == SLAVE CODE ==

HC05 Configuration:

#include <SoftwareSerial.h>
#define tx 2
#define rx 3
SoftwareSerial configBt(rx, tx); // RX, TX

void setup() {
  Serial.begin(9600);
  configBt.begin(9600);
  pinMode(tx, OUTPUT);
  pinMode(rx, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  Serial.readBytes(data,i)
  Serial.println(bt.read());
  Serial.println(data)
  delay(300);
  // Convert the data 
  int xAccl = ((data[1] * 256) + data[0]);  
  int yAccl = ((data[3] * 256) + data[2]);  
  int zAccl = ((data[5] * 256) + data[4]);
  // Output data to serial monitor  
  Serial.print("Acceleration in X-Axis : ");  
  Serial.println(xAccl);  
  Serial.print("Acceleration in Y-Axis : ");  
  Serial.println(yAccl);  
  Serial.print("Acceleration in Z-Axis : ");  
  Serial.println(zAccl);
  // put your main code here, to run repeatedly:

}
