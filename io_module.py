import queue_module
# variaveis globais do modulo de input output
# 1 ocupado 0 livre
# -1 sendo usado por nenhum processo
scanner = 0
process_using_scanner = -1
printer_1 = 0
process_using_printer_1 = -1
printer_2 = 0
process_using_printer_2 = -1
sata_dispositive_1 = 0
process_using_sata_dispositive_1 = -1
sata_dispositive_2 = 0
process_using_sata_dispositive_2 = -1
modem = 0
process_using_modem = -1
io_module_string = "io_module => "

# faz a verificacao de dispositivos necessarios para o processo
# verifica se algum outro processo ja esta utilizando o dispositivo
def check_process_necessary_input_output(process):
    global scanner,printer_1,printer_2,sata_dispositive_1,sata_dispositive_2
    if(check_scanner(process) == False):
        print(io_module_string + "PID " + str(process.PID) + " Aguardando Scanner Ocupado")
        return False

    if(check_printers(process) == False):
        print(io_module_string + "PID " + str(process.PID) + " Aguardando Impressora Ocupada")
        return False

    if(check_sata_dispositive(process) == False):
        print(io_module_string + "PID " + str(process.PID) + " Aguardando Dispositivo Sata Ocupado")
        return False

    if(check_modem(process) == False):
        print(io_module_string + "PID " + str(process.PID) + " Aguardando Modem Ocupado")
        return False
    return True

# verifica se o processo precisa do scanner
# verifica se o scanner ja esta em uso por outro processo
def check_scanner(process):
    global scanner
    result = True
    if(process.using_scanner == 0):
        result = True
    else:
        if(scanner == 0):
            result =  True
        else:
            if(process_using_scanner != process.PID):
                result =  False
    return result

# verifica se o processo precisa do modem
# verifica se o modem ja esta em uso por outro processo
def check_modem(process):
    global modem
    result = True
    if(process.using_modem == 0):
        result = True
    else:
        if(modem == 0):
            result =  True
        else:
            if(process_using_modem != process.PID):
                result =  False
    return result

# verifica se o processo precisa de alguma das impressoras
# verifica se a impressora ja esta em uso por outro processo
def check_printers(process):
    global printer_1,printer_2
    result = True
    if(process.using_printer == 0):
        result = True
    else:
        if(process.using_printer == 1):
            if(printer_1 == 0):
                result =  True
            else:
                if (process_using_printer_1 != process.PID):
                    result = False

        if(process.using_printer == 2):
            if(printer_2 == 0):
                result =  True
            else:
                if (process_using_printer_2 != process.PID):
                    result = False
    return result

# verifica se o processo precisa de algum dos dispositivos sata
# verifica se o dispositivo ja esta em uso por outro processo
def check_sata_dispositive(process):
    global sata_dispositive_1,sata_dispositive_2
    result = True
    if (process.using_sata_dispositive == 0):
        result = True
    else:
        if (process.using_sata_dispositive == 1):
            if (sata_dispositive_1 == 0):
                result = True
            else:
                if (process_using_sata_dispositive_1 != process.PID):
                    result = False

        if (process.using_sata_dispositive == 2):
            if (sata_dispositive_2 == 0):
                result = True
            else:
                if (process_using_sata_dispositive_2 != process.PID):
                    result = False
    return result

#libera os dispositivos ques estavam sendo usados por um processo
def free_process_dispositives(process):
    global printer_1,printer_2,scanner,sata_dispositive_1,sata_dispositive_2
    global process_using_sata_dispositive_1,process_using_sata_dispositive_2
    global process_using_printer_1,process_using_printer_2,process_using_scanner
    global process_using_modem,modem
    if(process.using_printer == 1):
        printer_1 = 0
        process_using_printer_1 = -1
    if(process.using_printer == 2):
        printer_2 = 0
        process_using_printer_2 = -1
    if(process.using_scanner == 1):
        scanner = 0
        process_using_scanner = -1
    if(process.using_sata_dispositive == 1):
        sata_dispositive_1 = 0
        process_using_sata_dispositive_1 = -1
    if(process.using_sata_dispositive == 2):
        process_using_sata_dispositive_2 = -1
        sata_dispositive_2 = 0
    if(process.using_modem == 1):
        process_using_modem = -1
        modem = 0

# deixa os dispositivos que um processo ira usar com o estado como ocupado
def process_dispositives_to_busy(process):
    global process_using_sata_dispositive_1, process_using_sata_dispositive_2
    global process_using_printer_1, process_using_printer_2, process_using_scanner
    global printer_1, printer_2, scanner, sata_dispositive_1, sata_dispositive_2
    global modem,process_using_modem
    if (process.using_printer == 1):
        process_using_printer_1 = process.PID
        printer_1 = 1
    if (process.using_printer == 2):
        process_using_printer_2 = process.PID
        printer_2 = 1
    if (process.using_scanner == 1):
        process_using_scanner = process.PID
        scanner = 1
    if (process.using_modem == 1):
        process_using_modem = process.PID
        modem = 1
    if (process.using_sata_dispositive == 1):
        process_using_sata_dispositive_1 = process.PID
        sata_dispositive_1 = 1
    if (process.using_sata_dispositive == 2):
        process_using_sata_dispositive_2 = process.PID
        sata_dispositive_2 = 1





