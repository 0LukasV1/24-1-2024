import tkinter as tk

# Mapa nôt na pozície na osnove
note_map = {'c': 50, 'd': 45, 'e': 40, 'f': 35, 'g': 30, 'a': 25, 'h': 20}

def draw_notes():
    # Vytvorenie Tkinter okna a plátna
    window = tk.Tk()
    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()

    # Čítanie nôt z textového súboru
    with open('noty.txt', 'r') as file:
        notes = file.read().replace('\n', '')

    y = 50  # Začiatočná pozícia pre osnovu
    x = 50  # Začiatočná pozícia pre noty

    # Kreslenie nôt a osnovy
    for note in notes:
        if note in note_map:
            if x > 550:  # Ak sa noty nezmestia, vytvorí sa nová osnova
                y += 70
                x = 50
            draw_staff(canvas, y)
            draw_note(canvas, x, y + note_map[note])
            x += 30

    window.mainloop()

def draw_staff(canvas, y):
    for i in range(5):
        canvas.create_line(50, y + i*10, 550, y + i*10)

def draw_note(canvas, x, y):
    canvas.create_oval(x, y, x + 15, y + 10, fill='white')  # Zmenené rozmery a farba

draw_notes()
