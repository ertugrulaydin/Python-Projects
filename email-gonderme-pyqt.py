import  sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.my_mail_label= QtWidgets.QLabel("Mail Adresiniz")
        self.my_mail =  QtWidgets.QLineEdit()
        self.password_label= QtWidgets.QLabel("Parola")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.subject_label= QtWidgets.QLabel("Başlık")
        self.subject = QtWidgets.QLineEdit()
        self.content_label=QtWidgets.QLabel("Mail İçeriği")
        self.content = QtWidgets.QLineEdit()
        self.to_label=QtWidgets.QLabel("Kime")
        self.to = QtWidgets.QLineEdit()
        self.gonder = QtWidgets.QPushButton("Gönder")


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.my_mail_label)
        v_box.addWidget(self.my_mail)
        v_box.addWidget(self.password_label)
        v_box.addWidget(self.password)
        v_box.addWidget(self.subject_label)
        v_box.addWidget(self.subject)
        v_box.addWidget(self.content_label)
        v_box.addWidget(self.content)
        v_box.addWidget(self.to_label)
        v_box.addWidget(self.to)
        v_box.addStretch()
        v_box.addWidget(self.gonder)


        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("Email Gonderme")
        self.gonder.clicked.connect(self.send)

        self.show()
    def send(self):


        email = MIMEMultipart()

        email["From"] = str(self.my_mail.text())
        email_password = str(self.password.text())
        emailto=str(self.to.text())
        email["Subject"]=str(self.subject.text())
        yazi=str(self.content.text())

        email_govdesi = MIMEText(yazi, "plain")

        email.attach(email_govdesi)
        mail = smtplib.SMTP("smtp.gmail.com", 587)

        mail.ehlo()

        mail.starttls()

        mail.login(email["From"], str(email_password))
        mail.sendmail(email["From"], emailto, email.as_string())
        mail.close()


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
