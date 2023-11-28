from PyQt5.Qt import *
from PyQt5.QtCore import Qt
from tools import button_function
from tools.database_function import databaseFunction


class PhotoSurface():

    def __init__(self, app, main_window, main_frame, task_item):
        self.app = app
        self.main_window = main_window
        self.main_frame = main_frame
        self.task_class = task_item["surface"]
        self.task_info = task_item["content"]
        self.task_level = task_item["level"]
        self._setup_main_frame()
        self._setup_frames()
        self._setup_title_frame_widgets()
        self._setup_work_frame_widgets()
        self.photo_main_frame.show()
        # init function tools
        self.databasefunction = databaseFunction()

    def _setup_main_frame(self):
        self.photo_main_frame = QFrame(self.main_window)
        self.photo_main_frame.setGeometry(0, 0, 800, 640)
        self.photo_main_frame.raise_()

    def _setup_frames(self):
        # frames
        self.title_frame = QFrame(self.photo_main_frame)
        self.title_frame.setStyleSheet("background-color: #f6f6f6;")
        self.work_frame = QFrame(self.photo_main_frame)
        self.work_frame.setStyleSheet("background-color: #f6f6f6;")
        # layout
        self.tol_vertical_layout = QVBoxLayout(self.photo_main_frame)
        self.tol_vertical_layout.setSpacing(0)
        self.tol_vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.tol_vertical_layout.addWidget(self.title_frame)
        self.tol_vertical_layout.addWidget(self.work_frame)
        self.tol_vertical_layout.setStretch(0, 1)
        self.tol_vertical_layout.setStretch(1, 10)

    def _setup_title_frame_widgets(self):
        """init title frame widgets"""
        # title_task_level
        self.title_task_level = QLabel(self.title_frame)
        self.title_task_level.setStyleSheet("""
                                            QWidget{
                                            image:url(./resources/title_frame_imgs/level_""" + self.task_level + """_photo.png)
                                            }
                                            """)
        # title_task_text
        self.title_task_text = QLabel(self.title_frame)
        self.title_task_text.setText(self.task_info)
        self.title_task_text.setAlignment(Qt.AlignCenter)
        self.title_task_text.setStyleSheet("""
                                            QLabel{
                                            font-family: "微软雅黑";
                                            font-size: 30px;
                                            color: black;}

                                            QLabel::hover{
                                            color: #ffd249;}
                                            """)
        # title_exit_button
        self.title_exit_button = QPushButton(self.title_frame)
        self.title_exit_button.setFocusPolicy(Qt.NoFocus)
        self.title_exit_button.setFlat(True)
        self.title_exit_button.setFixedHeight(40)
        self.title_exit_button.setStyleSheet("""
                                            QWidget{
                                            background-color: #f6f6f6;
                                            image:url(./resources/title_frame_imgs/exit_photo.png);
                                            border: none;
                                            }

                                            QPushButton::hover{
                                            image:url(./resources/title_frame_imgs/exit_hover_photo.png);
                                            border: 0px solid #f6f6f6;}

                                            QPushButton::pressed{
                                            border: 0px solid #f6f6f6;}
                                            """)
        self.title_exit_button.clicked.connect(lambda: self.title_exit_button_function())
        # layout
        self.title_horizontal_layout = QHBoxLayout(self.title_frame)
        self.title_horizontal_layout.addWidget(self.title_task_level)
        self.title_horizontal_layout.addWidget(self.title_task_text)
        self.title_horizontal_layout.addWidget(self.title_exit_button)
        self.title_horizontal_layout.setStretch(0, 1)
        self.title_horizontal_layout.setStretch(1, 15)
        self.title_horizontal_layout.setStretch(2, 1)
        self.title_horizontal_layout.setSpacing(0)
        self.title_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def _setup_work_frame_widgets(self):
        """init work frame widgets"""
        # work_start_button
        self.work_start_button = QPushButton(self.work_frame)
        self.work_start_button.setGeometry(340, 260, 120, 60)
        self.work_start_button.setFocusPolicy(Qt.NoFocus)
        self.work_start_button.setFlat(True)
        self.work_start_button.setText("done")
        self.work_start_button.setStyleSheet("""
                                            QPushButton{
                                            color: black;
                                            font-family: "微软雅黑";
                                            font-size: 45px;
                                            background-color: #f6f6f6;}

                                            QPushButton::hover{
                                            color: #ffd249;
                                            font-size: 50px;}

                                            QPushButton::pressed{
                                            border: 0px solid #f6f6f6;}
                                            """)
        self.work_start_button.clicked.connect(self.work_done_button_function)
        # work_blank_label
        self.work_blank_1 = QLabel(self.work_frame)
        # work_background_label
        self.work_background_img = QLabel(self.work_frame)
        self.work_background_img.lower()
        self.work_background_img.setMargin(0)
        # background_img = QPixmap("./resources/title_frame_imgs/camera.png")
        # self.work_background_img.setPixmap(background_img)
        self.work_background_img.setStyleSheet("""
                                                background-color: #f6f6f6;
                                                image: url("./resources/title_frame_imgs/camera.png");
                                                """)
        self.work_background_img.setFixedWidth(120)
        # layout
        self.work_horizontal_layout = QVBoxLayout(self.work_frame)
        self.work_horizontal_layout.addWidget(self.work_blank_1)
        self.work_horizontal_layout.addWidget(self.work_background_img)
        self.work_horizontal_layout.setStretch(0, 12)
        self.work_horizontal_layout.setStretch(1, 2)
        self.work_horizontal_layout.setAlignment(Qt.AlignLeft)
        self.work_horizontal_layout.setSpacing(0)
        self.work_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def work_done_button_function(self):
        button_function.work_done_button(self.app, self.main_window, self.main_frame,
                                         self.photo_main_frame, self.task_class,
                                         self.task_info, self.task_level,
                                         self.databasefunction)

    def title_exit_button_function(self):
        button_function.exit_button(self.app)