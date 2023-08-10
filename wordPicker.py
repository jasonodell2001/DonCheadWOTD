# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import shutil
from io import BytesIO
import os
import random
import win32clipboard
def moveFile(name):
    src = "Unused/"
    new = "Used/"
    shutil.move(src + name, new + name)

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list = os.listdir("Unused")
    if(len(list) > 0):
        rand = random.randint(0, len(list)-1)
        filePath = list[rand]
        from PIL import Image
        image = Image.open("Unused/" + filePath)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        moveFile(filePath)
    else:
        print("ERROR: NO MORE IMAGES, PLEASE GENERATE MORE")
