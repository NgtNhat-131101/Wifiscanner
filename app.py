from gui import WifiScanner
import tkinter as tk
import time, pywifi
    
if __name__ == "__main__":
    
    window = tk.Tk()

    wifi_scanner = WifiScanner(window)

    window.mainloop()