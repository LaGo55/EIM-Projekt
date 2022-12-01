 *                 == MASTER CODE ==

 HC05 Configuration:

#include <SoftwareSerial.h>
#define tx 2
#define rx 3
SoftwareSerial configBt(rx, tx); // RX, TX

#include 
// H3LIS331DL I2C address is 0x18(24)
#define Addr 0x18
void setup()
{  
// Initialise I2C communication as MASTER  
Wire.begin();  
// Initialise Serial Communication, set baud rate = 9600  
Serial.begin(9600);

configBt.begin(9600);
pinMode(tx, OUTPUT);
pinMode(rx, INPUT);

// Start I2C Transmission  
Wire.beginTransmission(Addr);  
// Select control register 1  
Wire.write(0x20);  
// Enable X, Y, Z axis, power on mode, data output rate 50Hz  
Wire.write(0x27);  
// Stop I2C Transmission  
Wire.endTransmission();
  // Start I2C Transmission  
Wire.beginTransmission(Addr);  
// Select control register 4  
Wire.write(0x23);  
// Set full scale, +/- 100g, continuous update 
Wire.write(0x00);  
// Stop I2C Transmission  
Wire.endTransmission();  
delay(300);
}
void loop()
{  
unsigned int data[6];  
for(int i = 0; i < 6; i++)  
{    
// Start I2C Transmission    
Wire.beginTransmission(Addr);    
// Select data register    
Wire.write((40+i));    
// Stop I2C Transmission    
Wire.endTransmission();
// Request 1 byte of data    
Wire.requestFrom(Addr, 1);    
// Read 6 bytes of data    
// xAccl lsb, xAccl msb, yAccl lsb, yAccl msb, zAccl lsb, zAccl msb    
if(Wire.available() == 1)    
{      
data[i] = Wire.read();    
}  
}  
Serial.write(data,i);  
bt.write(data,i)
delay(300);
}
