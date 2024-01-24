import tkinter as tk

class Tron:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()
        self.snake = [(100, 100)]
        self.direction = 'Up'
        self.canvas.bind_all('<Key>', self.change_direction)

    def change_direction(self, event):
        if event.keysym == 'Up':
            self.direction = 'Up'
        elif event.keysym == 'Down':
            self.direction = 'Down'
        elif event.keysym == 'Left':
            self.direction = 'Left'
        elif event.keysym == 'Right':
            self.direction = 'Right'

    def move(self):
        head = self.snake[0]
        if self.direction == 'Up':
            new_head = (head[0], head[1] - 1)
        elif self.direction == 'Down':
            new_head = (head[0], head[1] + 1)
        elif self.direction == 'Left':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'Right':
            new_head = (head[0] + 1, head[1])

        if new_head in self.snake:
            return False

        self.snake.insert(0, new_head)
        self.canvas.create_line(head[0], head[1], new_head[0], new_head[1], fill='black')
        return True

    def run(self):
        if self.move():
            self.canvas.after(100, self.run)
        else:
            self.canvas.create_text(100, 100, text='Game Over', fill='red')

root = tk.Tk()
tron = Tron(root)
tron.run()
root.mainloop()
