#include <Adafruit_NeoPixel.h>
#define PIN 13
#define RGBPIX 9
#define LEDSTRENGTH 5
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(9, PIN, NEO_GRB + NEO_KHZ800);
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define SCREEN_WIDTH 128 /*OLED display width 128, in pixels*/
#define SCREEN_HEIGHT 64 /*OLED display height 64, in pixels*/
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1); /*SSD1306 display connected at I2C pins (SDA, SCL)*/

#include <WiFi.h>
#include <WiFiMulti.h>
WiFiMulti wifiMulti;

//storing the WiFi crenentials
// const char* ssid = "Vinshtok";
// const char* password = "Natan92695";

const char* ssid = "Myphone";
const char* password = "something";

WiFiServer wifiServer(80);

// WiFi connect timeout per AP. Increase when connecting takes longer.
const uint32_t connectTimeoutMs = 10000;
int iterator = 1;
int nloop = 0;
int numPixels = 9;
int strength = 10;

int charCounter = 0;
int meslen=1000;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n");
  Serial.println("\n");
  WiFi.mode(WIFI_AP_STA);
  setRed(strength,numPixels);
  Serial.println("starting the code");

  WiFi.softAP(ssid, password);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..Base Network");
  }
  
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { /*I2C Address for OLED display*/
    Serial.println(F("SSD1306 allocation failed"));
      for(;;);
    }
  delay(2000);
  display.clearDisplay();  /*Clear previous display*/
  display.setTextSize(2);  /*OLED display text size defined*/
  display.setTextColor(WHITE); /*OLED display text color*/
  display.setCursor(0, 20); /*Display static text*/
  display.println("Connected");  /*String to represent on OLED display*/
  setGreen(strength,numPixels);
  display.display();

  Serial.println("Connected to the WiFi network");
  Serial.println("\n");
  Serial.println("version 8\n");
  //find ip adress of esp32
  Serial.println(WiFi.localIP());
  Serial.println("ip adress of ESP");
  Serial.println(WiFi.localIP());

  wifiServer.begin();
  Serial.println("\n");



//   wifiMulti.addAP("ATID", "atid1010"); //add list of networds
//   wifiMulti.addAP("ssid_from_AP_2", "your_password_for_AP_2");
//   wifiMulti.addAP("ssid_from_AP_3", "your_password_for_AP_3");
  //WiFi.scanNetworks will return the number of networks found
  nloop = WiFi.scanNetworks();
  Serial.println("scan done");
  if (nloop == 0) {
      Serial.println("no networks found");
  } 
  else {
    Serial.print(nloop);
    Serial.println(" networks found");
    for (int i = 0; i < nloop; ++i) {
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      
      //find the network name
      Serial.print(WiFi.SSID(i));
      Serial.print("\n");
      
      // find Signal Strength Indicator
      Serial.print(" signal strength: ");
      Serial.print(WiFi.RSSI(i));
      Serial.print(" dBm");
      Serial.print("\n");
      // Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN)?" ":"*");
      
      //print wifi channel for each network found
      Serial.print(" channel:");
      Serial.print(WiFi.channel(i));
      Serial.print("\n");
      delay(10);
    }
  }

  // // Connect to Wi-Fi using wifiMulti (connects to the SSID with strongest connection)
  // Serial.println("Connecting Wifi...");
  // if(wifiMulti.run() == WL_CONNECTED) {
  //   Serial.println("");
  //   Serial.println("WiFi connected");
  //   Serial.println("IP address: ");
  //   Serial.println(WiFi.localIP());
  // }
 }

void loop() {
  if(iterator % 100000 == 0){
    nloop = WiFi.scanNetworks();
    delay(1000);
  }
  else
  {
    iterator++;
  }
   //check if client is connected
  WiFiClient client = wifiServer.available();
  if (client) {

    while (client.connected()) {
      while (client.available()>0) {
        //send MAC address
        String m=WiFi.macAddress();
        char ma[m.length()];
        m.toCharArray(ma, (m.length() + 1));
        Serial.println("starting to send mac");        
        for (int i = 0; i < m.length() + 1; i++){
          delay(10);
          client.write(ma[i]);
          charCounter++;
          Serial.print(ma[i]);

        }
        Serial.print("\n");
        Serial.println("done with sending mac");
        delay(10);
        client.write("*");
        delay(10);

        charCounter+=1;
      for(int z=0; z < nloop ; z++){
          Serial.print("starting network number: ");
          Serial.print(z);
        //send SSID= wifi network name
          String ssid=WiFi.SSID(z);
          char ssidSend[ssid.length()];
          ssid.toCharArray(ssidSend, (ssid.length() + 1));
          for (int i = 0; i < ssid.length() + 1; i++){
            //Serial.println(ma[i]);
            delay(20);
            client.write(ssidSend[i]);
            charCounter++;
            Serial.print(ssidSend[i]);
          } 
          Serial.println("\n");
          Serial.println("done with sending ssid");
          client.write("*");

          charCounter+=1;

          //send RSSI= signal strength indicator
          int rssi=WiFi.RSSI(z);
          Serial.println(WiFi.RSSI(z));
          char rssiSend[10];
          // itoa(rssi,rssiSend,10);
          String strssi=String(rssi);
          Serial.println(strssi);

          strssi.toCharArray(rssiSend, 10);
          Serial.println("starting rssi loop");
          // rssi.toCharArray(rssiSend, (2 + 1));
          for (int i = 0; i < strssi.length(); i++){
            //Serial.println(ma[i]);
            delay(10);
          // Serial.println("sending rssi");
          //  Serial.println(rssiSend[i]);
            client.write(rssiSend[i]);
            charCounter++;
          }  
          Serial.println("done with sending rssi");
          client.write("*");

          charCounter++;


          // send wifi channel
          int channel=WiFi.channel(z);
          Serial.println(WiFi.channel(z));
          char channelSend[10];
          String stch=String(channel);
          Serial.println(stch);
          stch.toCharArray(channelSend, 10);
          Serial.println("starting channel loop");     
          // wifiC.toCharArray(ssidSend, (wifiC.length() + 1));
          for (int i = 0; i < stch.length() + 1; i++){
            //Serial.println(ma[i]);
            delay(10);
            Serial.print(channelSend[i]);
            client.write(channelSend[i]);
            charCounter++;
          }
          Serial.println("done with sending channel");
          client.write("*");

      }
      for (int i=0; i<(meslen-charCounter);i++){
            client.write("*");
      }       
      }
      delay(10);
    }


    client.stop();
    Serial.println("Client disconnected");

  // //if the connection to the stongest hotstop is lost, it will connect to the next network on the list
  // if (wifiMulti.run(connectTimeoutMs) == WL_CONNECTED) {
  //   Serial.print("WiFi connected: ");
  //   Serial.print(WiFi.SSID());
  //   Serial.print(" ");
  //   Serial.println(WiFi.RSSI());
  // }
  // else {
  //   Serial.println("WiFi not connected!");
  // }
  // delay(1000);
  }
}

// char* send2PY(String a)
// {
//   Serial.println("Hi, I got to the function\n");
//   Serial.println(a);
//   char temp[a.length()];
//   a.toCharArray(temp, (a.length() + 1));
//   for (int i = 0; i < a.length() + 1; i++){
//     Serial.println(temp[i]);
//     delay(1000);
//   }    
//   return temp;
// }  
void setGreen(int s, int n)
{
  for (int count = 0; count < n; count++)
  {
    pixels.setPixelColor(count, pixels.Color(0, s, 0)); // Moderately bright green color.
    pixels.show(); // This sends the updated pixel color to the hardware.              //red , green, blue
  }
}

 

void setRed(int s, int n)

{
  for (int count = 0; count < n; count++)
  {
    pixels.setPixelColor(count, pixels.Color(s, 0, 0)); // .
    pixels.show(); // This sends the updated pixel color to the hardware.              //red , green, blue
  }
}
