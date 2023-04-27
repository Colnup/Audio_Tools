import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from constants import FORMATS_OPTIONS


class CheckBox(QWidget):
    """Helper class with a checkbox and a label."""

    Checked = pyqtSignal(bool)

    def __init__(self, text: str):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.checkbox = QCheckBox()
        self.layout.addWidget(self.checkbox)

        self.label = QLabel(text)
        self.layout.addWidget(self.label)

        self.checkbox.stateChanged.connect(self.Checked.emit)


class Formats(QComboBox):
    """Formats combobox."""

    activatedText = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        for format in FORMATS_OPTIONS.keys():
            self.addItem(format)

        self.activated.connect(
            lambda index: self.activatedText.emit(self.itemText(index)))


class Controls(QWidget):
    """Controls widget.

    Contains the url input, 3 Chechboxes for options, a combobox for the format, and a download button.
    """

    downloadClicked = pyqtSignal()
    urlUpdated = pyqtSignal(str)

    def __init__(self):

        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.url_input = QLineEdit()
        self.layout.addWidget(self.url_input)

        self.options = QWidget()
        self.options.layout = QVBoxLayout()
        self.options.setLayout(self.options.layout)
        self.options.download_playlist = CheckBox("Download playlist")
        self.options.dowload_thumbnail = CheckBox(
            "Download thumbnail [EXPERIMENTAL]")
        # self.options.skip_non_music = CheckBox("Skip non music")
        self.options.layout.addWidget(self.options.download_playlist)
        self.options.layout.addWidget(self.options.dowload_thumbnail)
        # self.options.layout.addWidget(self.options.skip_non_music)
        self.layout.addWidget(self.options)

        self.format = Formats()
        self.layout.addWidget(self.format)

        # self.download = QPushButton("Download")
        # self.layout.addWidget(self.download)

        self.url_input.returnPressed.connect(
            lambda: self.urlUpdated.emit(self.url_input.text()))

        # self.download.clicked.connect(self.downloadClicked.emit)

        # So that the video info is updated before downloading

        self.show()

    def get_options(self) -> dict:
        """Returns the options from the checkboxes and the format combobox."""
        options = FORMATS_OPTIONS[self.format.currentText()].copy()
        options['noplaylist'] = not self.options.download_playlist.checkbox.isChecked()
        options['writethumbnail'] = self.options.dowload_thumbnail.checkbox.isChecked()
        return options


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controls = Controls()
    controls.show()
    sys.exit(app.exec())
