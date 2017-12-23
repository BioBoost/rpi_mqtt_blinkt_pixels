import threading
from time import sleep

class EffectManager(object):

    def __init__(self, pixelStrip):
        self.pixelStrip = pixelStrip
        self.effect = None
        self.effectLock = threading.Lock()
        self.__setup_run_deamon()

    def set_effect(self, effect):
        # Lock to make sure no concurrent access to effect
        self.effectLock.acquire()
        self.__stop_effect()
        self.effect = effect
        self.__start_effect()
        self.effectLock.release()

    def __setup_run_deamon(self):
        self.runEffectThread = threading.Thread(target=self.__run_effect)
        self.runEffectThread.daemon = True        # Daemon threads are abruptly stopped at shutdown.
        self.runEffectThread.start()

    def __stop_effect(self):
        if self.effect != None:
            self.effect.stop()
            self.effect = None

    def __start_effect(self):
        self.effect.start()

    def __run_effect(self):
        while True:
            if self.effect != None:
                self.effectLock.acquire()
                self.effect.run()
                interval = self.effect.updateInterval
                self.effectLock.release()
                sleep(interval)
