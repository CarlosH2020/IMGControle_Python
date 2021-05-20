"""
Controle de Img usando Python

By Carlos Henrique Barros Silva Campos
"""
import os
import glob
import shutil
import time
from pathlib import Path
import pyautogui as py

# usando lista de extensões
arq_img = ["*.png", "*.jpg", "*.gif"]

py.alert(text='Pronto para começar?', title='Alerta: Controle de IMG ', button='OK')

try:
    desktop = Path.home() / "Desktop"
    os.mkdir(f'{desktop}\\IMGControle')
    os.mkdir(f'{desktop}\\IMGControle\\JPG')
    os.mkdir(f'{desktop}\\IMGControle\\PNG')
    os.mkdir(f'{desktop}\\IMGControle\\GIF')
except:
    pass


def ControleImg():
    os.chdir(desktop)
    for img in arq_img:
        for formataIMG in glob.glob(img):
            time.sleep(1)
            print(formataIMG)
            if img == arq_img[0]:
                shutil.move(formataIMG, f'{desktop}\\IMGControle\\PNG')

            elif img == arq_img[1]:
                shutil.move(formataIMG, f'{desktop}\\IMGControle\\JPG')

            elif img == arq_img[2]:
                shutil.move(formataIMG, f'{desktop}\\IMGControle\\GIF')


if __name__ == '__main__':
    ControleImg()