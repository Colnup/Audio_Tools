
from PyQt6.QtGui import QPixmap
import requests


class VideoInfo():

    def __init__(self):

        self.title = None
        self.author = None
        self.duration = None

        self._thumbnail = None

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str | QPixmap):

        if isinstance(value, str):
            self._thumbnail = QPixmap(value)
        elif isinstance(value, QPixmap):
            self._thumbnail = value
        else:
            raise TypeError(f'Expected str or QPixmap, got {type(value)}')

    def load_img_url(self, url: str) -> None:
        """Load thumbnail from url."""
        response = requests.get(url)
        self.thumbnail = QPixmap()
        self.thumbnail.loadFromData(response.content)
