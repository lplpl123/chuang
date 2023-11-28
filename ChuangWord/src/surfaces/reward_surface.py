from PyQt5.Qt import *
from PyQt5.QtCore import Qt
from tools import button_function


class RewardSurface():
    def __init__(self, app, main_window, main_frame, task_class, task_level):
        self.app = app
        self.main_window = main_window
        self.main_frame = main_frame
        self.task_class = task_class
        self.task_level = task_level
        self._setup_main_frame()
        self._setup_frames()
        self._setup_title_frame_widgets()
        self._setup_work_frame_widgets()
        self.reward_main_frame.show()

    def _setup_main_frame(self):
        self.reward_main_frame = QFrame(self.main_window)
        self.reward_main_frame.setGeometry(0, 0, 800, 640)
        self.reward_main_frame.raise_()

    def _setup_frames(self):
        # frames
        self.title_frame = QFrame(self.reward_main_frame)
        self.title_frame.setStyleSheet("background-color: #f3f3f3;")
        self.work_frame = QFrame(self.reward_main_frame)
        self.work_frame.setStyleSheet("background-color: #f3f3f3;")
        # layout
        self.tol_vertical_layout = QVBoxLayout(self.reward_main_frame)
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
        # title_task_text
        self.title_task_text = QLabel(self.title_frame)
        self.title_task_text.setText("恭喜赢得奖励......")
        self.title_task_text.setAlignment(Qt.AlignCenter)
        self.title_task_text.setStyleSheet("""
                                            QLabel{
                                            font-family: "微软雅黑";
                                            font-size: 30px;
                                            color: black;}

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
                                            background-color: #f3f3f3;
                                            image:url(./resources/title_frame_imgs/exit_reward.png);
                                            border: none;
                                            }

                                            QPushButton::hover{
                                            image:url(./resources/title_frame_imgs/exit_hover_reward.png);
                                            border: 0px solid #f3f3f3;}

                                            QPushButton::pressed{
                                            border: 0px solid #f3f3f3;}
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
        self.work_start_button.setText("show")
        self.work_start_button.setStyleSheet("""
                                            QPushButton{
                                            color: black;
                                            font-family: "微软雅黑";
                                            font-size: 40px;
                                            background-color: #ffbd5a;}

                                            QPushButton::hover{
                                            color: black;
                                            font-size: 45px;}

                                            QPushButton::pressed{
                                            border: 0px solid #ffbd5a;}
                                            """)
        self.work_start_button.clicked.connect(self.work_show_button_function)
        # work_complete_button
        self.work_complete_button = QPushButton(self.work_frame)
        self.work_complete_button.hide()
        self.work_complete_button.setGeometry(300, 200, 160, 60)
        self.work_complete_button.setFocusPolicy(Qt.NoFocus)
        self.work_complete_button.setFlat(True)
        self.work_complete_button.setText("complete")
        self.work_complete_button.setStyleSheet("""
                                                    QPushButton{
                                                    color: black;
                                                    font-family: "微软雅黑";
                                                    font-size: 25px;
                                                    background-color: #f3f3f3;}

                                                    QPushButton::hover{
                                                    color: black;
                                                    font-size: 30px;}

                                                    QPushButton::pressed{
                                                    border: 0px solid #f3f3f3;}
                                                    """)
        self.work_complete_button.clicked.connect(self.work_complete_button_function)
        # work_date_label
        self.work_date_label = QLabel(self.work_frame)
        self.work_date_label.setStyleSheet("""
                                            QLabel{
                                            font-family: "微软雅黑";
                                            font-size: 20px;
                                            color: black;}
                                            """)
        # work_blank_label
        self.work_contents_label = QLabel(self.work_frame)
        self.work_contents_label.setWordWrap(True)
        self.work_contents_label.setStyleSheet("""
                                                QLabel{
                                                font-family: "微软雅黑";
                                                font-size: 20px;
                                                color: black;}
                                                """)
        self.work_contents_label.lower()
        # work_background_label
        self.work_background_img = QLabel(self.work_frame)
        self.work_background_img.lower()
        background_gif = QMovie("./resources/title_frame_imgs/reward.gif")
        background_gif.setScaledSize(QSize(100, 100))
        self.work_background_img.setMovie(background_gif)
        background_gif.start()
        # layout
        self.work_horizontal_layout = QVBoxLayout(self.work_frame)
        self.work_horizontal_layout.addWidget(self.work_date_label)
        self.work_horizontal_layout.addWidget(self.work_contents_label)
        self.work_horizontal_layout.addWidget(self.work_background_img)
        self.work_horizontal_layout.setStretch(0, 2)
        self.work_horizontal_layout.setStretch(1, 12)
        self.work_horizontal_layout.setStretch(2, 2)
        self.work_horizontal_layout.setAlignment(Qt.AlignCenter)

        self.work_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def work_show_button_function(self):
        self.work_background_img.hide()
        self.work_start_button.hide()
        if self.task_class == 'text':
            button_function.text_work_show_button(self.app, self.main_window, self.main_frame,
                                                  self.task_class, self.task_level,
                                                  self.title_task_text, self.work_contents_label,
                                                  self.work_date_label)
        self.work_complete_button.show()

    def work_complete_button_function(self):
        button_function.complete_button(self.main_frame, self.reward_main_frame)

    def title_exit_button_function(self):
        button_function.exit_button(self.app)