from PyQt5.Qt import *
from PyQt5.QtCore import Qt
from tools import button_function


class FinishSurface():

    def __init__(self, app, main_window, main_frame):
        self.app = app
        self.main_window = main_window
        self.main_frame = main_frame
        self._setup_main_frame()
        self._setup_frames()
        self._setup_title_frame_widgets()
        self._setup_work_frame_widgets()
        self.finish_main_frame.show()

    def _setup_main_frame(self):
        self.finish_main_frame = QFrame(self.main_window)
        self.finish_main_frame.setGeometry(0, 0, 800, 640)
        self.finish_main_frame.raise_()

    def _setup_frames(self):
        # frames
        self.title_frame = QFrame(self.finish_main_frame)
        self.title_frame.setStyleSheet("background-color: white;")
        self.work_frame = QFrame(self.finish_main_frame)
        self.work_frame.setStyleSheet("background-color: white;")
        # layout
        self.tol_vertical_layout = QVBoxLayout(self.finish_main_frame)
        self.tol_vertical_layout.setSpacing(0)
        self.tol_vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.tol_vertical_layout.addWidget(self.title_frame)
        self.tol_vertical_layout.addWidget(self.work_frame)
        self.tol_vertical_layout.setStretch(0, 1)
        self.tol_vertical_layout.setStretch(1, 10)

    def _setup_title_frame_widgets(self):
        """init title frame widgets"""
        # title_task_text
        self.title_task_text = QLabel(self.title_frame)
        self.title_task_text.setText("您已完成今日全部任务......")
        self.title_task_text.setAlignment(Qt.AlignCenter)
        self.title_task_text.setStyleSheet("""
                                            QLabel{
                                            font-family: "微软雅黑";
                                            font-size: 30px;
                                            color: black;}

                                            QLabel::hover{
                                            color: white;}
                                            """)
        # layout
        self.title_horizontal_layout = QHBoxLayout(self.title_frame)
        self.title_horizontal_layout.addWidget(self.title_task_text)
        self.title_horizontal_layout.setSpacing(0)
        self.title_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def _setup_work_frame_widgets(self):
        """init work frame widgets"""
        # work_start_button
        self.work_start_button = QPushButton(self.work_frame)
        self.work_start_button.setGeometry(340, 260, 120, 60)
        self.work_start_button.setFocusPolicy(Qt.NoFocus)
        self.work_start_button.setFlat(True)
        self.work_start_button.setText("close")
        self.work_start_button.setStyleSheet("""
                                            QPushButton{
                                            color: black;
                                            font-family: "微软雅黑";
                                            font-size: 45px;
                                            background-color: #f6f6f6;}

                                            QPushButton::hover{
                                            color: white;
                                            font-size: 50px;}

                                            QPushButton::pressed{
                                            border: 0px solid white;}
                                            """)
        self.work_start_button.clicked.connect(self.title_exit_button_function)
        # work_background_label
        self.work_background_img = QLabel(self.work_frame)
        self.work_background_img.lower()
        self.work_background_img.setMargin(0)
        self.work_background_img.setStyleSheet("""
                                                background-color: #f6f6f6;
                                                """)
        self.work_background_img.setFixedWidth(120)
        # layout
        self.work_horizontal_layout = QVBoxLayout(self.work_frame)
        self.work_horizontal_layout.addWidget(self.work_background_img)
        self.work_horizontal_layout.setAlignment(Qt.AlignLeft)
        self.work_horizontal_layout.setSpacing(0)
        self.work_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def title_exit_button_function(self):
        button_function.exit_button(self.app)