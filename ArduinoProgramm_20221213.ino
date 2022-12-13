#include <SoftwareSerial.h>
SoftwareSerial BT(10, 11); 
char a; // variable to store messages
void setup()  
{
  BT.begin(9600);                    // set the data rate for the SoftwareSerial port
  BT.println("Hello from Arduino");  // send wellcome message to other device
}
void loop() 
{
  // if text arrived in from BT serial...
  if (BT.available()){
    a=(BT.read());             // store incoming character from other device
    if (a=='1'){               //when send character 1 then...
      BT.println("send 1");
    } else if (a=='2'){        //when send character 2 then...
      BT.println("send 2");
    } else {                   // otherwise print this description...
      BT.println("Send '1' or '2'");
    }   
  }
}
