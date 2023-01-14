#include <SparkFun_LIS331.h>
#include <Wire.h>
#include <SoftwareSerial.h>
String message;
#define HWSERIAL Serial1

LIS331 xl;
//AT+BAUD8;

const int RunningAverageCount = 100;
float RunningAverageBufferZ[RunningAverageCount];
float RunningAverageBufferY[RunningAverageCount];
int NextRunningAverage;

void setup() 
{
  Serial.begin(9600);
  Wire.begin();
  xl.setI2CAddr(0x19);    // This MUST be called BEFORE .begin() so 
                          //  .begin() can communicate with the chip
  xl.begin(LIS331::USE_I2C); // Selects the bus to be used and sets
                          //  the power up bit on the accelerometer.
                          //  Also zeroes out all accelerometer
                          //  registers that are user writable.
  xl.setPowerMode(LIS331::NORMAL);
  xl.setODR(LIS331::DR_400HZ);
  HWSERIAL.begin(9600);
}

void loop() 
{
    int16_t x, y, z;
    xl.readAxes(x, y, z);  // The readAxes() function transfers the
                           //  current axis readings into the three
                           //  parameter variables passed to it.

    xl.setHighPassCoeff(LIS331::HPC_64);
    xl.enableHPF(true);
    
    float y_g = xl.convertToG(100,y);
    float z_g = xl.convertToG(100,z);

    // Averaging the raw acceleration data before printing out

    float RawAccelerationZ = z_g;
    float RawAccelerationY = y_g;
    RunningAverageBufferZ[NextRunningAverage++] = RawAccelerationZ;
    RunningAverageBufferY[NextRunningAverage++] = RawAccelerationY;

    if (NextRunningAverage >= RunningAverageCount)
    {
      NextRunningAverage = 0; 
    }
    float RunningAverageAccelerationZ = 0;
    float RunningAverageAccelerationY = 0;
    for(int i=0; i < RunningAverageCount; ++i)
    {
     RunningAverageAccelerationZ += RunningAverageBufferZ[i];
     RunningAverageAccelerationY += RunningAverageBufferY[i];
    }
    RunningAverageAccelerationZ /= RunningAverageCount;
    RunningAverageAccelerationY /= RunningAverageCount;
 
    
    //Serial.println(x);
    //Serial.println(y);
    //Serial.println(z);
    //Serial.println(xl.convertToG(100,x)); // The convertToG() function
    //Serial.println(xl.convertToG(100,y)); // accepts as parameters the
    //Serial1.print(z_g);// raw value and the current
    Serial1.print(RunningAverageAccelerationZ);
    Serial1.print(",");
    Serial1.println(RunningAverageAccelerationY);
    // Serial.println(" ");  // maximum g-rating. 

}
