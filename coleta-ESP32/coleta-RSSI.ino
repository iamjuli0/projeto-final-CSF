#include <WiFi.h>
#include <vector>

const int NUM_REDES = 10;  // <<<<< ALTERE AQUI SE QUISER MUDAR A QUANTIDADE

String pontoAtual = "";

bool ssidJaAdicionado(std::vector<String>& lista, String ssid) {
  for (auto& s : lista) {
    if (s == ssid) return true;
  }
  return false;
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect(); 
  delay(100);
}

void loop() {
  if (Serial.available()) {
    pontoAtual = Serial.readStringUntil('\n');
    pontoAtual.trim();

    for (int i = 1; i <= 120; i++) {
      int n = WiFi.scanNetworks();
      std::vector<String> ssids;
      std::vector<int> rssis;

      for (int j = 0; j < n && ssids.size() < NUM_REDES; j++) {
        String ssidAtual = WiFi.SSID(j);
        if (!ssidJaAdicionado(ssids, ssidAtual)) {
          ssids.push_back(ssidAtual);
          rssis.push_back(WiFi.RSSI(j));
        }
      }

      Serial.print(pontoAtual);
      Serial.print(",");
      Serial.print(i);
      Serial.print(",");
      for (int j = 0; j < ssids.size(); j++) {
        Serial.print(ssids[j]);
        Serial.print(",");
        Serial.print(rssis[j]);
        if (j < ssids.size() - 1 || ssids.size() < NUM_REDES) Serial.print(",");
      }
      for (int k = ssids.size(); k < NUM_REDES; k++) {
        Serial.print(",,");
      }
      Serial.println();

      delay(100);  // ajuste se quiser amostragem mais rápida
    }

    Serial.println("FIM");
  }
}
