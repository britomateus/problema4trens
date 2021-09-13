from tkinter import *
import threading


class trainController():

    def initValues(self):
        self.train1Dist = -1
        self.train2Dist = -1
        self.train3Dist = -1
        self.train4Dist = -1
        self.train1Vel = 400
        self.train2Vel = 400
        self.train3Vel = 400
        self.train4Vel = 400

    def setUpUI(self):        
        self.root = Tk()
        self.root.title('Problema dos 4 Trens - STR')
        self.root.geometry('900x400')
        self.root.config(bg='#fff')

        self.canvas = Canvas(self.root,height=400,width=900,bg="#fff")
        self.canvas.pack()
        return self.root, self.canvas

    def setUpTracks(self):
        self.canvas.create_rectangle(30, 30, 200, 200, outline="#63ccdb", width=5)
        self.canvas.create_rectangle(200, 30, 370, 200, outline="#af96f9", width=5)
        self.canvas.create_rectangle(370, 30, 540, 200, outline="#fdc300", width=5)
        self.canvas.create_rectangle(30, 200, 540, 370, outline="#fe4e6c", width=5)

    def setUpTrains(self):
        self.train1 = self.canvas.create_rectangle(20, 20, 40, 40, fill="#060301")
        self.train2 = self.canvas.create_rectangle(190, 20, 210, 40, fill="#060301")
        self.train3 = self.canvas.create_rectangle(360, 20, 380, 40, fill="#060301")
        self.train4 = self.canvas.create_rectangle(20, 190, 40, 210, fill="#060301")

    def train1Move(self):
        if(self.train1Dist<16):
            self.canvas.move(self.train1, 10, 0)
        elif(self.train1Dist<33):
            self.canvas.move(self.train1, 0, 10)
        elif(self.train1Dist<50):
            self.canvas.move(self.train1, -10, 0)
        elif(self.train1Dist<67):
            self.canvas.move(self.train1, 0, -10)
        elif(self.train1Dist==67):
            self.train1Dist = -1
            self.canvas.move(self.train1, 10, 0)

        self.train1Dist+=1
        self.canvas.after(self.train1Vel, self.train1Move)

    def train2Move(self):
        if(self.train2Dist<16):
            self.canvas.move(self.train2, 10, 0)
        elif(self.train2Dist<33):
            self.canvas.move(self.train2, 0, 10)
        elif(self.train2Dist<50):
            self.canvas.move(self.train2, -10, 0)
        elif(self.train2Dist<67):
            self.canvas.move(self.train2, 0, -10)
        elif(self.train2Dist==67):
            self.train2Dist = -1
            self.canvas.move(self.train2, 10, 0)

        self.train2Dist+=1
        self.canvas.after(self.train2Vel, self.train2Move)

    def train3Move(self):
        if(self.train3Dist<16):
            self.canvas.move(self.train3, 10, 0)
        elif(self.train3Dist<33):
            self.canvas.move(self.train3, 0, 10)
        elif(self.train3Dist<50):
            self.canvas.move(self.train3, -10, 0)
        elif(self.train3Dist<67):
            self.canvas.move(self.train3, 0, -10)
        elif(self.train3Dist==67):
            self.train3Dist = -1
            self.canvas.move(self.train3, 10, 0)

        self.train3Dist+=1
        self.canvas.after(self.train3Vel, self.train3Move)

    def train4Move(self):
        if(self.train4Dist<50):
            self.canvas.move(self.train4, 10, 0)
        elif(self.train4Dist<67):
            self.canvas.move(self.train4, 0, 10)
        elif(self.train4Dist<118):
            self.canvas.move(self.train4, -10, 0)
        elif(self.train4Dist<135):
            self.canvas.move(self.train4, 0, -10)
        elif(self.train4Dist==135):
            self.train4Dist = -1
            self.canvas.move(self.train4, 10, 0)
        
        self.train4Dist+=1
        self.canvas.after(self.train4Vel, self.train4Move)

    def setUpControlPanel(self):
        self.canvas.create_text(720,35,text="Painel de Controle", font="Helvetica 20 bold")

        #define button play content
        self.play = Button(self.root, text="Iniciar", width=5, font="Helvetica 15 bold", command=self.startMove)
        self.canvas.create_window(720,70,window=self.play)
        
        #define train 1 control panel
        self.canvas.create_text(600,110,text="Trem 1", font="Helvetica 15")
        self.increaseTrain1 = Button(self.root, text="+", width=3, font="Helvetica 20 bold", command=self.increaseTrain1Vel)
        self.canvas.create_window(720,110,window=self.increaseTrain1)

        self.decreaseTrain1 = Button(self.root, text="-", width=3, font="Helvetica 20 bold", command=self.decreaseTrain1Vel)
        self.canvas.create_window(800,110,window=self.decreaseTrain1)

        #define train 2 control panel
        self.canvas.create_text(600,150,text="Trem 2", font="Helvetica 15")
        self.increaseTrain2 = Button(self.root, text="+", width=3, font="Helvetica 20 bold", command=self.increaseTrain2Vel)
        self.canvas.create_window(720,150,window=self.increaseTrain2)

        self.decreaseTrain2 = Button(self.root, text="-", width=3, font="Helvetica 20 bold", command=self.decreaseTrain2Vel)
        self.canvas.create_window(800,150,window=self.decreaseTrain2)

        #define train 3 control panel
        self.canvas.create_text(600,190,text="Trem 3", font="Helvetica 15")
        self.increaseTrain3 = Button(self.root, text="+", width=3, font="Helvetica 20 bold", command=self.increaseTrain3Vel)
        self.canvas.create_window(720,190,window=self.increaseTrain3)

        self.decreaseTrain3 = Button(self.root, text="-", width=3, font="Helvetica 20 bold", command=self.decreaseTrain3Vel)
        self.canvas.create_window(800,190,window=self.decreaseTrain3)

        #define train 4 control panel
        self.canvas.create_text(600,230,text="Trem 4", font="Helvetica 15")
        self.increaseTrain4 = Button(self.root, text="+", width=3, font="Helvetica 20 bold", command=self.increaseTrain4Vel)
        self.canvas.create_window(720,230,window=self.increaseTrain4)

        self.decreaseTrain4 = Button(self.root, text="-", width=3, font="Helvetica 20 bold", command=self.decreaseTrain4Vel)
        self.canvas.create_window(800,230,window=self.decreaseTrain4)
    
    #define velocity control for train 1
    def increaseTrain1Vel(self):
        if(self.train1Vel != 100):
            self.train1Vel -= 100

    def decreaseTrain1Vel(self):
        self.train1Vel += 100

    #define velocity control for train 2
    def increaseTrain2Vel(self):
        if(self.train2Vel != 100):
            self.train2Vel -= 100

    def decreaseTrain2Vel(self):
        self.train2Vel += 100

    #define velocity control for train 3
    def increaseTrain3Vel(self):
        if(self.train3Vel != 100):
            self.train3Vel -= 100

    def decreaseTrain3Vel(self):
        self.train3Vel += 100

    #define velocity control for train 4
    def increaseTrain4Vel(self):
        if(self.train4Vel != 100):
            self.train4Vel -= 100

    def decreaseTrain4Vel(self):
        self.train4Vel += 100

    def startMove(self):
        self.t1.start()
        self.t2.start()
        self.t3.start()
        self.t4.start()

    def setUpThreads(self):
        self.t1 = threading.Thread(target=self.train1Move)
        self.t2 = threading.Thread(target=self.train2Move)
        self.t3 = threading.Thread(target=self.train3Move)
        self.t4 = threading.Thread(target=self.train4Move)

    def joinThreads(self):
        self.t1.join()
        self.t2.join()
        self.t3.join()
        self.t4.join()

if __name__ == "__main__":

    controller = trainController()
    root, canvas = controller.setUpUI()
    
    controller.initValues()
    controller.setUpThreads()
    controller.setUpTracks()
    controller.setUpTrains()
    controller.setUpControlPanel()

    root.mainloop()

    controller.joinThreads()