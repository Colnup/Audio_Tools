# Audio Tools

An internet video downloader using a simple interface and [Youtube-dl](https://github.com/ytdl-org/youtube-dl)

## How to use ?

Simply run the interface.pyw script. Then, you will be provided with a simple interface.

## Current Features :

- Select wether to download in a video or audio format

- Whole youtube playlist download (on by default)

- Download in the best quality automaticaly

## Install and Prerequites :

### Prerequites :

Download and install [Python](https://www.python.org/downloads/) (version 3.10 or higher) and [Git](https://git-scm.com/downloads) (version 2.0 or higher).

### Install :

Download the latest release [here](https://github.com/Colnup/Audio_Tools/releases/latest) and extract it.

Then, open a terminal in the extracted folder and run these commands if you are on linux :

```bash
sudo pip3 install --upgrade pip

sudo pip3 install --upgrade youtube-dl
```
Or, if you are on windows, run this in a cmd shell with administrator rights:

```cmd

py -m pip install --upgrade pip

py -m pip install --upgrade youtube-dl
```



Finally, you can run the `interface.pyw`.

## Bug Report or issues

If you encounter any bug using Audio tools, any issues or simply want to upgrade the code, don't hesitate and go ahead open an issue [here](https://github.com/Colnup/Audio_Tools/issues/new). There is no template whatsoever, but just don't throw a "It doesn't work". Please format the title like this : `[proposed Label] actual title` wether the proposed label is a bug report, request or something else.

## About the project

This project is a side project, with only me working on it, and will most likely not be worked on nor updated for long periods of time. If you would like to see a feature added, open an issue and I will try to implement it.


## What happened to the old version ?

As a developer, I like to keep my code clean and readable. The old version was a mess, and I decided to rewrite it from scratch. The old version is still available [here](https://github.com/Colnup/Audio_Tools/releases/tag/v0.3-alpha) if you want to check it out, but it is not maintained anymore.

The new version brings more stability, a better interface and a better code overall.

Still, there are missing features from the old version, namely:

- The `downloader.py` library. This library was a front-end for youtube-dl, and since we switched to yt-dlp, it is not compatible anymore. This library won't be re-implemented, but you can check the new `downloader.py` which contains some similar code that you can use.
- The automatic installer. This feature was an experiment for me, and it was buggy and not working properly. It won't be re-implemented for now, but with enough requests, I might do it.
- The log file. This feature was not really useful, as you can just check the console for the logs. It won't be re-implemented for now, but with enough requests, I might do it.
- Automatic youtube search from the url bar. This will be re-implemented in the future, but it is not a priority for now.


## License

This project is licensed under the Creative Commons CC-BY 4.0 License.

This means that you can use, modify and redistribute this project, as long as you credit me. Feel free to use this project for any purpose, commercial or not.