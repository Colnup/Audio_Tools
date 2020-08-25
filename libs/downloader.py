from youtube_dl import YoutubeDL


# def my_hook(d):
#     print(d)


def download(url, **opts):

    # Default parameters
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "C:/%HOMEPATH%/Desktop/Music/new/%(title)s.%(ext)s",
        "noplaylist": False,
        "quiet": False,
        "no_warnings": False,
        "simulate": False,
        "nooverwrites": True,
        "writedescription": False,
        "default_search": "auto",
        "ignoreerrors": True,

        # "progress_hooks": [my_hook],

    }

    # Since you can download multiple URLs, you need a list. If there is only one str, we put it in a list
    if type(url) == str:
        url = [url]

    # Replace any default option with the one we give inside the opts dictionnary
    for i in opts.items():
        ydl_opts[i[0]] = i[1]

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
