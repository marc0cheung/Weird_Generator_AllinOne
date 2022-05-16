import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QMessageBox
from ui_BallsBurgerGenerator import Ui_MainWindow


class BallsBurgerGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.BBGUI = Ui_MainWindow()
        self.BBGUI.setupUi(self)

        self.BBGUI.generate_btn.clicked.connect(self.generate)
        self.BBGUI.exit_btn.clicked.connect(self.close)
        self.BBGUI.about_btn.clicked.connect(self.about)
        self.BBGUI.zhHK_btn.clicked.connect(self.setzhHK)
        self.BBGUI.zhCN_btn.clicked.connect(self.setzhCN)

    def generate(self):
        Uwant = str(self.BBGUI.uwant_input.toPlainText())
        Usee = str(self.BBGUI.usee_input.toPlainText())
        verb = str(self.BBGUI.verb_input.toPlainText())
        flag = Uwant != '' and Usee != '' and verb != ''

        if self.BBGUI.zhCN_btn.isChecked() and flag:
            result = str("今天是" + Uwant + "瘾发作最严重的一次，躺在床上，拼命念大悲咒，难受得一直抓自己眼睛，以为刷知乎没事，看到知乎都在发"
                         + Usee + "，眼睛越来越大都要炸开了一样，拼命扇自己眼睛，越扇越用力，扇到自己眼泪流出来，真的不知道该怎么办，我真的想"
                         + Uwant + "想得要发疯了。我躺在床上会想" + Uwant + "，我洗澡会想"
                         + Uwant + "，我出门会想" + Uwant + "，我走路会想" + Uwant +
                         "，我坐车会想" + Uwant + "，我工作会想" + Uwant + "，我玩手机会想" + Uwant + "，我盯着路边的" + Usee +
                         "看，我盯着马路对面的" + Usee + "看，我盯着地铁里的" + Usee +
                         "看，我盯着网上的" + Usee + "看，我盯着朋友圈别人照片里的" + Usee + "看，我每时每刻眼睛都直直地盯着" + Usee +
                         "看，像一台雷达一样扫视我身边的每一个" + Usee + "，我真的觉得自己像中邪了一样，我对" + Uwant +
                         "的念想似乎都是病态的了，我好孤独啊！真的好孤独啊！这世界上那么多" + Uwant +
                         "为什么没有一个是属于我的。你知道吗？每到深夜，我的眼睛滚烫滚烫，我发病了我要疯狂" + verb + Uwant +
                         "，我要狠狠" + verb + Uwant + "，我的眼睛受不了了，" + Uwant + "，我的" + Uwant + " " + Uwant + "，我的" + Uwant +
                         " " + Uwant + "……………………")

            self.BBGUI.result_textbox.setPlainText(result)

        elif self.BBGUI.zhHK_btn.isChecked() and flag:
            result = str("今天是" + Uwant + "癮發作最嚴重的一次，躺在床上，拼命念大悲咒，難受得一直抓自己眼睛，以為刷知乎沒事，看到知乎都在發"
                         + Usee + "，眼睛越來越大都要炸開了一樣，拼命扇自己眼睛，越扇越用力，扇到自己眼淚流出來，真的不知道該怎麽辦，我真的想"
                         + Uwant + "想得要發瘋了。我躺在床上會想" + Uwant + "，我洗澡會想"
                         + Uwant + "，我出門會想" + Uwant + "，我走路會想" + Uwant +
                         "，我坐車会想" + Uwant + "，我工作會想" + Uwant + "，我玩手機會想" + Uwant + "，我盯著路邊的" + Usee +
                         "看，我盯著馬路對面的" + Usee + "看，盯著地鐵里的" + Usee +
                         "看，我盯著網上的" + Usee + "看，我盯著朋友圈別人照片里的" + Usee + "看，我每時每刻眼睛都直直地盯著" + Usee +
                         "看，像一台雷達一樣掃視我身邊的每一個" + Usee + "，我真的覺得自己像中邪了一樣，我對" + Uwant +
                         "的念想似乎都是病態的了，我好孤獨啊！真的好孤獨啊！這世界上那麽多" + Uwant +
                         "為什麽沒有一個是屬於我的。你知道嗎？每到深夜，我的眼睛滾燙滾燙，我發病了我要瘋狂" + verb + Uwant +
                         "，我要狠狠" + verb + Uwant + "，我的眼睛受不了了，" + Uwant + "，我的" + Uwant + " " + Uwant + "，我的" + Uwant +
                         " " + Uwant + "……………………")

            self.BBGUI.result_textbox.setPlainText(result)

        elif not (self.BBGUI.zhHK_btn.isChecked() or self.BBGUI.zhCN_btn.isChecked()):
            self.BBGUI.result_textbox.setPlainText("未有選擇語言！\nHaven't Select a language! \n还没有选择语言！")

        elif not (flag and (self.BBGUI.zhHK_btn.isChecked() or self.BBGUI.zhCN_btn.isChecked())):
            self.BBGUI.result_textbox.setPlainText("未有輸入內容！\nHaven't Input Content! \n还没有输入内容！")

    def about(self):
        QMessageBox.about(self, "About This Generator", "Designed by Marco Cheung. \nOriginally inspired by Zhihu.")

    def setzhHK(self):
        self.BBGUI.lang_label.setText("選擇語言？")
        self.BBGUI.usee_label.setText("會見到什麼？")
        self.BBGUI.uwant_label.setText("想要什麼？")
        self.BBGUI.verb_label.setText("給一個對應的動詞：")
        self.BBGUI.about_btn.setText("關於")

    def setzhCN(self):
        self.BBGUI.lang_label.setText("选择语言？")
        self.BBGUI.usee_label.setText("会见到什么？")
        self.BBGUI.uwant_label.setText("想要什么？")
        self.BBGUI.verb_label.setText("给一个对应的动词：")
        self.BBGUI.about_btn.setText("关于")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    BBG = BallsBurgerGenerator()
    BBG.show()
    sys.exit(app.exec_())
