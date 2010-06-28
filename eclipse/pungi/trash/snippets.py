"""
class InterruptableThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.sync = threading.Event()

    def run(self):
        logging.debug("Thread %s started" % self.getName())
        while not self.sync.isSet():
            interval = self.runTask()
            if not interval:
                break
            self.sync.wait(interval)
        logging.debug("Thread %s stopped" % self.getName())
    
    def runTask(self):
        return None
    
    def stop(self):
        logging.debug("Thread %s stopping" % self.getName())
        self.sync.set()
        
def exitApplication():
    logging.debug("exitApplication() called")
    sys.exit()
"""

"""
def login():
    appuifw.app.title = u"Pungi - Login"
    while True:
        loginDetails = appuifw.multi_query(u"Username", u"Password")
        if loginDetails: 
            if True:#remoteLogin(loginDetails[0], loginDetails[1]):
                return True
            appuifw.note(u"Username or password incorrect", 'error')
        else:
            logging.debug("User cancelled login request")
            return False
        
class MainScreen(appuifw.Canvas):
    
    def __init__(self):
        appuifw.Canvas.__init__(self, self.redraw)
        #self.redraw()
    
    def redraw(self, coords):
        self.outline = 0xffffff
        self.fill = 0xffff00
        self.rectangle((0, 0, 10, 10))
        
def mainScreen():
    appuifw.app.title = u"Pungi"
    appuifw.app.body = MainScreen()
              
appuifw.app.exit_key_handler = functions.exitApplication
appuifw.app.screen = "normal"
appuifw.app.body = None
"""