
OUTPUT_DIR = "%USERPROFILE%/Music/Audio_Tools/"

DEFAULT_OPTIONS = {
    'outtmpl': OUTPUT_DIR + '%(title)s.%(ext)s',
    "no_color": True,
    "quiet": True,
}

FORMATS_OPTIONS = {

    "mp3": {"format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }]},


    "wav": {"format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "0",
            }]},

    "mp4": {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "postprocessors": [{
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4"
        }]
    },
}
