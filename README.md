# Audio Tools

An internet video downloader using a simple interface and [Youtube-dl](https://github.com/ytdl-org/youtube-dl)

## How to use ?

Simply run the interface.pyw script. Then, you will be provided with a simple interface.

## Current Features :

- Automatic link recognition, wether it's a link or search on youtube

- Select wether to download in a video or audio format

- Whole youtube playlist download (on by default)

- Download in the best quality automaticaly

## Install and Prerequites :

First, you need to have python 3.2+ (latest version is recommanded thought) installed with tkinter integrated with it.

Then, run these commands :

```bash
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade youtube-dl
```

Or, if you are on windows, run this in a cmd shell with administrator rights:

```batch
pip3 install --upgrade pip
pip3 install --upgrade youtube-dl
```

Finally, you can run the `interface.pyw` and it will work fine.

## Bug Report or issues

If you encounter any bug using Audio tools, any issues or simply want to upgrade the code, don't hesitate and go ahead open an issue [here](https://github.com/Colnup/Audio_Tools/issues/new). There is no template whatsoever, but just don't throw a "It doesn't work". You could also please format the title like this : `[proposed Label] actual title` wether the proposed label is a bug report, request or something else.

## About the project

This project is a side project, with only me working on it, and will most likely not be worked on nor updated for long periods of time. If you would like to see a feature added, open an issue and I will try to implement it.

You could also use the `downloader.py` as a library, there are defaults settings that I believe are quiet good. So, feel free to implement this in any of your projects (remember to cite the [GitHub](https://github.com/Colnup/Audio_Tools) webpage in your project).
