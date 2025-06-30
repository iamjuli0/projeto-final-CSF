# Comunicação sem Fio
**📘 Projeto Final da disciplina de Comunicação Sem Fio**

**👨‍🏫 Professor: Celso Barbosa Carvalho**

**👥 Alunos:**
  - Daniel Silveira Gonzalez
  - Júlio Melo Campos
## 📜 Descrição
Neste seguinte trabalho, foi documentado todos os datasets e códigos utilizados para a efetuação do projeto, que utilizou o uso de um microcontrolador ESP32 com um módulo Wi-Fi para captação de Access Points para estudo de caso no algoritmo k-NN. Tais dados que formam os datasets foram capturados no 1° andar do CETELI-1 da Faculdade de Tecnologia.
## 🗂 Como se organizam os datasets?
Na pastas datasets, há presença de seis arquivos onde foram coletados para o experimento:
  - **dadosRP.csv:** representa a saída bruta do ESP32, com a presença de espaços em branco quando o sinal de RSSI não foi encontrado para determinado AP.
  - **dadosRP_corrigido.csv:** representa a saída em que os espaços em branco foram preenchidos com -100 dBm, indicando a ausência de sinal. Essa correção foi realizada utilizando o código completar.py.
  - **dadosRP_final.csv:** representa a saída filtrada com os 10 SSIDs mais frequentes, utilizando o código filtroSSID.py, para serem utilizados no código knn.py.

**Observação:** As informações acima se aplicam para os dadosTP.
## 📥 Coleta
Na pasta coleta-ESP32, foi documentado a codificação para a coleta que deu como resultado os datasets utilizados
  - **coleta.js:** Com este, faz a conexão com a serial e filtra os dados vindos do coleta-RSSI.ino a cada 120 amostras, solicitando o nome do ponto onde foi coletado (ex: RPs ou TPs) e coloca no formato .csv
  - **coleta-RSSI.ino:** Faz a comunicação da Wi-Fi com o ESP32 para coleta de dados, coletando 120 amostras das 10 redes com maior RSSI no instante.

