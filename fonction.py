from tkinter import *
import tkinter as tk
from tkinter import scrolledtext





tab = ["https://www.romsgames.net/roms/snk-neo-geo/", "https://www.romsgames.net/roms/atari-2600/", "https://www.romsgames.net/roms/atari-5200-supersystem/",
 "https://www.romsgames.net/roms/atari-7800-prosystem/", "https://www.romsgames.net/roms/atari-jaguar/", "https://www.romsgames.net/roms/atari-lynx/",
  "https://www.romsgames.net/roms/nintendo/", "https://www.romsgames.net/roms/super-nintendo/", "https://www.romsgames.net/roms/gameboy/" ,
   "https://www.romsgames.net/roms/gameboy-color/" , "https://www.romsgames.net/roms/gameboy-advance/","https://www.romsgames.net/roms/sega-genesis/",
   "https://www.romsgames.net/roms/sega-32x/", "https://www.romsgames.net/roms/sega-master-system/","https://www.romsgames.net/roms/game-gear/"]
tab1 = ["neo", "atari2600", "atari5200", "atari7800", "atarijaguar", "atarilynx", "nes", "snes","gameboy","gameboycolor","gba","megadrive","32x","mastersysteme","gamegear"]

def Droms(name,nb):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # https://sites.google.com/chromium.org/driver/
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(name)

    element = driver.find_element(By.TAG_NAME, 'section')
    elements = element.find_elements(By.TAG_NAME, "a")

    stoppp = False
    # Use index to keep track of the current element
    for i in range(37):
        # Re-acquire the element list after navigation
        element = driver.find_element(By.TAG_NAME, 'section')
        elements = element.find_elements(By.TAG_NAME, "a")

        e = elements[i]
        print(e.text)
        # Scroll to the element
        driver.execute_script("arguments[0].scrollIntoView(true);", e)
        time.sleep(1)  # Pause to ensure scrolling is complete
        # Click the element using JavaScript
        driver.execute_script("arguments[0].click();", e)
        print(i)
        if e == 'next':
            print("next")
        else:
            time.sleep(1)  # Pause to allow the page to load after click
            driver.back()
            time.sleep(1)  # Pause to allow the previous page to load

    time.sleep(100)
    driver.quit()
selected_index = None

def spawn_button():
    global selected_index
    
    window = Tk()
    window.title("Heisenberg en personne")
    window.geometry("1920x1080")
    window.minsize(480, 360)
    window.configure(bg='blue')
    window.config(background="#00FFD4")

    def assign_text(nombre):
        return tab1[nombre]

    rows = len(tab1) // 5 + (1 if len(tab1) % 5 != 0 else 0)

    for i in range(rows):
        window.grid_rowconfigure(i, weight=1)
    for j in range(5):
        window.grid_columnconfigure(j, weight=1)

    tab2 = [""] * len(tab1)
    nb = 0

    def on_button_press(index):
        global selected_index
        selected_index = index
        window.destroy()

    for i in range(rows):
        for j in range(5):
            if nb < len(tab1):
                tab2[nb] = Button(window, font=('white', 20), text=tab1[nb], command=lambda index=nb: on_button_press(index))
                tab2[nb].grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                nb += 1

    window.mainloop()
    return selected_index

class TextBoxApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Exemple de Text Box")

        self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.text_box.pack(padx=10, pady=10)

        self.root.bind("<Return>", self.capturer_texte)
        self.texte = None

    def capturer_texte(self, event=None):
        self.texte = self.text_box.get("1.0", tk.END).strip()
        self.root.destroy()

    def run(self):
        self.root.mainloop()
        return self.texte

def texteboxe():
    app = TextBoxApp()
    texte = app.run()
    return texte


def download_Roms():
    nombre = texteboxe()
    print(nombre)
    console = spawn_button()
    print(console)
    Droms(tab[console], nombre)

download_Roms()