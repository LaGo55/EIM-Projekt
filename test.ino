String message; //string that stores the incoming message
#define HWSERIAL Serial1
const int ledPin = 11;

void setup()
{
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);   // set the LED on
  Serial.begin(9600); //set baud rate
  HWSERIAL.begin(9600);
  HWSERIAL.println("Bereit");
}

void loop()
{
  while(Serial.available())
  {//while there is data available on the serial monitor
    message+=char(Serial.read());//store string from serial command
  }
  if(!Serial.available())
  {//This comes from the console
    if(message!="")
    {//if data is available
      Serial.println("<" + message); //show the data
      HWSERIAL.print(message); //show the data
      message=""; //clear the data
    }
  }

  while(HWSERIAL.available())
  {//while there is data available on the serial monitor
    message+=char(HWSERIAL.read());//store string from serial command
  }
  if(!HWSERIAL.available())
  {//This comes from the bluetooth device (such as phone)
    if(message!="")
    {//if data is available
      Serial.println(">" + message); //show the data
      HWSERIAL.println(message); //show the data
      if(message=="0") digitalWrite(ledPin, LOW);    // set the LED off
        else HWSERIAL.println("Nix gut diese");
      if(message=="1") digitalWrite(ledPin, HIGH);    // set the LED on
        else HWSERIAL.println("Nix gut diese");
      //message=""; //clear the data
    }
  }

  delay(2000); //delay
}
