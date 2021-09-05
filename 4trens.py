from tkinter import *
import threading


class trainController():

    def initValues(self):
        self.train1Dist = -1
        self.train1Vel = 400

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
        self.train1 = self.canvas.create_rectangle(19, 20, 39, 40, fill="#060301")

    def train1Move(self):
        if(self.train1Dist<16):
            self.canvas.move(self.train1, 10, 0)
            self.x+=10
        elif(self.train1Dist<33):
            self.canvas.move(self.train1, 0, 10)
            self.y+=10
        elif(self.train1Dist<50):
            self.canvas.move(self.train1, -10, 0)
            self.x-=10
        elif(self.train1Dist<67):
            self.canvas.move(self.train1, 0, -10)
            self.y-=10
        elif(self.train1Dist==67):
            self.train1Dist = -1
            self.canvas.move(self.train1, 10, 0)

        self.train1Dist+=1
        self.canvas.after(self.train1Vel, self.train1Move)

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

    def increaseTrain1Vel(self):
        if(self.train1Vel != 100):
            self.train1Vel -= 100

    def decreaseTrain1Vel(self):
        self.train1Vel += 100

    def startMove(self):
        self.canvas.after(self.train1Vel, self.train1Move)
            

if __name__ == "__main__":

    controller = trainController()
    root, canvas = controller.setUpUI()
    
    controller.initValues()
    controller.setUpTracks()
    controller.setUpTrains()
    controller.setUpControlPanel()

    root.mainloop()