import tkinter as tk
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime

MASTER = "Farrel"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Pemanggilan fungsi speak pada awal program
speak("Hello, my name is Arel. I can help you")

def whisMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Selamat Pagi " + MASTER
        message = "Apa yang bisa saya bantu untuk Anda hari ini?"
    elif 12 <= hour < 18:
        greeting = "Selamat Siang " + MASTER
        message = "Ada yang dapat saya bantu di tengah hari ini?"
    else:
        greeting = "Selamat Sore " + MASTER
        message = "Ada yang dapat saya bantu menjelang malam?"
    
    speak(greeting)
    return greeting, message

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        result_text.set("Saya akan mendengarkan Anda...")
        root.update_idletasks()  # Memperbarui jendela agar tampilan segera diperbarui
        print("Mendengarkan....")
        audio = r.listen(source)

    try:
        print("Mengenali...")
        query = r.recognize_google(audio, language="id-id")
        print(f"Pengguna mengatakan: {query}\n")
        result_text.set("Perintah akan saya lakukan.")
        root.update_idletasks()  # Memperbarui jendela agar tampilan segera diperbarui
        return query
    except Exception as e:
        print("Ulangi Lagi Tolong")
        result_text.set("Maaf, saya tidak dapat mengenali perintah.")
        root.update_idletasks()  # Memperbarui jendela agar tampilan segera diperbarui
        return None

def on_button_click():
    query = takeCommand()

    if query:
        if "buka pekerjaan saya" in query.lower():
            urls = [
                "https://youtube.com",
                "https://web.telegram.org",
                "https://trello.com/b/Mi12vqeN/progress-konten",
                "https://docs.google.com/spreadsheets/d/1uP9GlUH1Yb8VoMTdta6ho6tNfqsugb0-HOghlgNIxwY/edit#gid=1465611317"
            ]
            for url in urls:
                webbrowser.open(url)
            speak("Membuka link-link pekerjaan Anda.")
        elif "wikipedia" in query.lower():
            speak("Mencari di Wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            result_text.set(result)
        elif "buka youtube"in query.lower():
            url = "youtube.com"
            chrome_path = "C:/Program Files (x64)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.open(url)
        elif "buka telegram"in query.lower():
            url = "https://web.telegram.org"
            chrome_path = "C:/Program Files (x64)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.open(url)
        elif "buka daftar tugas" in query.lower():
            url = "https://keep.google.com/"
            chrome_path = "C:/Program Files (x64)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.open(url)
        elif "buka canva PREMIUM" in query.lower():
            url = "https://www.canva.com/"
            chrome_path = "C:/Program Files (x64)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.open(url)
        else:
            result_text.set("Perintah tidak dikenali.")

# Membuat jendela tkinter
root = tk.Tk()
root.title("Asisten Suara Arel")

# Mendapatkan dimensi layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Mendefinisikan lebar dan tinggi minimum untuk jendela
min_width = 400
min_height = 300

# Menghitung posisi untuk menempatkan jendela di tengah layar
x_position = (screen_width - min_width) // 2
y_position = (screen_height - min_height) // 2

# Menempatkan jendela di tengah layar dengan lebar dan tinggi minimum
root.geometry(f"{min_width}x{min_height}+{x_position}+{y_position}")

# Membuat dan mengonfigurasi elemen GUI
greeting_label = tk.Label(root, text=whisMe()[0], font=("Helvetica", 14))
greeting_label.grid(row=0, column=0, pady=4, columnspan=2, sticky="nsew")

message_label = tk.Label(root, text=whisMe()[1], font=("Helvetica", 12))
message_label.grid(row=1, column=0, pady=4, columnspan=2, sticky="nsew")

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12))
result_label.grid(row=2, column=0, pady=4, columnspan=2, sticky="nsew")

button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, pady=4, columnspan=2, sticky="nsew")

listen_button = tk.Button(button_frame, text="Dengar", command=on_button_click, width=10)
listen_button.grid(row=0, column=0, pady=7)

exit_button = tk.Button(button_frame, text="Keluar", command=root.destroy, width=10)
exit_button.grid(row=0, column=1, pady=7)

# Mengatur elemen GUI di tengah jendela secara dinamis
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.update_idletasks()  # Memperbarui jendela agar tampilan segera diperbarui

# Mendapatkan dimensi jendela setelah diperbarui
window_width = root.winfo_width()

# Menghitung posisi untuk menempatkan teks "SELAMAT SIANG FARREL" di tengah jendela
x_text_position = (window_width - greeting_label.winfo_reqwidth()) // 2

# Menempatkan teks "SELAMAT SIANG FARREL" di tengah jendela
greeting_label.grid_configure(padx=x_text_position)

root.mainloop()
