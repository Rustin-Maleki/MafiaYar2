import tkinter as tk
import time
import pyttsx3

def on_button_click():
    window.withdraw()  # پنهان کردن پنجره اصلی
    new_window = tk.Toplevel(window)
    new_window.title("Game Window")
    new_window.geometry("300x200")
    mafia_label = tk.Label(new_window, text="تعداد بازیکنان مافیا:")
    mafia_label.pack(pady=10)
    mafia_entry = tk.Entry(new_window)
    mafia_entry.pack()
    submit_button = tk.Button(new_window, text="Submit", command=lambda: on_submit(mafia_entry, new_window))
    submit_button.pack(pady=10)
    new_window.wait_window()  # منتظر ماندن تا پنجره بسته شود

def on_submit(mafia_entry, new_window):
    mafia_count = int(mafia_entry.get())
    names_label = tk.Label(new_window, text="نام‌های بازیکنان مافیا:")
    names_label.pack(pady=10)
    names_entries = []
    for i in range(mafia_count):
        name_label = tk.Label(new_window, text=f"نام بازیکن مافیا {i+1}:")
        name_label.pack(pady=5)
        name_entry = tk.Entry(new_window)
        name_entry.pack()
        names_entries.append(name_entry)
    submit_button = tk.Button(new_window, text="Submit", command=lambda: on_submit_names(names_entries, new_window))
    submit_button.pack(pady=10)
    new_window.wait_window()  # منتظر ماندن تا پنجره بسته شود

def on_submit_names(names_entries, new_window):
    mafia_names = []
    for entry in names_entries:
        name = entry.get()
        mafia_names.append(name)
        entry.delete(0, tk.END)  
    print("نام‌های بازیکنان مافیا:", mafia_names)
    speak(mafia_names)
    new_window.destroy()  # بستن پنجره جاری

def speak(mafia_names):
    speak_window = tk.Toplevel(window)
    speak_window.title("Speak Window")
    speak_window.geometry("200x200")
    names_label = tk.Label(speak_window, text="نام‌های بازیکنان مافیا:")
    names_label.pack(pady=10)
    for player in mafia_names:
        player_label = tk.Label(speak_window, text=player)
        player_label.pack()
        speak_window.update()
        time.sleep(1)
        
def get_votes(mafia_names, new_window):
    votes_window = tk.Toplevel(window)
    votes_window.title("Votes Window")
    votes_window.geometry("300x200")
    votes_label = tk.Label(votes_window, text="تعداد رای برای هر بازیکن:")
    votes_label.pack(pady=10)
    votes_entries = []
    for player in mafia_names:
        vote_label = tk.Label(votes_window, text=f"تعداد رای برای {player}:")
        vote_label.pack(pady=5)
        vote_entry = tk.Entry(votes_window)
        vote_entry.pack()
        votes_entries.append(vote_entry)
    submit_button = tk.Button(votes_window, text="Submit", command=lambda: on_submit_votes(votes_entries, votes_window))
    submit_button.pack(pady=10)
    votes_window.wait_window()  # منتظر ماندن تا پنجره بسته شود


window = tk.Tk()
window.title("Main Window")
window.geometry("300x200")
button = tk.Button(window, text="Start Game", command=on_button_click)
button.pack(pady=50)
window.mainloop()
