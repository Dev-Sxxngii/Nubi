import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QMessageBox, QFileDialog
from gui.ui_Nubi import Ui_MainWindow 
import main

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_main_buttons()
        self.connect_site_buttons()
        self.setup_condition_buttons()
        self.ui.start_button.clicked.connect(self.validate_inputs)
        self.ui.download.setEnabled(False)
        self.ui.download.clicked.connect(self.show_save_dialog)
        self.excel_object = None

    def connect_main_buttons(self):
        # 버튼 클릭 시 main_stackedWidget 인덱스를 변경
        self.ui.coming_soon_prev_button.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentIndex(0)) # home
        self.ui.info_prev_button.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentIndex(0)) # home
        self.ui.help.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentIndex(1)) # coming soon
        self.ui.setting.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentIndex(2)) # coming soon

    def connect_site_buttons(self):
        # 버튼 클릭 시 site_stackedWidget 인덱스를 변경
        self.ui.eleven_left_button.clicked.connect(lambda: self.ui.site_stackedWidget.setCurrentIndex(2))   # naver
        self.ui.naver_right_button.clicked.connect(lambda: self.ui.site_stackedWidget.setCurrentIndex(0))   # coupang
        self.ui.naver_left_button.clicked.connect(lambda: self.ui.site_stackedWidget.setCurrentIndex(1))    # eleven
        self.ui.coupang_right_button.clicked.connect(lambda: self.ui.site_stackedWidget.setCurrentIndex(2)) # naver


    def setup_condition_buttons(self):
        # 라디오 버튼 그룹화
        self.condition_button_group = QButtonGroup(self)
        self.condition_button_group.addButton(self.ui.recommend_button)
        self.condition_button_group.addButton(self.ui.sales_button)
        self.condition_button_group.addButton(self.ui.newest_button)
        # 라디오 버튼 설정
        self.condition_button_group.setExclusive(True)

    def enable_download_button(self):
        self.ui.download.setEnabled(True)
        self.ui.download.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 255, 0, 0.1);  /* 연한 초록 */
            }
            QPushButton:hover {
                background-color: rgba(0, 200, 0, 0.3);
                border-radius: 10px;
            }
        """)

    def reset_download_button(self):
        self.ui.download.setEnabled(False)
        self.ui.download.setStyleSheet("") 

    def indicate_download_failure(self):
        self.ui.download.setEnabled(False)
        self.ui.download.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 0, 0, 0.1);  /* 연한 붉은색 */
                color: gray;
            }
        """)

    def show_save_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "저장할 위치 선택",
            "",
            "Excel Files (*.xlsx);;All Files (*)",
            options=options
        )
        if file_path and self.excel_object:
            try:
                self.excel_object.save_excel(file_path)  # 여기서 저장!
                self.reset_download_button() 
                QMessageBox.information(self, "저장 완료", "엑셀 파일이 저장되었습니다.")
            except Exception as e:
                QMessageBox.critical(self, "오류", f"저장 실패: {e}")

    def validate_inputs(self):
        # 1. 검색창 내용 검사
        search_text = self.ui.search_bar_input.text().strip()
        if not search_text:
            QMessageBox.warning(self, "입력 오류", "검색창에 상품명을 입력해 주세요.")
            return

        # 2. 라디오 버튼 선택 검사
        if self.condition_button_group.checkedButton() is None:
            QMessageBox.warning(self, "입력 오류", "검색 조건을 선택해주세요.")
            return

        # 3. 페이지 수 입력 검사
        page_text = self.ui.page_input_text.text().strip()
        if not page_text:
            QMessageBox.warning(self, "입력 오류", "페이지 수를 입력해 주세요.")
            return
        
        # 4. 현재 선택된 사이트 확인
        text = self.ui.search_bar_input.text()
        page = self.ui.page_input_text.text()
        page = int(page)
        current_index = self.ui.site_stackedWidget.currentIndex()
        if current_index == 1:
            site = "COUPANG"
        elif current_index == 0:
            site = "ELEVEN"
        elif current_index == 2:
            site = "NAVER"        
        
        self.excel_object = main.main(site, text, page)

        if self.excel_object:
            self.enable_download_button()
        else:
            self.indicate_download_failure()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())