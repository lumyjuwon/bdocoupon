import sys
import datetime
import coupon
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pickle

form_class = uic.loadUiType("bdocoupon.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.save_account.stateChanged.connect(self.checkBoxState) # 체크 박스 실행
        self.launch.clicked.connect(self.launch_clicked) # 실행 클릭 시
        self.daumpw_input.setEchoMode(QLineEdit.Password)  # 비밀번호 가리기

        if check_button:
            self.save_account.setChecked(True)

        # 쿠폰 존재 여부 확인
        now = datetime.datetime.now()
        month_day = now.strftime('%m-%d')
        bol, ea = bdo.confirm_state()
        if bol == True:
            self.state.setStyleSheet('color: green')
            self.state.setText(month_day +" 일자 쿠폰이 " + str(ea) + " 개 존재합니다 !")
        elif bol == False:
            self.state.setStyleSheet('color: red')
            self.state.setText(month_day + " 일자 쿠폰이 존재하지 않습니다.")
        else:
            self.state.setStyleSheet('color: green')
            self.state.setText("쿠폰 정보를 불러올 수 없습니다")

    # 계정 저장이 활성화 되어 있을 경우
    def checkBoxState(self):
        if self.save_account.isChecked():
            try:
                file_checkboxstate = open('account.dat', 'rb')
                db = []
                while True:
                    try:
                        db.append(pickle.load(file_checkboxstate))
                    except:
                        break
                self.daumid_input.setText(db[1])
                self.daumpw_input.setText(db[2])
            except:
                pass
        else:
            pass

    def launch_clicked(self):
        daum_id = self.daumid_input.text()
        daum_pw = self.daumpw_input.text()

        if len(daum_id) == 0:
            QMessageBox.about(self, 'Error', '아이디를 입력하세요')
        elif len(daum_pw) == 0:
            QMessageBox.about(self, 'Error', '비밀번호를 입력하세요')
        else:
            if self.save_account.isChecked(): # 저장 체크가 되어 있는 경우 계정 정보 저장
                file_launch = open('account.dat', 'wb')
                pickle.dump('1', file_launch)
                pickle.dump(str(daum_id), file_launch)
                pickle.dump(str(daum_pw), file_launch)
                file_launch.close()
            else: # 저장 케츠가 안 되어 있는 경우 계정 정보 저장을 안 하며 기존 계정 정보 삭제
                file_launch = open('account.dat', 'wb')
                pickle.dump('0', file_launch)
                file_launch.close()

            bdo.launch_process(daum_id, daum_pw)

if __name__ == "__main__":
    check_button = False
    try:
        file = open('account.dat', 'rb')
        if pickle.load(file) == '1':
            check_button = True
    except:
        pass
    bdo = coupon.bdochrome()
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
