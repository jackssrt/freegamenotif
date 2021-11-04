from loader import Loader
import time
import os


def main():
    if not os.path.exists("./lastRan.txt"):
        with open("./lastRan.txt", "w") as f:
            f.write("0")
    with open("./lastRan.txt") as f:
        lastRan = float(f.read().strip())
        if time.time() <= lastRan+15:
            print("Already ran within")
            return
    print("""
  __                                                      _   _  __ 
 / _|                                                    | | (_)/ _|
| |_ _ __ ___  ___  __ _  __ _ _ __ ___   ___ _ __   ___ | |_ _| |_ 
|  _| '__/ _ \/ _ \/ _` |/ _` | '_ ` _ \ / _ \ '_ \ / _ \| __| |  _|
| | | | |  __/  __/ (_| | (_| | | | | | |  __/ | | | (_) | |_| | |  
|_| |_|  \___|\___|\__, |\__,_|_| |_| |_|\___|_| |_|\___/ \__|_|_|  
                    __/ |                                           
                   |___/                                            
""")
    s, n = Loader.load()
    print("Running")
    games = s.check()
    n.notify(games)
    with open("./lastRan.txt", "w") as f:
        f.write(str(time.time()))


if __name__ == "__main__":
    Loader.load_env()
    if os.getenv("FGN_WEB", "false") == "true":
        import web
    else:
        main()
