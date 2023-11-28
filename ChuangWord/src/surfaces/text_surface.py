from PyQt5.Qt import *
from PyQt5.QtCore import Qt
from tools import button_function
from tools.database_function import databaseFunction


class TextSurface():
    def __init__(self, app, main_window, main_frame, task_item):
        self.app = app
        self.main_window = main_window
        self.main_frame = main_frame
        self.task_class = task_item["surface"]
        self.task_info = task_item["content"]
        self.task_level = task_item["level"]
        self.task_related_words = task_item["related_words"]
        self._setup_main_frame()
        self._setup_frames()
        self._setup_title_frame_widgets()
        self._setup_work_frame_widgets()
        self.text_main_frame.show()
        # init function tools
        self.databasefunction = databaseFunction()
        # init done_task_num
        self._setup_done_task_num()

    def _setup_main_frame(self):
        self.text_main_frame = QFrame(self.main_window)
        self.text_main_frame.setGeometry(0, 0, 800, 640)
        self.text_main_frame.raise_()

    def _setup_frames(self):
        # frames
        self.title_frame = QFrame(self.text_main_frame)
        self.title_frame.setStyleSheet("background-color: #ffbd5a;")
        self.work_frame = QFrame(self.text_main_frame)
        self.work_frame.setStyleSheet("background-color: #ffbd5a;")
        # layout
        self.tol_vertical_layout = QVBoxLayout(self.text_main_frame)
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
                                            image:url(./resources/title_frame_imgs/level_""" + self.task_level + """_text.png)
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
                                            background-color: #ffbd5a;
                                            image:url(./resources/title_frame_imgs/exit_text.png);
                                            border: none;
                                            }

                                            QPushButton::hover{
                                            image:url(./resources/title_frame_imgs/exit_hover_text.png);
                                            border: 0px solid #ffbd5a;}

                                            QPushButton::pressed{
                                            border: 0px solid #ffbd5a;}
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
        # work_done_button
        self.work_start_button = QPushButton(self.work_frame)
        self.work_start_button.setGeometry(340, 15, 120, 60)
        self.work_start_button.setFocusPolicy(Qt.NoFocus)
        self.work_start_button.setFlat(True)
        self.work_start_button.setText("done")
        self.work_start_button.setStyleSheet("""
                                            QPushButton{
                                            color: white;
                                            font-family: "微软雅黑";
                                            font-size: 40px;
                                            background-color: #ffbd5a;}

                                            QPushButton::hover{
                                            color: black;
                                            font-size: 45px;}

                                            QPushButton::pressed{
                                            border: 0px solid #ffbd5a;}
                                            """)
        self.work_start_button.clicked.connect(self.work_done_button_function)
        # work_sure_button
        self.work_sure_button = QPushButton(self.work_frame)
        self.work_sure_button.setGeometry(340, 15, 120, 60)
        self.work_sure_button.setFocusPolicy(Qt.NoFocus)
        self.work_sure_button.setFlat(True)
        self.work_sure_button.setText("sure")
        self.work_sure_button.setStyleSheet("""
                                                            QPushButton{
                                                            color: white;
                                                            font-family: "微软雅黑";
                                                            font-size: 40px;
                                                            background-color: #ffbd5a;}

                                                            QPushButton::hover{
                                                            color: black;
                                                            font-size: 45px;}

                                                            QPushButton::pressed{
                                                            border: 0px solid #ffbd5a;}
                                                            """)
        self.work_sure_button.clicked.connect(self.work_sure_button_function)
        self.work_sure_button.hide()
        # work_edit_area
        self.work_edit_area = QTextEdit(self.work_frame)
        self.work_edit_area.setGeometry(20, 100, 760, 400)
        self.work_edit_area.setFont(QFont("微软雅黑", 12))
        self.work_edit_area.setStyleSheet("""
                                        background-color: white;
                                        border: none;
                                        """)
        # work_background_label
        self.work_background_img = QLabel(self.work_frame)
        self.work_background_img.lower()
        background_gif = QMovie("./resources/title_frame_imgs/text.gif")
        self.work_background_img.setMovie(background_gif)
        background_gif.start()
        # layout
        self.work_horizontal_layout = QHBoxLayout(self.work_frame)
        self.work_horizontal_layout.addWidget(self.work_background_img)
        self.work_horizontal_layout.setAlignment(Qt.AlignBottom)

        self.work_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def _setup_done_task_num(self):
        self.done_task_num = 5
        if self.task_level == "excellent":
            self.done_task_num -= 5
        if self.task_level == "great":
            self.done_task_num -= 3
        if self.task_level == "good":
            self.done_task_num -= 1

    def work_done_button_function(self):
        button_function.work_done_button(self.app, self.main_window, self.main_frame,
                                         self.text_main_frame, self.task_class,
                                         self.task_info, self.task_level, self.task_related_words,
                                         self.databasefunction, self.work_edit_area,
                                         self.title_task_text, self.work_start_button,
                                         self.work_sure_button, self.done_task_num)

    def title_exit_button_function(self):
        button_function.exit_button(self.app)

    def work_sure_button_function(self):
        button_function.work_sure_button(self.work_sure_button, self.title_task_text,
                                         self.task_info, self.work_start_button)