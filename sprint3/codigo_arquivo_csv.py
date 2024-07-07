import serial      #importa a biblioteca do arduino
import datetime    #importa a biblioteca de data e hora

porta = "COM3"    #porta do arduino conectada ao computador
baud = 9600       #baud rate
arquivo = "logger.csv"   #arquivo .csv em que serão colocados os dados

ser = serial.Serial(porta,baud)    #variável correspondente ao sensor
ser.flushInput()      #limpa a entrada caso tenha um dado fora do padrão
print("Abrindo Serial")

tabelas = "Data;Hora;Temperatura(C°);Umidade(%)\n"     #primeira linha do arquivo .csv
print(tabelas)
file = open(arquivo,"a")     #abre o arquivo .csv
file.write(tabelas)     #escreve a primeira linha do arquivo .csv

amostra = 70      #quantidade de dados que serão armazenados
linha = 0
while linha <= amostra:      #loop para armazenar os dados
    agora = datetime.datetime.now()    #armazena o dia e a hora
    agora_string = agora.strftime("%d/%m/%Y;%H:%M:%S;")     #tratamento da string do dia e hora
    sensor = str(ser.readline().decode("utf-8"))     #leitura dos dados do sensor
    dados = agora_string + sensor   #concatenação dos dados que serão escritos
    dados1 = dados[0:33]     #tratamento para os dados serem escritos linha por linha
    print(dados1)
    file.write(dados1)     #escreve o dado no arquivo .csv
    linha = linha+1    #incremento para o loop

print("Final de leituras")
file.close()
ser.close()
