from PyQt5.Qt import *
from PyQt5.QtCore import Qt
from tools import button_function
from tools.database_function import databaseFunction


class MainSurface:
    def __init__(self, app, main_window):
        # init params
        self.app = app
        self.main_window = main_window
        # init widgets
        self._setup_main_frame()
        self._setup_frames()
        self._setup_title_frame_widgets()
        self._setup_work_frame_widgets()
        # init function tools
        self.databasefunction = databaseFunction()

    def _setup_main_frame(self):
        self.main_frame = QFrame(self.main_window)
        self.tol_layout = QVBoxLayout(self.main_window)
        self.tol_layout.setContentsMargins(0, 0, 0, 0)
        self.tol_layout.addWidget(self.main_frame)

    def _setup_frames(self):
        # frames
        self.title_frame = QFrame(self.main_frame)
        self.work_frame = QFrame(self.main_frame)
        # layout
        self.tol_vertical_layout = QVBoxLayout(self.main_frame)
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
        self.title_task_text.setText("请开始你的创作......")
        self.title_task_text.setAlignment(Qt.AlignCenter)
        self.title_task_text.setStyleSheet("""
                                            QLabel{
                                            font-family: "微软雅黑";
                                            font-size: 30px;
                                            background-color: #00b66d;
                                            color: white;}
                                            
                                            QLabel::hover{
                                            color: black;}
                                            """)
        # title_exit_button
        self.title_exit_button = QPushButton(self.title_frame)
        self.title_exit_button.setFocusPolicy(Qt.NoFocus)
        self.title_exit_button.setFlat(True)
        self.title_exit_button.setFixedHeight(40)
        self.title_exit_button.setStyleSheet("""
                                            QWidget{
                                            background-color: #00b66d;
                                            image:url(./resources/title_frame_imgs/exit.png);
                                            border: none;
                                            }
                                            
                                            QPushButton::hover{
                                            image:url(./resources/title_frame_imgs/exit_hover.png);
                                            border: 0px solid #00b66d;}
                                            
                                            QPushButton::pressed{
                                            border: 0px solid #00b66d;}
                                            """)
        self.title_exit_button.clicked.connect(self.title_exit_button_function)
        # layout
        self.title_horizontal_layout = QHBoxLayout(self.title_frame)
        self.title_horizontal_layout.addWidget(self.title_task_text)
        self.title_horizontal_layout.addWidget(self.title_exit_button)
        self.title_horizontal_layout.setStretch(0, 16)
        self.title_horizontal_layout.setStretch(1, 1)
        self.title_horizontal_layout.setSpacing(0)
        self.title_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def _setup_work_frame_widgets(self):
        """init work frame widgets"""
        # work_start_button
        self.work_start_button = QPushButton(self.work_frame)
        self.work_start_button.setGeometry(50, 50, 120, 60)
        self.work_start_button.setFocusPolicy(Qt.NoFocus)
        self.work_start_button.setFlat(True)
        self.work_start_button.setText("START")
        self.work_start_button.setStyleSheet("""
                                            QPushButton{
                                            color: white;
                                            font-family: "微软雅黑";
                                            font-size: 30px;
                                            background-color: #00b66d;}
                                            
                                            QPushButton::hover{
                                            color: black;
                                            font-size: 35px;}
                                            
                                            QPushButton::pressed{
                                            border: 0px solid #00b66d;}
                                            """)
        self.work_start_button.clicked.connect(self.work_start_button_function)
        # work_background_label
        self.work_background_img = QLabel(self.work_frame)
        self.work_background_img.lower()
        background_gif = QMovie("./resources/title_frame_imgs/jijian02.gif")
        self.work_background_img.setMovie(background_gif)
        background_gif.start()
        # layout
        self.work_horizontal_layout = QHBoxLayout(self.work_frame)
        self.work_horizontal_layout.addWidget(self.work_background_img)

        self.work_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def work_start_button_function(self):
        button_function.main_start_button(self.app, self.main_window, self.main_frame, self.databasefunction)

    def title_exit_button_function(self):
        button_function.exit_button(self.app)