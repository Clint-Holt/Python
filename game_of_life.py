from Tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.QUIT = Button(self)
        self.run_sym = Button(self)
        self.life_squares = [NONE] * 64
        for row in range(8):
            for column in range(8):

            self.life_squares[i] = Button(self)
            self.life_squares[i]["text"] = " "
            if i > 32:
                self.life_squares[i].pack({"side": "left"})
            else:
                self.life_squares[i].pack({"side": "right"})
        self.create_widgets()

    @staticmethod
    def run():
        print 'hello everybody!'

    def create_widgets(self):

        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.run_sym["text"] = "Run Simulation",
        self.run_sym["command"] = self.run

        self.run_sym.pack({"side": "left"})

root = Tk()
app = Application(master=root)
# for r in range(3):
#     for c in range(4):
#         Label(root, text='R%s/C%s'%(r,c),
#             borderwidth=1 ).grid(row=r,column=c)
app.mainloop()
root.destroy()
