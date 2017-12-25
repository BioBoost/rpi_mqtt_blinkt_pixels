import threading
from time import sleep
from lib.color import *
from lib.effects.color_effect import *

class EffectManager(object):

    def __init__(self, pixelStrip):
        self.pixelStrip = pixelStrip
        self.effect = ColorEffect(pixelStrip, Colors.BLACK)
        self.effectLock = threading.Lock()
        self.enable()
        self.__setup_run_deamon()

    def disable(self):
        self.enabled = False
        self.effectLock.acquire()
        self.effect.stop()
        self.effectLock.release()

    def enable(self):
        self.effectLock.acquire()
        self.effect.start()
        self.effectLock.release()
        self.enabled = True

    def is_enabled(self):
        return self.enabled

    def get_current_effect(self):
        return self.effect

    def set_effect(self, effect):
        # Lock to make sure no concurrent access to effect
        self.effectLock.acquire()
        self.effect.stop()
        self.effect = effect
        self.effect.start()
        self.effectLock.release()

    def __setup_run_deamon(self):
        self.runEffectThread = threading.Thread(target=self.__run_effect)
        self.runEffectThread.daemon = True        # Daemon threads are abruptly stopped at shutdown.
        self.runEffectThread.start()

    def __run_effect(self):
        while True:
            if self.enabled:
                self.effectLock.acquire()
                self.effect.run()
                interval = self.effect.updateInterval
                self.effectLock.release()
            else:
                interval = 1.0

            sleep(interval)
