import time
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
import cv2
import sys
from PyQt5.QtWidgets import *
from detect_qt5 import v5detect
from detect_qt5_2 import v5detect_2

'''摄像头和视频实时检测界面'''


class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.timer_camera1 = QtCore.QTimer()
        self.timer_camera2 = QtCore.QTimer()
        self.timer_camera3 = QtCore.QTimer()
        self.timer_camera4 = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.fps = 0.0
        self.cls = ' '
        # self.fps_2 = 0.0
        # self.cls_2 = ' '

        self.CAM_NUM = 0

        self.__flag_work = 0
        self.x = 0
        self.count = 0
        self.setWindowTitle("交通标志识别系统")
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\logo.ico'))
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\data\\source_image\\backgroud.jpg')))
        self.setPalette(window_pale)
        self.setFixedSize(1600, 900)
        self.myv5 = v5detect()
        self.myv5_2 = v5detect_2()
        self.button_open_camera = QPushButton(self)
        self.button_open_camera.setText(u'打开摄像头')
        self.button_open_camera.setStyleSheet(''' 
                                     QPushButton
                                     {text-align : center;
                                     background-color : white;
                                     font: bold;
                                     border-color: gray;
                                     border-width: 2px;
                                     border-radius: 10px;
                                     padding: 6px;
                                     height : 14px;
                                     border-style: outset;
                                     font : 14px;}
                                     QPushButton:pressed
                                     {text-align : center;
                                     background-color : light gray;
                                     font: bold;
                                     border-color: gray;
                                     border-width: 2px;
                                     border-radius: 10px;
                                     padding: 6px;
                                     height : 14px;
                                     border-style: outset;
                                     font : 14px;}
                                     ''')
        self.button_open_camera.move(10, 180)
        self.button_open_camera.clicked.connect(self.button_open_camera_click)

        self.btn1 = QPushButton(self)
        self.btn1.setText("检测摄像头")
        self.btn1.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.btn1.move(10, 220)
        self.btn1.clicked.connect(self.button_open_camera_click1)

        self.open_video = QPushButton(self)
        self.open_video.setText("打开视频")
        self.open_video.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.open_video.move(10, 260)
        self.open_video.clicked.connect(self.open_video_button)

        self.btn1 = QPushButton(self)
        self.btn1.setText("检测视频")
        self.btn1.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.btn1.move(10, 300)
        self.btn1.clicked.connect(self.detect_video)

        btn2 = QPushButton(self)
        btn2.setText("返回图片检测")
        btn2.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        btn2.move(10, 340)
        btn2.clicked.connect(self.back_lastui)

        btn3 = QPushButton(self)
        btn3.setText("返回主页面")
        btn3.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn3.move(10, 380)
        btn3.clicked.connect(self.back_main)

        self.labeltitle_show_camera = QLabel(self)
        self.labeltitle_show_camera.setText('交通标志识别--视频检测模块')
        self.labeltitle_show_camera.move(430, 40)
        self.labeltitle_show_camera.setStyleSheet("font-size:50px;")
        self.labeltitle_show_camera.adjustSize()

        # 信息显示
        self.label_show_camera = QLabel(self)
        self.label_move = QLabel()
        self.label_move.setFixedSize(140, 100)
        self.label_show_camera.setFixedSize(600, 500)
        self.label_show_camera.setAutoFillBackground(True)
        self.label_show_camera.move(130, 180)
        self.label_show_camera.setText("   ")
        self.label_show_camera.setStyleSheet("QLabel{background:＃E0FFFF;}"
                                             "QLabel{color:rgb(0,0,0);font-size:20px;font-weight:bold;font-family:宋体;}"
                                             )
        self.label_show_camera1 = QLabel(self)
        self.label_show_camera1.setFixedSize(600, 500)
        self.label_show_camera1.setAutoFillBackground(True)
        self.label_show_camera1.move(850, 180)
        self.label_show_camera1.setText("   ")
        self.label_show_camera1.setStyleSheet("QLabel{background:＃E0FFFF;}"
                                              "QLabel{color:rgb(0,0,0);font-size:20px;font-weight:bold;font-family:宋体;}"
                                              )

        self.label_show_camera11 = QLabel(self)
        self.label_show_camera11.setText('Original')
        self.label_show_camera11.move(350, 140)
        self.label_show_camera11.setStyleSheet("font-size:30px;")
        self.label_show_camera11.adjustSize()

        self.label_show_camera22 = QLabel(self)
        self.label_show_camera22.setText("YOLOv5-CA")
        self.label_show_camera22.move(1050, 140)
        self.label_show_camera22.setStyleSheet("font-size:30px;")
        self.label_show_camera22.adjustSize()

        self.label_show_camera2 = QLabel(self)
        self.label_show_camera2.setText('0.00000000   ')
        self.label_show_camera2.move(1000, 720)
        self.label_show_camera2.setStyleSheet("font-size:30px;")
        self.label_show_camera2.adjustSize()

        self.label_show_camera2_2 = QLabel(self)
        self.label_show_camera2_2.setText('0.00000000   ')
        self.label_show_camera2_2.move(300, 720)
        self.label_show_camera2_2.setStyleSheet("font-size:30px;")
        self.label_show_camera2_2.adjustSize()

        self.label_show_camera3 = QLabel(self)
        self.label_show_camera3.setText("推理时延：")
        self.label_show_camera3.move(850, 720)
        self.label_show_camera3.setStyleSheet("font-size:30px;")
        self.label_show_camera3.adjustSize()

        self.label_show_camera3_2 = QLabel(self)
        self.label_show_camera3_2.setText("推理时延：")
        self.label_show_camera3_2.move(150, 720)
        self.label_show_camera3_2.setStyleSheet("font-size:30px;")
        self.label_show_camera3_2.adjustSize()

        self.label_show_camera4 = QLabel(self)
        self.label_show_camera4.setText("推理结果：")
        self.label_show_camera4.move(850, 780)
        self.label_show_camera4.setStyleSheet("font-size:30px;")
        self.label_show_camera4.adjustSize()

        self.label_show_camera4_2 = QLabel(self)
        self.label_show_camera4_2.setText("推理结果：")
        self.label_show_camera4_2.move(150, 780)
        self.label_show_camera4_2.setStyleSheet("font-size:30px;")
        self.label_show_camera4_2.adjustSize()

        self.label_show_camera5 = QLabel(self)
        self.label_show_camera5.setText('none        ')
        self.label_show_camera5.move(1000, 780)
        self.label_show_camera5.setStyleSheet("font-size:30px;")
        self.label_show_camera5.adjustSize()

        self.label_show_camera5_2 = QLabel(self)
        self.label_show_camera5_2.setText('none        ')
        self.label_show_camera5_2.move(300, 780)
        self.label_show_camera5_2.setStyleSheet("font-size:30px;")
        self.label_show_camera5_2.adjustSize()

        self.timer_camera1.timeout.connect(self.show_camera)
        self.timer_camera2.timeout.connect(self.show_camera1)
        self.timer_camera4.timeout.connect(self.show_camera2)
        self.timer_camera4.timeout.connect(self.show_camera3)
        self.clicked = False

        self.frame_s = 3
        '''
        # 设置背景图片
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        self.setPalette(palette1)
        '''

    def back_lastui(self):
        self.timer_camera1.stop()
        self.cap.release()
        self.label_show_camera.clear()
        self.timer_camera2.stop()

        self.label_show_camera1.clear()
        cam_t.close()
        pic_t.show()

    '''摄像头'''

    def back_main(self):
        self.timer_camera1.stop()
        self.cap.release()
        self.label_show_camera.clear()
        self.timer_camera2.stop()

        self.label_show_camera1.clear()
        cam_t.close()
        ui_p.show()

    '''摄像头'''

    def button_open_camera_click(self):
        if self.timer_camera1.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.timer_camera1.start(30)

                self.button_open_camera.setText(u'关闭摄像头')
        else:
            self.timer_camera1.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.timer_camera2.stop()

            self.label_show_camera1.clear()
            self.button_open_camera.setText(u'打开摄像头')

    def show_camera(self):  # 摄像头左边
        flag, self.image = self.cap.read()

        dir_path = os.getcwd()
        camera_source = dir_path + "\\data\\test\\2.jpg"
        cv2.imwrite(camera_source, self.image)

        width = self.image.shape[1]
        height = self.image.shape[0]

        # 设置新的图片分辨率框架
        width_new = 700
        height_new = 500

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = cv2.resize(self.image, (width_new, int(height * width_new / width)))
        else:

            show = cv2.resize(self.image, (int(width * height_new / height), height_new))

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], 3 * show.shape[1], QtGui.QImage.Format_RGB888)

        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def button_open_camera_click1(self):
        if self.timer_camera2.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.timer_camera2.start(30)
                self.button_open_camera.setText(u'关闭摄像头')
        else:
            self.timer_camera2.stop()
            self.cap.release()
            self.label_show_camera1.clear()
            self.button_open_camera.setText(u'打开摄像头')

    def show_camera1(self):
        flag, self.image = self.cap.read()

        cls, timefps, label, im0 = self.myv5.detect(self.image)
        # cls_2, timefps_2, label_2, im0_2 = self.myv5_2.detect(self.image)
        self.fps = timefps
        self.cls = cls
        # self.fps_2 = timefps_2
        # self.cls_2 = cls_2

        # ASFF
        if label == 'debug':
            print("labelkong")

        width = im0.shape[1]
        height = im0.shape[0]

        # 设置新的图片分辨率框架
        width_new = 700
        height_new = 500

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = cv2.resize(im0, (width_new, int(height * width_new / width)))
        else:

            show = cv2.resize(im0, (int(width * height_new / height), height_new))
        im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)

        showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)

        # # yolov5
        # if label_2 == 'debug':
        #     print("labelkong")
        #
        # width = im0_2.shape[1]
        # height = im0_2.shape[0]
        #
        # # 设置新的图片分辨率框架
        # width_new = 700
        # height_new = 500
        #
        # # 判断图片的长宽比率
        # if width / height >= width_new / height_new:
        #
        #     show = cv2.resize(im0_2, (width_new, int(height * width_new / width)))
        # else:
        #
        #     show = cv2.resize(im0_2, (int(width * height_new / height), height_new))
        # im0_2 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
        #
        # showImage_2 = QtGui.QImage(im0_2, im0_2.shape[1], im0_2.shape[0], 3 * im0_2.shape[1], QtGui.QImage.Format_RGB888)


        self.fps = ('%.6f' % self.fps)
        # self.fps_2 = ('%.6f' % self.fps_2)
        self.label_show_camera2.setText(str(self.fps) + "s")
        self.label_show_camera5.setText(self.cls)
        # self.label_show_camera2_2.setText(str(self.fps_2) + "s")
        # self.label_show_camera5_2.setText(self.cls_2)

        self.label_show_camera1.setPixmap(QtGui.QPixmap.fromImage(showImage))
        # self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage_2))

    '''视频检测'''

    def open_video_button(self):

        if self.timer_camera4.isActive() == False:

            imgName, imgType = QFileDialog.getOpenFileName(self, "打开视频", "", "*.mp4;;*.AVI;;*.rmvb;;All Files(*)")

            self.cap_video = cv2.VideoCapture(imgName)

            flag = self.cap_video.isOpened()

            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.show_camera2()
                self.open_video.setText(u'关闭视频')
        else:
            self.cap_video.release()
            self.label_show_camera.clear()
            self.timer_camera4.stop()
            self.frame_s = 3
            self.label_show_camera1.clear()
            self.open_video.setText(u'打开视频')

    def detect_video(self):

        if self.timer_camera4.isActive() == False:
            flag = self.cap_video.isOpened()
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.timer_camera4.start(30)

        else:
            self.timer_camera4.stop()
            self.cap_video.release()
            self.label_show_camera.clear()
            self.label_show_camera1.clear()

    def show_camera2(self):  # 显示视频的左边

        # 抽帧
        length = int(self.cap_video.get(cv2.CAP_PROP_FRAME_COUNT))  # 抽帧
        print(self.frame_s, length)  # 抽帧
        flag, self.image1 = self.cap_video.read()  # image1是视频的
        if flag == True:

            width = self.image1.shape[1]
            height = self.image1.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(self.image1, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(self.image1, (int(width * height_new / height), height_new))

            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], 3 * show.shape[1],
                                     QtGui.QImage.Format_RGB888)

            self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        else:
            self.cap_video.release()
            self.label_show_camera.clear()
            self.timer_camera4.stop()

            self.label_show_camera1.clear()
            self.open_video.setText(u'打开视频')

    def show_camera3(self):

        flag, self.image1 = self.cap_video.read()
        self.frame_s += 1
        if flag == True:
            cls, timefps, label, im0 = self.myv5.detect(self.image1)
            # cls_2, timefps_2, label_2, im0_2 = self.myv5_2.detect(self.image1)
            self.fps = timefps
            self.cls = cls
            # self.fps_2 = timefps_2
            # self.cls_2 = cls_2

            # ASFF
            if label == 'debug':
                print("labelkong")

            width = im0.shape[1]
            height = im0.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(im0, (int(width * height_new / height), height_new))

            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            # print("debug2")

            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)

            # # yolov5
            # if label_2 == 'debug':
            #     print("labelkong")
            #
            # width = im0_2.shape[1]
            # height = im0_2.shape[0]
            #
            # # 设置新的图片分辨率框架
            # width_new = 700
            # height_new = 500
            #
            # # 判断图片的长宽比率
            # if width / height >= width_new / height_new:
            #
            #     show = cv2.resize(im0_2, (width_new, int(height * width_new / width)))
            # else:
            #
            #     show = cv2.resize(im0_2, (int(width * height_new / height), height_new))
            #
            # im0_2 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            #
            # showImage_2 = QtGui.QImage(im0_2, im0_2.shape[1], im0_2.shape[0], 3 * im0_2.shape[1], QtGui.QImage.Format_RGB888)

            self.fps = ('%.6f' % self.fps)
            # self.fps_2 = ('%.6f' % self.fps_2)
            self.label_show_camera2.setText(str(self.fps) + "s")
            self.label_show_camera5.setText(self.cls)

            # self.label_show_camera2_2.setText(str(self.fps_2) + "s")
            # self.label_show_camera5_2.setText(self.cls_2)

            self.label_show_camera1.setPixmap(QtGui.QPixmap.fromImage(showImage))
            # self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage_2))


'''单张图片检测'''

class picture(QWidget):

    def __init__(self):
        super(picture, self).__init__()

        self.str_name = '0'
        self.fps = 0.0
        self.cls = ' '
        self.str_name_2 = '0'
        self.fps_2 = 0.0
        self.cls_2 = ' '

        self.myv5 = v5detect()
        self.myv5_2 = v5detect_2()

        self.resize(1600, 900)
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\logo.ico'))
        self.setWindowTitle("交通标志识别系统")

        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\data\\source_image\\backgroud.jpg')))
        self.setPalette(window_pale)

        camera_or_video_save_path = 'data\\test'
        if not os.path.exists(camera_or_video_save_path):
            os.makedirs(camera_or_video_save_path)

        self.labeltitle = QLabel(self)
        self.labeltitle.setText('交通标志识别--图片检测模块')
        self.labeltitle.move(430, 40)
        self.labeltitle.setStyleSheet("font-size:50px;")
        self.labeltitle.adjustSize()

        self.label1 = QLabel(self)
        self.label1.setText("   ")
        self.label1.setFixedSize(600, 500)
        self.label1.move(140, 180)

        # 左信息框
        self.label1.setStyleSheet("QLabel{background:＃E0FFFF;}"
                                  "QLabel{color:rgb(0,0,0);font-size:20px;font-weight:bold;font-family:宋体;}"
                                  )
        self.label2 = QLabel(self)
        self.label2.setText("   ")
        self.label2.setFixedSize(600, 500)
        self.label2.move(850, 180)

        # 右信息框
        self.label2.setStyleSheet("QLabel{background:＃E0FFFF;}"
                                  "QLabel{color:rgb(0,0,0);font-size:20px;font-weight:bold;font-family:宋体;}"
                                  )

        self.label11 = QLabel(self)
        self.label11.setText('YOLOv5s')
        self.label11.move(350, 140)
        self.label11.setStyleSheet("font-size:30px;")
        self.label11.adjustSize()

        self.label22 = QLabel(self)
        self.label22.setText("YOLOv5-CA")
        self.label22.move(1050, 140)
        self.label22.setStyleSheet("font-size:30px;")
        self.label22.adjustSize()

        self.label3 = QLabel(self)
        self.label3.setText('0.00000000   ')
        self.label3.move(1000, 720)
        self.label3.setStyleSheet("font-size:30px;")
        self.label3.adjustSize()

        self.label3_2 = QLabel(self)
        self.label3_2.setText('0.00000000   ')
        self.label3_2.move(300, 720)
        self.label3_2.setStyleSheet("font-size:30px;")
        self.label3_2.adjustSize()

        self.label4 = QLabel(self)
        self.label4.setText("推理时延：")
        self.label4.move(850, 720)
        self.label4.setStyleSheet("font-size:30px;")
        self.label4.adjustSize()

        self.label4_2 = QLabel(self)
        self.label4_2.setText("推理时延：")
        self.label4_2.move(150, 720)
        self.label4_2.setStyleSheet("font-size:30px;")
        self.label4_2.adjustSize()

        self.label5 = QLabel(self)
        self.label5.setText("推理结果：")
        self.label5.move(850, 780)
        self.label5.setStyleSheet("font-size:30px;")
        self.label5.adjustSize()

        self.label5_2 = QLabel(self)
        self.label5_2.setText("推理结果：")
        self.label5_2.move(150, 780)
        self.label5_2.setStyleSheet("font-size:30px;")
        self.label5_2.adjustSize()

        self.label6 = QLabel(self)
        self.label6.setText('none         ')
        self.label6.move(1000, 780)
        self.label6.setStyleSheet("font-size:30px;")
        self.label6.adjustSize()

        self.label6_2 = QLabel(self)
        self.label6_2.setText('none         ')
        self.label6_2.move(300, 780)
        self.label6_2.setStyleSheet("font-size:30px;")
        self.label6_2.adjustSize()

        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn.move(10, 180)
        btn.clicked.connect(self.openimage)

        btn1 = QPushButton(self)
        btn1.setText("图片检测")
        btn1.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn1.move(10, 220)
        btn1.clicked.connect(self.button1_test)

        btn3 = QPushButton(self)
        btn3.setText("视频和摄像头检测")
        btn3.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn3.move(10, 260)
        btn3.clicked.connect(self.camera_find)

        btn4 = QPushButton(self)
        btn4.setText("返回主页面")
        btn4.setStyleSheet(''' 
                                                             QPushButton
                                                             {text-align : center;
                                                             background-color : white;
                                                             font: bold;
                                                             border-color: gray;
                                                             border-width: 2px;
                                                             border-radius: 10px;
                                                             padding: 6px;
                                                             height : 14px;
                                                             border-style: outset;
                                                             font : 14px;}
                                                             QPushButton:pressed
                                                             {text-align : center;
                                                             background-color : light gray;
                                                             font: bold;
                                                             border-color: gray;
                                                             border-width: 2px;
                                                             border-radius: 10px;
                                                             padding: 6px;
                                                             height : 14px;
                                                             border-style: outset;
                                                             font : 14px;}
                                                             ''')
        btn4.move(10, 300)
        btn4.clicked.connect(self.back_main)

        self.imgname1 = '0'

    def back_main(self):
        pic_t.close()
        ui_p.show()

    def camera_find(self):
        pic_t.close()
        ui_p.close()
        cam_t.show()

    def openimage(self):

        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")

        if imgName != '':
            self.imgname1 = imgName
            self.im0 = cv2.imread(imgName)

            width = self.im0.shape[1]
            height = self.im0.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(self.im0, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(self.im0, (int(width * height_new / height), height_new))

            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))


    def button1_test(self):
        if self.imgname1 != '0':
            QApplication.processEvents()
            cls, timefps, label, im0 = self.myv5.detect(self.im0)
            cls_2, timefps_2, label_2, im0_2 = self.myv5_2.detect(self.im0)
            self.fps = timefps
            self.cls = cls
            self.fps_2 = timefps_2
            self.cls_2 = cls_2

            QApplication.processEvents()

            # ASFF
            width = im0.shape[1]
            height = im0.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(im0, (int(width * height_new / height), height_new))
            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            image_name = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label2.setPixmap(QtGui.QPixmap.fromImage(image_name))

            # 原始
            width = im0_2.shape[1]
            height = im0_2.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(im0_2, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(im0_2, (int(width * height_new / height), height_new))
            im0_2 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            image_name = QtGui.QImage(im0_2, im0_2.shape[1], im0_2.shape[0], 3 * im0_2.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(image_name))

            self.fps = ('%.6f' % self.fps)
            self.fps_2 = ('%.6f' % self.fps_2)
            self.label3.setText(str(self.fps) + "s")
            self.label6.setText(self.cls)
            self.label3_2.setText(str(self.fps_2) + "s")
            self.label6_2.setText(self.cls_2)
        else:
            QMessageBox.information(self, '错误', '请先选择一个图片文件', QMessageBox.Yes, QMessageBox.Yes)

class About(QWidget):

    def __init__(self):
        super(About, self).__init__()


        self.resize(1600, 900)
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\logo.ico'))
        self.setWindowTitle("交通标志识别系统")

        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\data\\source_image\\backgroud.jpg')))
        self.setPalette(window_pale)

        self.About_label1 = QLabel(self)
        self.About_label1.setText("关于软件")
        self.About_label1.move(650, 100)
        self.About_label1.setStyleSheet("font-size:50px;")
        self.About_label1.adjustSize()

        self.About_label1 = QLabel(self)
        self.About_label1.setText("开发日期：2023年05月17日")
        self.About_label1.move(500, 200)
        self.About_label1.setStyleSheet("font-size:35px;")
        self.About_label1.adjustSize()

        self.About_label2 = QLabel(self)
        self.About_label2.setText("版本号： V1.0")
        self.About_label2.move(500, 300)
        self.About_label2.setStyleSheet("font-size:35px;")
        self.About_label2.adjustSize()

        self.About_label3 = QLabel(self)
        self.About_label3.setText("开发语言：Python")
        self.About_label3.move(500, 400)
        self.About_label3.setStyleSheet("font-size:35px;")
        self.About_label3.adjustSize()

        self.About_label3 = QLabel(self)
        self.About_label3.setText("咨询邮箱：1252718719@qq.com")
        self.About_label3.move(500, 500)
        self.About_label3.setStyleSheet("font-size:35px;")
        self.About_label3.adjustSize()

        About_btn2 = QPushButton(self)
        About_btn2.setText("返回上一界面")
        About_btn2.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     ''')
        About_btn2.move(650, 700)
        About_btn2.clicked.connect(self.back_lastui)


    def back_lastui(self):
        about_t.close()
        ui_p.show()


class Use(QWidget):

    def __init__(self):
        super(Use, self).__init__()
        self.resize(1600, 900)
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\logo.ico'))
        self.setWindowTitle("交通标志识别系统")

        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\data\\source_image\\backgroud.jpg')))
        self.setPalette(window_pale)

        self.Use_label1 = QLabel(self)
        self.Use_label1.setText("使用说明")
        self.Use_label1.move(650, 100)
        self.Use_label1.setStyleSheet("font-size:50px;")
        self.Use_label1.adjustSize()


        self.Use_label2 = QLabel(self)
        self.Use_label2.setText("1. 点击”开始识别“选项进入图片检测。")
        self.Use_label2.move(150, 200)
        self.Use_label2.setStyleSheet("font-size:30px;")
        self.Use_label2.adjustSize()

        self.Use_label3 = QLabel(self)
        self.Use_label3.setText("2. 点击”选择图片“读入检测图片。")
        self.Use_label3.move(150, 270)
        self.Use_label3.setStyleSheet("font-size:30px;")
        self.Use_label3.adjustSize()

        self.Use_label4 = QLabel(self)
        self.Use_label4.setText("3. 点击”图片检测“选项对读入图片中的交通标志做出检测，并给出检测结果、推理时间")
        self.Use_label4.move(150, 340)
        self.Use_label4.setStyleSheet("font-size:30px;")
        self.Use_label4.adjustSize()

        self.Use_label6 = QLabel(self)
        self.Use_label6.setText("4. 点击”图片检测“选项，进入视频和摄像头检测界面")
        self.Use_label6.move(150, 410)
        self.Use_label6.setStyleSheet("font-size:30px;")
        self.Use_label6.adjustSize()

        self.Use_label7 = QLabel(self)
        self.Use_label7.setText("5. 点击打开摄像头或者选择视频读入帧形式图片")
        self.Use_label7.move(150, 480)
        self.Use_label7.setStyleSheet("font-size:30px;")
        self.Use_label7.adjustSize()

        self.Use_label8 = QLabel(self)
        self.Use_label8.setText("6. 与图片检测相同，点击检测后会对视频帧中的交通标志实时做出检测，")
        self.Use_label8.move(150, 550)
        self.Use_label8.setStyleSheet("font-size:30px;")
        self.Use_label8.adjustSize()

        self.Use_label9 = QLabel(self)
        self.Use_label9.setText("   并给出检测结果、推理时间")
        self.Use_label9.move(150, 620)
        self.Use_label9.setStyleSheet("font-size:30px;")
        self.Use_label9.adjustSize()

        Use_btn2 = QPushButton(self)
        Use_btn2.setText("返回上一界面")
        Use_btn2.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     ''')
        Use_btn2.move(650, 810)
        Use_btn2.clicked.connect(self.back_lastui)

    def back_lastui(self):
        use_t.close()
        ui_p.show()


class Main_picture(QWidget):

    def __init__(self):
        super(Main_picture, self).__init__()
        self.resize(1600, 900)
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\logo.ico'))
        self.setWindowTitle("交通标志识别系统")

        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\data\\source_image\\backgroud.jpg')))
        self.setPalette(window_pale)

        self.Main_label0 = QLabel(self)
        self.Main_label0.setText("交通标志识别系统")
        self.Main_label0.move(580, 200)
        self.Main_label0.setStyleSheet("font-size:60px;")
        self.Main_label0.adjustSize()

        Main_btn3 = QPushButton(self)
        Main_btn3.setText("开始检测")
        Main_btn3.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     ''')
        Main_btn3.move(250, 600)
        Main_btn3.clicked.connect(self.camera_find)

        Main_btn4 = QPushButton(self)
        Main_btn4.setText("关于软件")
        Main_btn4.setStyleSheet(''' 
                                                             QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                             ''')
        Main_btn4.move(675,600)
        Main_btn4.clicked.connect(self.About_find)

        Main_btn5 = QPushButton(self)
        Main_btn5.setText("使用说明")
        Main_btn5.setStyleSheet(''' 
                                                             QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 6px;
                                                     border-radius: 60px;
                                                     padding: 12px;
                                                     height : 30px;
                                                     border-style: outset;
                                                     font : 35px;}
                                                             ''')
        Main_btn5.move(1100, 600)
        Main_btn5.clicked.connect(self.Use_find)


    def camera_find(self):
        pic_t.close()
        ui_p.close()
        pic_t.show()

    def About_find(self):
        ui_p.close()
        about_t.show()

    def Use_find(self):
        ui_p.close()
        use_t.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(".\\data\\source_image\\logo.png"))
    # 设置画面中的文字的字体
    splash.setFont(QFont('Gesture recognition UI', 12))
    # 显示画面
    splash.show()
    # 显示信息
    splash.showMessage("程序初始化中... 0%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    time.sleep(0.3)
    splash.showMessage("正在加载模型配置文件...60%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    cam_t = Ui_MainWindow()
    pic_t = picture()
    about_t = About()
    use_t = Use()
    splash.showMessage("正在加载模型配置文件...100%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)

    ui_p = Main_picture()
    ui_p.show()
    splash.close()

    sys.exit(app.exec_())
