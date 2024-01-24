import tkinter as tk
from itertools import cycle
import codecs

class TramDisplay:
    def __init__(self, stops_file):
        with codecs.open(stops_file, 'r', encoding='utf8') as f:
            stops = f.read().splitlines()
            stops.append('Posledná zastávka - Treba vystúpiť!')
            self.stops = cycle(stops)
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=100, bg='black')
        self.canvas.pack()
        self.text = self.canvas.create_text(600, 50, text=next(self.stops), font=("Helvetica", 24), anchor='w', fill='red')
        self.root.bind("<space>", self.next_stop)
        self.move_text()

    def next_stop(self, event):
        stop = next(self.stops)
        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(600, 50, text=stop, font=("Helvetica", 24), anchor='w', fill='red')

    def move_text(self):
        x, y = self.canvas.coords(self.text)
        if x < -self.canvas.bbox(self.text)[2]:
            self.canvas.coords(self.text, 600, 50)
        else:
            self.canvas.move(self.text, -6, 0)  # zdvojnásobená rýchlosť
        self.root.after(100, self.move_text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    display = TramDisplay('zastavky.txt')
    display.run()
