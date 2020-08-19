"""Tkinter Graphical interface for the Audio Tools Project
"""

import sys
from tkinter import *
from tkinter import ttk

from downloader import download


log_file = open("logs.txt", "w")
sys.stdout = log_file
sys.stderr = log_file


class App(Tk):
    """Root windown of the app
    """

    def __init__(self, title="App"):
        """App class init

        Parameters
        ----------
        title : str, optional
            Title of the created window, by default "App"
        """

        Tk.__init__(self)
        self.wm_title(title)


class Window(ttk.Frame):
    """Child of the ttk.Frame class, allowing an easier way to have a global theme for the frames in the app
    """

    def __init__(self, master=None, **kwargs):
        ttk.Frame.__init__(self, master, borderwidth=5,
                           relief="sunken", **kwargs)
        self.master = master
        self.pack()


def proceed(*args):
    # *args is necessary beacuse of the bind to the enter key of the keyboard
    options = {
        "format": formattage.get(),
        "noplaylist": playlist.get(),
    }
    status.set("Status :\nDownloading...")
    status_label.update()
    download(text.get(), **options)
    status.set("Status :\nWaiting for a download...")
    text.set("")


root = App("Audio Tools")
content = Window(root)


text = StringVar()
text_box = ttk.Entry(content, textvariable=text, width=48)
formattage = StringVar()
formattage.set("bestaudio")
audio = ttk.Radiobutton(content, text="Audio",
                        variable=formattage, value="bestaudio")
video = ttk.Radiobutton(content, text="Vidéo",
                        variable=formattage, value="best")
downaload_button = ttk.Button(content, text="Proceed",
                              command=proceed)
playlist = BooleanVar()
playlist.set(False)
playlist_button = ttk.Checkbutton(
    content, text="Download the playlist (if appropriate)", variable=playlist,
    onvalue=False, offvalue=True)
status = StringVar()
status.set("Status :\nWaiting for a download...")
status_label = ttk.Label(content, textvar=status, justify="center")


content.grid(column=0, row=0, sticky=(N, S, E, W))
text_box.grid(column=0, row=0, sticky=(E, W), padx=5, pady=5)
audio.grid(column=0, row=1, sticky=(E, W))
video.grid(column=0, row=2, sticky=(E, W))
playlist_button.grid(column=0, row=3, sticky=(E, W))
downaload_button.grid(column=1, row=3)
status_label.grid(column=1, row=2)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)

text_box.focus()
root.bind("<Return>", proceed)


root.mainloop()
