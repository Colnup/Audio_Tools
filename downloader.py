from yt_dlp import YoutubeDL
from video_info import VideoInfo
import datetime
from functools import cache, partial
from PyQt6.QtWidgets import QProgressBar


from constants import DEFAULT_OPTIONS


from PyQt6.QtCore import *


class Downloader(QThread):

    progressUpdated = pyqtSignal(int)
    progressTextUpdated = pyqtSignal(str)
    finished = pyqtSignal(object)

    def __init__(self, state, url):

        super().__init__()
        self.state = state  # "get_video_info" or "download"
        self.url = url
        self.options: dict = None
        self.bar = None

    def run(self):
        match self.state:
            case "get_video_info":
                res = self.get_video_info()
            case "download":
                res = self.download()

        self.finished.emit(res)

    def get_downloader(self, options) -> YoutubeDL:
        """Returns the downloader object."""
        downloader = YoutubeDL({**DEFAULT_OPTIONS, **options})
        return downloader

    def download(self) -> None:
        """Download video from url"""

        if self.options:
            options = self.options.copy()
        else:
            options = {}

        if self.bar:
            options = {**options,
                       "progress_hooks": [
                           lambda d: self.progressUpdated.emit(
                               int(float(d["_percent_str"].replace(
                                   "%", "").strip()))
                           ),
                           lambda d: self.progressTextUpdated.emit(
                               f"{d['info_dict'].get('title', 'Unknown title') if len(d['info_dict'].get('title', 'Unknown title'))<17 else d['info_dict'].get('title', 'Unknown title')[:15]+'...'} | {d.get('_speed_str', '')} | {d.get('_eta_str', '00:00')}"
                           ),
                       ]}

        with self.get_downloader(options) as downloader:
            downloader.download([self.url])

        return None

    def get_video_info(self) -> VideoInfo:
        """Returns a VideoInfo object from a video url."""

        with self.get_downloader({'skip_download': True, 'noplaylist': True, }) as downloader:
            info = downloader.extract_info(self.url)
        video_info = VideoInfo()
        video_info.title = info['title']
        video_info.author = info['uploader']
        video_info.duration = str(datetime.timedelta(seconds=info['duration']))
        video_info.load_img_url(info['thumbnail'])
        return video_info
