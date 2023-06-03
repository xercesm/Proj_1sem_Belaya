from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia #импортируем всё необходимое в проект
import interface  #импортируем конвертированный вариант интерфейса из .ui в .py
import os #для работы с файлами импортируем ОС

class Player(QtWidgets.QMainWindow, interface.Ui_MainWindow): #создаём класс, который будет переходить от QtWidgets к QMainWindow, и от нашего интерфейса
# к Ui_MainWindow
    def __init__(self): #создаём функцию инициализации
        super(Player, self).__init__() #проводим супер-инициализацию
        self.setupUi(self) #после вызываем метод self.setupUi(), в который передаём объект self

        self.pushButton.clicked.connect(self.play) #ставим вызов метода на кнопки, self.play для проигрывания
        self.pushButton_2.clicked.connect(self.stop) #self.stop для остановки
        self.listWidget.itemDoubleClicked.connect(self.play) #cделаем прослушивание по двойному клику, загруженом в списке треков
        self.pushButton_4.clicked.connect(self.load) #создаём для кнопки загрузки треков вызов соответствующего метода

        self.dir = "" #создаем переменную для записи директории

        self.setFixedSize(self.size())#и установим фиксированный размер для нашего интерфейса
        self.setWindowIcon(QtGui.QIcon("icon.ico"))#в корневой папке проекта лежит
        # иконка котoрая присутсвует в интерфейсе, она послужит иконкой для окна

    #начинаем прописывать методы
    def play(self): #создаем метод play в котором создаем:
        item = self.listWidget.currentItem()
        #дальше делаем проверку
        if item:
            file_name = os.path.join(self.dir, item.text())
            content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name)) #после создаем переменную контент
            # куда записываем занчения из QtMultimedia.QMediaContent, а в этот метод передаём file_name

            self.mediaPlayer = QtMultimedia.QMediaPlayer() #теперь создаем self.mediaPlayer, экземпляр QtMultimedia
            self.mediaPlayer.setMedia(content) # через этот экземпляр обращаемся к методу setMedia и передаем туда content
            self.mediaPlayer.play()# а после обращаемся к методу Play для воспроизведения трека
        else: #добавляем блок else в котром вызываем:
            self.listWidget.setCurrentRow(0) #и устанавливаем ему нулевую позицию
            self.play() #после вызываем self.play

        # с помощью этого блока заустится первый трек даже если он не выбран

    def stop(self): #дальше создаем метод stop, в котором вызываем:
        self.mediaPlayer.stop() # для остановки и перезапуска трека

    def load(self): #создаем метод load, в котором обращаемся к:
        self.listWidget.clear() # для того чтобы скачать папку с желаемыми треками

        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory") #теперь создаём переменную dir,
        # в которую выписываем полученную директорию

        if dir: #делаем проверку
            for file_name in os.listdir(dir): # в теле проверки делаем цикл
                if file_name.endswith(".mp3"): # в цикле делаем проверку
                    self.listWidget.addItem(os.path.join(file_name))
            self.dir = dir


if __name__ == '__main__':   #создаем точку входа
    app = QtWidgets.QApplication([])
    player = Player()  #создаем player экземпляр класса player
    player.show()   #вызываем метод show
    app.exec()   #вызываем app.exec