from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from video_info import VideoInfo


class VideoView(QWidget):
    """Video view widget.
    Contains the video thumbnail, title, author, and duration.
    """

    def __init__(self, video: VideoInfo = None):

        super().__init__()

        self._video_info = video if video else VideoInfo()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.thumbnail = QLabel()
        self.thumbnail.setFixedSize(160, 90)
        self.layout.addWidget(self.thumbnail)

        self.title = QLabel()
        self.layout.addWidget(self.title)

        self.author = QLabel()
        self.layout.addWidget(self.author)

        self.duration = QLabel()
        self.layout.addWidget(self.duration)

    @property
    def video_info(self):
        return self._video_info

    @video_info.setter
    def video_info(self, video: VideoInfo):
        if not isinstance(video, VideoInfo):
            raise TypeError(
                f'video must be of type VideoInfo, got {type(video)}')
        self._video_info = video
        self.update()

    def set_video_info(self, video: VideoInfo):
        self.video_info = video

    def update(self):
        """Load video info from a VideoInfo object."""
        self.title.setText(self.video_info.title)
        self.author.setText(self.video_info.author)
        self.duration.setText(self.video_info.duration)

        # Resize thumbnail
        self.thumbnail.setPixmap(self.video_info.thumbnail.scaled(
            self.thumbnail.width(),
            self.thumbnail.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))
