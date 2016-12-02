import time
import threading
process_module_string = "process_module => "


class Process(threading.Thread):
    PID = 0
    priority = 0
    offset = 0
    allocated_blocks = 0
    initialization_time = 0
    processing_time = 0
    using_printer = 0
    using_scanner = 0
    using_modem = 0
    using_sata_dispositive = 0
    running = False
    times_using_cpu = 0
    time_already_executed = 0

    def __init__(self, PID, priority,offset,allocated_blocks,initialization_time,processing_time,
                 using_printer,using_scanner,using_modem,using_sata_dispositive):
        threading.Thread.__init__(self)
        self.PID = int(PID)
        self.priority = int(priority)
        self.offset = int(offset)
        self.allocated_blocks = int(allocated_blocks)
        self.initialization_time = int(initialization_time)
        self.processing_time = int(processing_time)
        self.using_printer = int(using_printer)
        self.using_scanner = int(using_scanner)
        self.using_modem = int(using_modem)
        self.using_sata_dispositive = int(using_sata_dispositive)

    # codigo executado quando processo eh iniciado
    def run(self):
        self.despachante()
        self.process_execution()

    # despachante printa as informacoes do processo
    def despachante(self):
        print "dispatcher =>"
        print "    PID: " + str(self.PID)
        print "    offset: " + str(self.offset)
        print "    blocks: " + str(self.allocated_blocks)
        print "    priority: " + str(self.priority)
        print "    time: " + str(self.processing_time)
        print "    printers: " + str(self.using_printer)
        print "    scanners: " + str(self.using_scanner)
        print "    modems: " + str(self.using_modem)
        print "    drives: " + str(self.using_sata_dispositive)

    # simula execucao do processo
    def process_execution(self):
        instruction_counter = 0
        while instruction_counter < 8:
            if (self.running):
                print process_module_string + "PID " + str(self.PID) + " processing instruction " + str(instruction_counter+1)
                instruction_counter += 1
                self.time_already_executed += 1
                time.sleep(1)

    # instancia process(thread)
    def start_thread(self):
        self.start()

    # pausa execucao da thread
    def pause_thread(self):
        self.running = False

    # continua ou inicia execucao da thread
    def resume_thread(self):
        self.running = True
