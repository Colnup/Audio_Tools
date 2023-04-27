import sys
from time import sleep
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


from controls import Controls
from video_view import VideoView
from downloader import Downloader


class Main(QWidget):

    def __init__(self):

        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.inside_layout = QHBoxLayout()
        self.layout.addLayout(self.inside_layout)

        self.video_view = VideoView()
        self.inside_layout.addWidget(self.video_view)

        self.controls = Controls()
        self.inside_layout.addWidget(self.controls)

        self.controls.downloadClicked.connect(self.download)

        self.progress_bars = QVBoxLayout()
        self.layout.addLayout(self.progress_bars)

        # Logic
        self.current_url = None
        self.controls.urlUpdated.connect(self.update_video_info)

        # Prevent QThreads from being killed early
        self.workers = []

    def update_video_info(self, url: str):
        """Update video info from url."""
        if url == self.current_url:
            self.download()
            return

        self.current_url = url

        d = Downloader("get_video_info", url)
        self.workers.append(d)

        def handle_video_info(video):
            self.video_view.video_info = video
            self.workers.remove(d)

        d.finished.connect(handle_video_info)
        d.start()

    def download(self):
        """Download video."""

        # Generate progress bar
        p = QProgressBar()
        p.setMinimum(0)
        p.setMaximum(100)
        p.setValue(0)
        p.setFormat("Downloading...")
        p.setTextVisible(True)
        self.progress_bars.addWidget(p)

        d = Downloader("download", self.controls.url_input.text())
        self.workers.append(d)

        def handle_download(res):
            self.workers.remove(d)
            # self.progress_bars.removeWidget(p)
            p.deleteLater()

        d.bar = p
        d.options = self.controls.get_options()

        d.progressUpdated.connect(p.setValue)
        d.progressTextUpdated.connect(lambda t: p.setFormat(t))
        d.finished.connect(handle_download)

        d.start()


if __name__ == '__main__':
    print(f'main')
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec())
