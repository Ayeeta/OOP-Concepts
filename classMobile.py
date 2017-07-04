class mobile(object):
 
 """this is the mobile class"""
    def __init__(self, IEMICode, Processor_Type, simcard_size, internalMemory,IssingleSim):
        self.IEMICode = IEMICode
        self.Processor_Type = Processor_Type        
        self.simcard_size = simcard_size
        self.internalMemory = internalMemory
        self.IssingleSim = IssingleSim
     
    def dial():
        return 'Dial a number'
    def receive(self):
        return 'Receive a call'
    def sendMessage(self):
        return 'Message Sent'  
