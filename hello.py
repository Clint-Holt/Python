from Tkinter import *


class App:
    counter = 1

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        for i in range(16):
            self.button = Button(frame, text='QUIT', bg='black', fg='red', command=quit)
            self.button.pack()

        self.button2 = Button(frame, text='SLOGAN', fg='blue', command=self.write_label)
        self.button2.pack(side=LEFT)

        self.label = Label(root, fg='dark green')

    def write_label(self):
        if self.counter > 1:
            self.label.destroy()

        self.counter += 1
        self.label = Label(text='Label number %d' % self.counter)
        self.label.pack()

root = Tk()
app = App(root)
root.mainloop()
