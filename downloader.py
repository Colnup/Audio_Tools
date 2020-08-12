from youtube_dl import YoutubeDL


# def my_hook(d):
#     if d["status"] == "finished":
#         print("Done downloading, now converting ...")


def download(url, **args):
    # Paramètres par défaut
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "C:/%HOMEPATH%/Desktop/Musique/new/%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "no_warnings": False,
        "simulate": False,
        "nooverwrites": True,
        "writedescription": False,

        # "progress_hooks": [my_hook],
    }

    if type(url) == str:
        url = [url]

    for i in args.items():
        ydl_opts[i[0]] = i[1]

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


if __name__ == "__main__":
    download("https://www.youtube.com/watch?v=PKfxmFU3lWY, bestaudio")
