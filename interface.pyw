"""Interface grapgique Tktiner pour le projet audio_tools
"""

# Test de modif du repo

from tkinter import *
from tkinter import ttk
import time
from downloader import download


class App(Tk):
    """Fenêtre mère de l'application
    """

    def __init__(self, title="App"):
        """Constructeur de la classe App

        Parameters
        ----------
        title : str, optional
            Titre de la fenêtre que l'on crée, by default "App"
        """
        Tk.__init__(self)
        self.wm_title(title)


class Window(ttk.Frame):
    """Classe héritant de frame permettant un thème graphique global
    """

    def __init__(self, master=None, **kwargs):
        """Constructeur de la calsse Window
        """
        ttk.Frame.__init__(self, master, borderwidth=5,
                           relief="sunken", **kwargs)
        self.master = master
        self.pack()


def proceed(*args):
    # Le *args c'est juste pour que ça plante pas à cause du bind avec la touche entrée
    options = {
        "format": formattage.get(),
        "noplaylist": playlist.get(),
    }
    status.set("Status :\nTéléchargement en cours")
    status_label.update()
    download(text.get(), **options)
    status.set("Status :\nEn attente d'un téléchargement")
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
downaload_button = ttk.Button(content, text="SHNELL",
                              command=proceed)
playlist = BooleanVar()
playlist.set(False)
playlist_button = ttk.Checkbutton(
    content, text="Télécharger la playlist (le cas échéant)", variable=playlist,
    onvalue=False, offvalue=True)
status = StringVar()
status.set("Status :\nEn attente d'un téléchargement")
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
