from threading import Thread
import sys
from memory_module import *
from queue_module import *


PID = 0

# abre o arquivo de entrada e cria uma lista com os dados de cada linha(processo) do arquivo
def read_file():
    [filename] = sys.argv[1:]
    linhas = [linha.rstrip('\n') for linha in open(filename)]
    print "Starting Dispatcher"
    print "Dispatcher Started"
    for linha in linhas:
        create_process(linha)
        #slow execution prints
        time.sleep(3)
    return


# recebe cada linha lida, cria uma processo novo com os dados
# verifica disponibilidade de memoria para o processo
def create_process(linha):
    global PID
    valores = linha.split(",")
    #impede processsos de prioridade 0 usarem dispositivos de io
    if(int(valores[1]) == 0):
        process = Process(PID, valores[1], 0, valores[3], valores[0],
                            valores[2], 0, 0, 0, 0)
    else:
        process = Process(PID,valores[1],0,valores[3],valores[0],
                            valores[2],valores[4],valores[5],valores[6],valores[7])
    verify_memory_disponibility(process)
    PID += 1
    return

def start_modules():
    if __name__ == "__main__":
        scheduling_thread = Thread(target=process_scheduling, args=())
        memory_thread = Thread(target=read_file, args=())
        # leitura do arquivo, criacao dos processos e inicio da gerencia de memoria
        memory_thread.start()
        # inicio do escalonamento de processos
        time.sleep(5)
        scheduling_thread.start()

# main code

# inicializa bitmaps e semaforos
initialize_bit_map()
# cria as threads bases de execucao dos modulos do programa
start_modules()
