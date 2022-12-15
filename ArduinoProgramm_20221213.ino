#include <SparkFun_LIS331.h>
#include <Wire.h>
#include <SoftwareSerial.h>
String message;
#define HWSERIAL Serial
//#define tx 0
//#define rx 1

LIS331 xl;

void setup() 
{
  HWSERIAL.begin(9600);
  Wire.begin();
  xl.setI2CAddr(0x19);    // This MUST be called BEFORE .begin() so 
                          //  .begin() can communicate with the chip
  xl.begin(LIS331::USE_I2C); // Selects the bus to be used and sets
                          //  the power up bit on the accelerometer.
                          //  Also zeroes out all accelerometer
                          //  registers that are user writable.
  LIS331::NORMAL;
  LIS331::DR_1000HZ;
  Serial.begin(9600);
}

void loop() 
{
  int16_t x, y, z;
    xl.readAxes(x, y, z);  // The readAxes() function transfers the
                           //  current axis readings into the three
                           //  parameter variables passed to it.
    //Serial.println(x);
    //Serial.println(y);
    //Serial.println(z);
    //Serial.println(xl.convertToG(6,x)); // The convertToG() function
    //Serial.println(xl.convertToG(6,y)); // accepts as parameters the
    Serial.println(xl.convertToG(6,z)); // raw value and the current
    //Serial.println(" ");                // maximum g-rating.

      while(HWSERIAL.available())
  {//while there is data available on the serial monitor
    message+=char(HWSERIAL.read());//store string from serial command
  }
  if(message!="")
  {
      Serial.println(">" + message); //show the data
      HWSERIAL.println(message); //show the data
    }
  }
