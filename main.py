import yt_downloader

def printYTmessage():
    print(" -------------------------------------------")
    print("|        ||      ||     ||||||||||          |")
    print("|          ||  ||           ||              |")
    print("|            ||             ||              |")
    print("|          ||               ||              |")
    print("|         ||                ||              |")
    print(" -------------------------------------------")


def printDOWNLOADmessage():
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("|          ||||||         |||||||       ||            ||     ||      ||     ||             |||||||           ||         ||||||            |")
    print("|          ||    ||     ||       ||      ||    ||    ||      ||||    ||     ||           ||       ||        ||||        ||    ||          |")
    print("|          ||    ||     ||       ||       ||  ||||  ||       ||  ||  ||     ||           ||       ||       ||  ||       ||    ||          |")
    print("|          ||    ||     ||       ||        ||||  ||||        ||    ||||     ||           ||       ||      ||||||||      ||    ||          |")
    print("|          ||||||         |||||||           ||    ||         ||      ||     ||||||||       |||||||       ||      ||     ||||||            |")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")

def printMENUmessage():
    print(" -------------------------------------------")
    print("|        SELECT OPTION BY NUMBER:           |")
    print("|            (1) DOWNLOAD MP4               |")
    print("|            (2) DOWNLOAD MP3               |")
    print(" -------------------------------------------")
def processDecision(decision):
    if(decision == '1'):
        url = input("Afegeix la URL del video que et vols descarregar: ")   
        yt_downloader.descarregar_video(url)
def main():
    printYTmessage()
    printDOWNLOADmessage()
    printMENUmessage()
    decision = input()
    processDecision(decision)

def redirectToMain():      
    if __name__== "__main__":
        main()

redirectToMain()
