import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.cm as cm
import Tkinter as tk  # python 2.7
import ttk            # python 2.7
import sys

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.createWidgets()

    def createWidgets(self):
        fig=plt.figure(figsize=(8,8))
        ax=fig.add_axes([0.1,0.1,0.8,0.8])
        ax.set_ylim(-400,400)
        ax.set_xlim(-400,400)
        ax.axhline(ls='--',color='black')
        ax.axvline(ls='--',color='black')
        canvas=FigureCanvasTkAgg(fig,master=root)
        canvas.get_tk_widget().grid(row=0,column=1)
        canvas.show()

        colors = cm.rainbow(np.linspace(0,1,56))
        self.cplotbutton=tk.Button(master=root, text="continuous\nplot", command=lambda: self.continuous_plot(canvas,ax,colors))
        self.cplotbutton.grid(row=0,column=0)
        self.plotbutton=tk.Button(master=root, text="plot", command=lambda: self.plot(canvas,ax,colors))
        self.plotbutton.grid(row=1,column=0)
        self.plotbutton.place(x=10,y=300)
        self.plotbutton=tk.Button(master=root, text="no\nclear\nplot", command=lambda: self.noclear_plot(canvas,ax,colors))
        self.plotbutton.grid(row=1,column=0)
        self.plotbutton.place(x=10,y=500)

    def continuous_plot(self,canvas,ax,colors):
        while True:
            self.plot(canvas,ax,colors)
        return

    def noclear_plot(self,canvas,ax,colors):
        c = 20
        while c > 0:
            try:
                filename = "test/csv1x3.csv"
                raw = np.genfromtxt(filename, delimiter=',')
            except:
                print("error")
            else:
                if len(raw)>= 56:
                    for r,color in zip(raw,colors):
                        ax.plot(r[0],r[1],linestyle="None",marker='o',color=color)
                    canvas.draw()
                    c -= 1
                else:
                    print("len not enough")
        return
            
    def plot(self,canvas,ax,colors):
        try:
            filename = "test/csv1x3.csv"
            raw = np.genfromtxt(filename, delimiter=',')
        except:
            print("error")
            return
        else:
            if len(raw)>= 56:
                ax.clear()
                ax.set_ylim(-400,400)
                ax.set_xlim(-400,400)
                ax.axhline(ls='--',color='black')
                ax.axvline(ls='--',color='black')
                for r,color in zip(raw,colors):
                    ax.plot(r[0],r[1],linestyle="None",marker='o',color=color)
                canvas.draw()
            else:
                print("len not enough")
            return


root=tk.Tk()
app=Application(master=root)
app.mainloop()