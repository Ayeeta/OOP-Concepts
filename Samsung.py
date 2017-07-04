from classMobile import mobile

class Samsung(classMobile):
    
    def __init__(self):
        self.phone_Name = 'Samsung'
    
    def GetWifiConnection(self):
        return 'wifi connected'  

    #implementing method overloading 
    def cameraClick(self, cameraMode):
        if cameraMode is None:
            return 'camera clicked'
        else:
            return 'Camera clicked in '+cameraMode+'mode'
