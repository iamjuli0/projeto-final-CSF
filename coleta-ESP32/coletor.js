const { SerialPort } = require('serialport');
const { ReadlineParser } = require('@serialport/parser-readline');
const fs = require('fs');
const readline = require('readline-sync');

// === CONFIGURAÇÃO ===
const portaSerial = '/dev/ttyUSB0'; // Altere conforme necessário
const baudrate = 115200;
const caminhoCSV = 'dadosTP.csv';
const NUM_REDES = 10;

let port;
let parser;

// === CABEÇALHO DO CSV ===
if (!fs.existsSync(caminhoCSV)) {
    const header = ['Ponto', 'Amostra'];
    for (let i = 1; i <= NUM_REDES; i++) {
      header.push(`SSID${i}`, `RSSI${i}`);
    }
    fs.writeFileSync(caminhoCSV, header.join(',') + '\n');
  }
  

// === CONEXÃO COM A SERIAL ===
function conectarSerial() {
  try {
    port = new SerialPort({
      path: portaSerial,
      baudRate: baudrate,
      autoOpen: false
    });

    port.open((err) => {
      if (err) {
        console.error(`❌ Erro ao abrir ${portaSerial}:`, err.message);
        return;
      }

      console.log(`✅ Conectado à ${portaSerial}. Aguardando estabilização...`);
      setTimeout(() => {
        console.log('✅ Estabilização concluída.\n');
        solicitarPonto();
      }, 2000);
    });

    parser = port.pipe(new ReadlineParser({ delimiter: '\r\n' }));

    parser.on('data', (linha) => {
      if (linha.startsWith('[INFO]')) return;

      if (linha === 'FIM') {
        console.log('📍 Coleta finalizada!\n');
        solicitarPonto(); // pede o próximo ponto
      } else {
        fs.appendFileSync(caminhoCSV, linha + '\n');
        console.log(`[CSV] ${linha}`);
      }
    });

    port.on('error', (err) => {
      console.error('Erro na porta serial:', err.message);
    });

  } catch (e) {
    console.error(`Erro inesperado ao conectar na serial: ${e.message}`);
  }
}

// === SOLICITA O PRÓXIMO PONTO ===
function solicitarPonto() {
  const ponto = readline.question('Digite o nome do ponto (ex: RP ou TP): ');
  port.write(ponto.trim() + '\n');
  console.log(`➡️  Nome "${ponto}" enviado ao ESP32. Coleta em andamento...\n`);
}

conectarSerial();