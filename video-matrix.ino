#include "Arduino_LED_Matrix.h"
#include "badapple.h"

ArduinoLEDMatrix matrix;
unsigned long oldTime;

int Reset = 12;
String res;

void setup() {
  Serial.begin(9600);  
  Serial.setTimeout(1000);
  matrix.loadSequence(animation);
  matrix.begin();
  oldTime = millis();
  Serial.println(oldTime);
  matrix.play(false);
}

void loop() {
  /*
  if(matrix.sequenceDone())
    Serial.println(millis() - oldTime);

  if (Serial.available()){
    res = Serial.readString();
    if ("RESET\n" == res){
      Serial.println("Condition HIT");
      // something to reset
    }
  }
  */
}
