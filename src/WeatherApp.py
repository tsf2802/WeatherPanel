
import tkinter as tk
from tkinter import font

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # Setting up fonts
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        condition_font = font.Font(family="Helvetica", size=12)
        main_temp_font = font.Font(family="Helvetica", size=20)
        small_font = font.Font(family="Helvetica", size=10)
        
        # Title
        title_label = tk.Label(self, text="Rochester, NY :", font=title_font, bg="#B0C4DE")
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Weather Icon
        weather_icon = tk.Label(self, text="🌧", font=main_temp_font, bg="#B0C4DE")
        weather_icon.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        # Temperature
        temp_label = tk.Label(self, text="70°F / 23°C", font=main_temp_font, bg="#B0C4DE")
        temp_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Condition
        condition_label = tk.Label(self, text="Condition", font=condition_font, bg="#B0C4DE")
        condition_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        # High/Low
        high_low_label = tk.Label(self, text="H: 77 L: 65", font=small_font, bg="#B0C4DE")
        high_low_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Next 6 hours
        next6_frame = tk.Frame(self, bg="#D3D3D3", height=50, width=200)
        next6_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        next6_label = tk.Label(next6_frame, text="Grind layout of next 6 hours", bg="#D3D3D3")
        next6_label.pack(expand=True, fill="both")
        
        # Additional info frame
        info_frame = tk.Frame(self, bg="#AFEEEE", height=50, width=400)
        info_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        info_label = tk.Label(info_frame, text="Feels Like:    Humidity:    Wind:    Pressure:    AQI:    Cloud Cover:", bg="#AFEEEE")
        info_label.pack(expand=True, fill="both")
        
        # Daily forecast frame
        daily_forecast_frame = tk.Frame(self, bg="#AFEEEE", height=100, width=200)
        daily_forecast_frame.grid(row=5, column=0, padx=10, pady=10, sticky="we")
        daily_forecast_label = tk.Label(daily_forecast_frame, text="Date+Monday icon, high temp- avgtemp- lowtemp", bg="#AFEEEE")
        daily_forecast_label.pack(expand=True, fill="both")
        
        # Quote frame
        quote_frame = tk.Frame(self, bg="#AFEEEE", height=100, width=200)
        quote_frame.grid(row=5, column=1, padx=10, pady=10, sticky="we")
        quote_label = tk.Label(quote_frame, text="zenquotes io:", bg="#AFEEEE")
        quote_label.pack(expand=True, fill="both")
        
        # Footer
        footer_label = tk.Label(self, text="[7/4/24, 21:20]: Heavy Rain in the Rochester Area...", font=small_font, bg="#AFEEEE")
        footer_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Configure grid
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    root.configure(bg="#B0C4DE")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
