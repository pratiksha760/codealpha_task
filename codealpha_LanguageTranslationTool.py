
import tkinter as tk
from tkinter import ttk, messagebox
import urllib.request
import urllib.parse
import json

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Dutch": "nl",
    "Tamil": "ta",
    "Telugu": "te"
}

def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    source = source_lang.get()
    target = target_lang.get()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    if source == target:
        messagebox.showwarning("Warning", "Please select different languages.")
        return

    try:
        lang_pair = languages[source] + "|" + languages[target]

        params = urllib.parse.urlencode({
            "q": text,
            "langpair": lang_pair
        })

        url = "https://api.mymemory.translated.net/get?" + params

        request = urllib.request.Request(
            url,
            headers={"User-Agent": "PythonTranslationTool/1.0"}
        )

        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))

        translated = data["responseData"]["translatedText"]

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", "Translation failed. Please check your internet connection and try again.")

def copy_text():
    translated = output_text.get("1.0", tk.END).strip()

    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Copied", "Translation copied successfully!")

def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x650")
root.config(bg="#eaf2f8")

title = tk.Label(
    root,
    text="LANGUAGE TRANSLATION TOOL",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
title.pack(pady=20)

source_frame = tk.Frame(root, bg="#eaf2f8")
source_frame.pack(pady=10)

tk.Label(
    source_frame,
    text="Source Language:",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8"
).grid(row=0, column=0, padx=10)

source_lang = ttk.Combobox(
    source_frame,
    values=list(languages.keys()),
    state="readonly",
    width=15
)
source_lang.set("English")
source_lang.grid(row=0, column=1, padx=10)

tk.Label(
    source_frame,
    text="Target Language:",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8"
).grid(row=1, column=0, padx=10, pady=15)

target_lang = ttk.Combobox(
    source_frame,
    values=list(languages.keys()),
    state="readonly",
    width=15
)
target_lang.set("Hindi")
target_lang.grid(row=1, column=1, padx=10)

tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 13, "bold"),
    bg="#eaf2f8"
).pack(anchor="w", padx=40, pady=5)

input_text = tk.Text(
    root,
    height=7,
    width=60,
    font=("Arial", 11),
    wrap="word"
)
input_text.pack(padx=30, pady=5)

translate_button = tk.Button(
    root,
    text="TRANSLATE",
    font=("Arial", 12, "bold"),
    bg="#2874a6",
    fg="white",
    width=20,
    command=translate_text
)
translate_button.pack(pady=15)

tk.Label(
    root,
    text="Translated Text:",
    font=("Arial", 13, "bold"),
    bg="#eaf2f8"
).pack(anchor="w", padx=40, pady=5)

output_text = tk.Text(
    root,
    height=7,
    width=60,
    font=("Arial", 11),
    wrap="word"
)
output_text.pack(padx=30, pady=5)

button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="COPY",
    font=("Arial", 11, "bold"),
    bg="#239b56",
    fg="white",
    width=12,
    command=copy_text
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 11, "bold"),
    bg="#c0392b",
    fg="white",
    width=12,
    command=clear_text
).grid(row=0, column=1, padx=10)

root.mainloop()
