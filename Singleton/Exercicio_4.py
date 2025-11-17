import threading
import time

album = {"Love Story": 10, "Angels": 12, "Elle": 18}

class MusicPlayer():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__currentItem = ""
            cls._instance.__musicLength = 0
            cls._instance.__timer = 0
            cls._instance.__thread = threading.Thread(target=cls._instance.playsound)
        return cls._instance

    def __init__(self):
        pass

    def play(self):
        if self.__thread.is_alive():
            pass
        else:
            self.__thread.start()

    def updateItem(self, musicfile, length):
        self.__currentItem = musicfile
        self.__musicLength = length
        self.__timer = 0

    def playsound(self):
        while self.__timer <= self.__musicLength:
            print("-- playing {} | {}.00/{}.00".format(self.__currentItem, self.__timer, self.__musicLength))
            time.sleep(1)
            self.__timer += 1
        print("{} playing thread has ended".format(self.__currentItem))

class Siri():
    def __init__(self):
        self.player = MusicPlayer()

    def runCMD(self, cmd):
        if cmd.startswith("play music"):
            music = cmd.replace("play music", "").strip()
            self.player.updateItem(music, album[music])
            self.player.play()

if __name__ == "__main__":
    musicList = list(album.keys())
    
    siri = Siri()
    siri.runCMD("play music {}".format(musicList[0]))
    
    time.sleep(4)
    
    siri.runCMD("play music {}".format(musicList[1]))
    
    mainTime = 0
    while mainTime < 20:
        mainTime += 1
        time.sleep(1)
        
    print("End of simulation")