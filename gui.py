import tkinter as tk
from tkinter import ttk
import pywifi
import time

class WifiScanner:
    def __init__(self, window):
        self.window = window
        self.window.title("WifiScanner")

        self.tree = ttk.Treeview(self.window)
        self.tree["columns"] = ("SSID", "RSSI", "Frequency", "BSSID")

        self.tree.heading("#0", text="ID")
        self.tree.heading("SSID", text="SSID")
        self.tree.heading("RSSI", text="RSSI (dbm)")
        self.tree.heading("Frequency", text="Frequency")
        self.tree.heading("BSSID", text="BSSID")

        self.tree.grid(row=0, column=0, columnspan=2)

        self.start_button = tk.Button(self.window, 
                                      text="Start", 
                                      command=self.start_scanning, 
                                      width=10, height=2)
        self.start_button.grid(row=1, 
                               column=0, 
                               padx=5, pady=5)

        self.stop_button = tk.Button(self.window, 
                                     text="Stop", 
                                     command=self.stop_scanning, 
                                     width=10, height=2)
        self.stop_button.grid(row=1, 
                              column=1, 
                              padx=5, pady=5)

        self.is_scanning = False

    def add_row(self, 
                row_id, 
                name_network, 
                rssi, 
                freq, 
                bssid):
        # row_id = self.tree.get_children()
        self.tree.insert("", "end", 
                         text=row_id, 
                         values=(name_network, 
                                 rssi, 
                                 freq, 
                                 bssid))

    def start_scanning(self):
        if not self.is_scanning:
            self.is_scanning = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.clear_table()
            self.scanning()

    def stop_scanning(self):
        self.is_scanning = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def scanning(self):
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]

        while self.is_scanning:
            iface.scan()
            time.sleep(0.5)
            results = iface.scan_results()

            row_id = 1
            
            self.clear_table()
    
            for data in results:
                if data.ssid == "":
                    continue
                self.add_row(row_id, 
                             data.ssid, 
                             data.signal, 
                             data.freq, 
                             data.bssid)
                row_id += 1
                
            self.window.update()

    def clear_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)