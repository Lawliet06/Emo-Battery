import winreg
import psutil
from plyer import notification
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
import os



# Create GUI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Emo Battery")
        MainWindow.resize(690, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.backgroundLabel = QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.backgroundLabel.setObjectName("backgroundLabel")


        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(150, 250, 111, 41))
        self.startBtn.setObjectName("startBtn")
        self.minimizeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.minimizeBtn.setGeometry(QtCore.QRect(270, 250, 111, 41))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(390, 250, 111, 41))
        self.stopBtn.setObjectName("stopBtn")

        self.percentLabel = QtWidgets.QLabel(self.centralwidget)
        self.percentLabel.setGeometry(QtCore.QRect(300, 200, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.percentLabel.setFont(font)
        self.percentLabel.setObjectName("percentLabel")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Add minimizeButton clicked signal
        self.minimizeBtn.clicked.connect(self.hide)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Emo Battery", "Emo Battery"))
        self.startBtn.setText(_translate("Emo Battery", "Start"))
        self.minimizeBtn.setText(_translate("Emo Battery", "Minimize"))
        self.stopBtn.setText(_translate("Emo Battery", "Stop"))




# Program logic
class BatteryMonitor(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('img/evil.ico'))


        self.setupUi(self)


        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)  # Disable maximize button

        self.startBtn.clicked.connect(self.start_battery_monitor)
        self.minimizeBtn.clicked.connect(self.minimize_battery_monitor)
        self.stopBtn.clicked.connect(self.stop_battery_monitor)

        self.old_percent = 0
        self.last_notification_percent = None

        self.notification_timer = None
        self.battery_timer = None

    def start_battery_monitor(self):
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)
        if self.notification_timer is None:
            self.notification_timer = QtCore.QTimer()
            self.notification_timer.timeout.connect(self.notify)
            self.notification_timer.start(5000)

        if self.battery_timer is None:
            self.battery_timer = QtCore.QTimer()
            self.battery_timer.timeout.connect(self.update_battery_percentage)
            self.battery_timer.start(500)

    def minimize_battery_monitor(self):
        self.hide()
        self.icon = QtGui.QIcon("img/evil.ico")
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.activated.connect(self.showMainWindow)
        self.tray.setToolTip("Emo Battery")
        self.tray.show()

    def showMainWindow(self):
        self.show()

    def stop_battery_monitor(self):
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)
        if self.notification_timer is not None:
            self.notification_timer.stop()
            self.notification_timer = None

        if self.battery_timer is not None:
            self.battery_timer.stop()
            self.battery_timer = None

    def update_battery_percentage(self):
        battery = psutil.sensors_battery()
        self.old_percent = battery.percent
        self.percentLabel.setText(f"Your battery is: 10000%")
        self.update()

    def update(self):
        self.percentLabel.adjustSize()


    def notify(self):
        battery = psutil.sensors_battery()

        new_percent = battery.percent

        print("New percentage is: ", new_percent)


        if battery.power_plugged and new_percent == 17  and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="Hey man dont forget to remove the charger!",
                app_icon='img/bt2.ico',
                timeout=50,
                message=str(new_percent) + "% Battery percentage")
            self.last_notification_percent = new_percent

        elif battery.power_plugged and new_percent == 46 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="I dont think too much power is good for me!",
                app_icon='img/bt3.ico',
                timeout=50,
                message=("My life is ") + str(new_percent) + ("%"))
            self.last_notification_percent = new_percent

        elif battery.power_plugged and new_percent == 90 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="Yes! this power is amazing",
                app_icon=('img/Evil2.ico'),
                timeout=50,
                message=("Power Level ") + str(new_percent) + ("%"))
            self.last_notification_percent = new_percent

        elif battery.power_plugged and new_percent == 95 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="I think am going to explode with this power!",
                app_icon=('img/Evil.ico'),
                timeout=50,
                message=("Power Level ") + str(new_percent) + ("%"))
            self.last_notification_percent = new_percent

        elif battery.power_plugged and new_percent == 100 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="Explosion!",
                app_icon='img/exp.ico',
                timeout=50,
                message=("Power Level ") + str(new_percent) + ("%"))
            self.last_notification_percent = new_percent

        elif not battery.power_plugged and new_percent == 40 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="Dude am dying here plug in the charger!",
                app_icon='img/bt1.ico',
                timeout=50,
                message=str(new_percent) + "% Battery percentage")
            self.last_notification_percent = new_percent

        elif not battery.power_plugged and new_percent == 18 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="If nothing is done now then i will die!",
                app_icon='img/death2.ico',
                timeout=50,
                message=("Battery Life ") + str(new_percent) + ("%"))
            self.last_notification_percent = new_percent

        elif not battery.power_plugged and new_percent == 20 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="It's me again and i ain't playing, i am dying!",
                app_icon=('img/death3.ico'),
                timeout=50,
                message=("Critical ") + str(new_percent) + ("%"))
            self.last_notification_percent = new_percent

        elif not battery.power_plugged and new_percent == 15 and self.last_notification_percent != new_percent:
            notification.notify(
                app_name="Emo battery",
                ticker="Emo battery",
                title="DEATH!",
                app_icon=('img/death1.ico'),
                timeout=50,
                message=("Nothing to see here ") + str(new_percent) + ("%"))
            self.last_notification_percent = new_percent


def add_program_to_startup():
    # Open the "Run" registry key
    run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0,
                             winreg.KEY_WRITE)

    # Set the path to the program executable
    program_path = sys.executable  # Use the current Python executable as the program path

    # Add the program to the "Run" key with a custom name
    winreg.SetValueEx(run_key, "EmoBattery", 0, winreg.REG_SZ, program_path)

    # Close the registry key
    winreg.CloseKey(run_key)


# Main app
if __name__ == "__main__":
    import sys

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    app = QtWidgets.QApplication(sys.argv)
    add_program_to_startup()
    window = BatteryMonitor()
    pixmap = QtGui.QPixmap("img/logo3.png")
    window.backgroundLabel.setPixmap(
        pixmap.scaled(window.backgroundLabel.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))
    window.show()
    sys.exit(app.exec_())
