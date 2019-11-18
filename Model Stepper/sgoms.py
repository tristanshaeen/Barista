from pynput import keyboard
#######################################

class Sgoms:
    
    def on_release(self,key):
        try:        
            if key.char == 'd':
                return False # Stop listener - or listener.stop??
            if key.char == 'w':
                print(5555555555555555555)
                self.step()
        except AttributeError:
            print('{0} has no function'.format(key))


    def run(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join() # run the listener thread
        print('stopped')


    def _init_(self):
        self.planning_unit=None
        self.unit_task=None
        self.method=None

    def step(self):
        print('step')
