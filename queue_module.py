import time
from process_module import Process
import memory_module
import io_module

all_process_queue = []
user_process_queue = []
real_time_process_queue= []
user_process_queue_1 = []
user_process_queue_2 = []
user_process_queue_3 = []
blocked_process_queue = []
quantum = 1
process_max_number = 1000
process_aging_times = 1
cpu = Process
queue_module_string = "queue_module => "


# identifica prioridade do processo e adiciona na fila de processos correspondente
def add_process_to_queue(process):
    all_process_queue.append(process)
    if(process.priority == 0):
        real_time_process_queue.append(process)
    if(process.priority == 1):
        user_process_queue.append(process)
        user_process_queue_1.append(process)
    if(process.priority == 2):
        user_process_queue.append(process)
        user_process_queue_2.append(process)
    if(process.priority >= 3):
        user_process_queue.append(process)
        user_process_queue_3.append(process)
    return


# escalonador de processos
def process_scheduling():
    global cpu
    if(len(all_process_queue) > 0):
        print (queue_module_string + "Escalonando...")
        if(len(all_process_queue) < process_max_number):
            check_real_time_queue()
        else:
            print(queue_module_string + "Erro fila suporta apenas 1000 elementos")
    else:
        print(queue_module_string + "Nenhum processo na fila.")
        time.sleep(1)
        process_scheduling()


# verifica se o proximo processo na cpu deve ser da fila de tempo real
# verifica o uso de dispositivos de entrada e saida do processo
def check_real_time_queue():
    global cpu
    if (len(real_time_process_queue) > 0):
        cpu = real_time_process_queue[0]
        real_time_process_queue.remove(cpu)
        if(io_module.check_process_necessary_input_output(cpu)):
            io_module.process_dispositives_to_busy(cpu)
            start_cpu_process()
        else:
            time.sleep(2)
            cpu.priority = 3
            add_process_to_queue(cpu)
            process_scheduling()
    else:
        check_queue_1()

# verifica se o proximo processo na cpu deve ser da fila de prioridade 1
# verifica o uso de dispositivos de entrada e saida do processo
def check_queue_1():
    global cpu,user_process_queue,user_process_queue_1
    if (len(user_process_queue) > 0):
        if (len(user_process_queue_1) > 0):
            cpu = user_process_queue_1[0]
            user_process_queue_1.remove(cpu)
            if(io_module.check_process_necessary_input_output(cpu)):
                io_module.process_dispositives_to_busy(cpu)
                start_cpu_process()
            else:
                time.sleep(2)
                cpu.priority = 3
                add_process_to_queue(cpu)
                process_scheduling()
        else:
            check_queue_2()

# verifica se o proximo processo na cpu deve ser da fila de prioridade 2
# verifica o uso de dispositivos de entrada e saida do processo
def check_queue_2():
    global cpu,user_process_queue_2
    if (len(user_process_queue_2) > 0):
        cpu = user_process_queue_2[0]
        user_process_queue_2.remove(cpu)
        if(io_module.check_process_necessary_input_output(cpu)):
            io_module.process_dispositives_to_busy(cpu)
            start_cpu_process()
        else:
            time.sleep(2)
            cpu.priority = 3
            add_process_to_queue(cpu)
            process_scheduling()
    else:
        check_queue_3()


# verifica se o proximo processo na cpu deve ser da fila de prioridade 3
# verifica o uso de dispositivos de entrada e saida do processo
def check_queue_3():
    global cpu,user_process_queue_3
    if (len(user_process_queue_3) > 0):
        cpu = user_process_queue_3[0]
        user_process_queue_3.remove(cpu)
        if(io_module.check_process_necessary_input_output(cpu)):
            io_module.process_dispositives_to_busy(cpu)
            start_cpu_process()
        else:
            cpu.priority = 3
            add_process_to_queue(cpu)
            process_scheduling()
    else:
        print(queue_module_string+ "Nenhum processo na fila")
        time.sleep(2)
        process_scheduling()


# alloca processo na cpu
# chama proximas etapas apos o tempo de quantum ter terminado
def start_cpu_process():
    global cpu
    continue_cpu_processing()
    process_scheduling()


# diminui prioridade do processo se ja foi allocado na cpu varias vezes
# evita starvation
def check_process_aging():
    global cpu,process_aging_times
    if (cpu.times_using_cpu >= process_aging_times):
        user_process_queue.append(cpu)
        if (cpu.priority == 0):
            real_time_process_queue.remove(cpu)
            user_process_queue_1.append(cpu)
        if (cpu.priority == 1):
            user_process_queue_1.remove(cpu)
            user_process_queue_2.append(cpu)
        if (cpu.priority == 2):
            user_process_queue_2.remove(cpu)
            user_process_queue_3.append(cpu)
        cpu.priority += 1
        cpu.times_using_cpu = 0
    else:
        cpu.times_using_cpu =+ 1


# continua a execucao do processo allocado na cpu
def continue_cpu_processing():
    global cpu
    time.sleep(3)
    cpu.resume_thread()
    quantum_time()
    if(cpu.priority != 0):
        cpu.pause_thread()
        verify_process_finished_execution()
    else:
        verify_process_finished_execution();


# verifica se processo terminou de executar se nao readiciona no final da fila
def verify_process_finished_execution():
    global cpu
    if (cpu.time_already_executed >= cpu.processing_time):
        memory_module.remove_process_from_memory(cpu)
        all_process_queue.remove(cpu)
        io_module.free_process_dispositives(cpu)
        if (cpu.priority > 1):
            user_process_queue.remove(cpu)
        if (cpu.priority == 0):
            cpu.pause_thread()
    else:
        check_process_aging()
        add_process_to_queue(cpu)


# tempo maximo que o processo pode ficar na cpu
def quantum_time():
    global quantum
    time.sleep(quantum)

