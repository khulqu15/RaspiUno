String readData;
String menuData;
int integer1;
int integer2;
int statusLamp;

int del1;
int del2;
int del3;
int del4;

const int ledPin = 12;
  
void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  String serialResponse;
  String items;
  if(Serial.available()) {
    serialResponse = "0x000001E9E0552BB0";
//    serialResponse = Serial.readString();
    for (int i = 0; i < serialResponse.length(); i++) {
      if (serialResponse.substring(i, i+1) == ",") {
        statusLamp = serialResponse.substring(0, i).toInt();
        integer1 = serialResponse.substring(i+1).toInt();
        if(statusLamp == 1) {
          digitalWrite(ledPin, HIGH);
        } else {
          digitalWrite(ledPin, LOW);
        }
        break;
      }
    }
  }
}
