from process_module import Process
from queue_module import *
import time

number_of_memory_blocks = 1024
number_of_real_time_memory_blocks = 64
number_of_users_memory_blocks = 960
block_size = 1
memory = []
bit_map = []
memory_module_string = "memory_module => "
process_module_string = "process_module => "


# inicializa o mapa de bits com bits 0 ou com booleano falso
def initialize_bit_map():
    global number_of_memory_blocks
    for idx in range(0, number_of_memory_blocks-1):
        bit_map.append(False)


# verificando disponibilidade da memoria usando algoritmo first fit
def verify_memory_disponibility(process):
    global number_of_memory_blocks,bit_map
    size_counter = 0
    inserted = False

    # verifica se processo de tempo real, se nao memoria comeca a partir do bloco 64
    if(process.priority == 0):
        position = 0
    else:
        position = 64
    # percorre mapa de bits buscando um espaco vazio que caiba o processo
    while(inserted == False):
        if(position != number_of_memory_blocks-1):
            if(size_counter == int(process.allocated_blocks)):
                inserted = True
                add_process_to_memory(process,size_counter,position)
            if(bit_map[position] == False):
                size_counter += 1
            else:
                size_counter = 0
            position += 1
        else:
            # nao conseguiu encontrar espaco livre tenta novamente apos 1 segundo
            if (process.priority == 0):
                position = 0
            else:
                position = 64
            size_counter = 0
            print (memory_module_string + "Processo " + str(process.PID) + " nao encontrou espaco vazio na memoria")
            time.sleep(5)


# encontrou espaco suficiente na memoria alloca o processo
def add_process_to_memory(process,size_counter,position):
    process = save_process_offset(process,size_counter,position)
    memory.append(process)
    bit_maps_position_to_true(process)
    process.start_thread()
    add_process_to_queue(process)
    print(memory_module_string + "PID " + str(process.PID) + " inicializando...")
    time.sleep(cpu.initialization_time)
    print(memory_module_string + "PID " + str(process.PID) + " adicionado na memoria")


# salva em um processo o offset da localizacao na memoria
def save_process_offset(process,size_counter,position):
    process.offset = position - size_counter
    return process


# remove um processo da memoria e trocas os bits correspondente do bitmap para liberado
def remove_process_from_memory(process):
    memory.remove(process)
    bit_maps_position_to_false(process)
    print(process_module_string + "PID " + str(process.PID) + " finished execution")
    print(memory_module_string + "PID " + str(process.PID) + " retirado da memoria")


# seta os bits do bitmap para ocupado na regiao de memoria em que o processo foi inserido
def bit_maps_position_to_true(process):
    for position in range(process.offset,process.offset+process.allocated_blocks):
        bit_map[position] = True


# seta os bits do bitmap para liberado na regiao de memoria em que o processo foi inserido
def bit_maps_position_to_false(process):
    for position in range(process.offset,process.offset+process.allocated_blocks):
        bit_map[position] = False


