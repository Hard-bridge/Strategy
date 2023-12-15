from tkinter import *
from random import *
from time import *
from pole import *
from pers import *
from math import sqrt


pole = Pole()
root = Tk()
root.geometry(f'{pole.field_size[0] * pole.kletka_size}x{pole.field_size[1]*pole.kletka_size}')
canvas = Canvas(bg='green')
canvas.place(x=0, y=0, width=pole.field_size[0]*pole.kletka_size, height=pole.field_size[1]*pole.kletka_size)

chozen_unit = None

def start():
    global pole
    for i in range(2):
        for j in range(12):
            f = Unit()
            f.i = i + 1
            f.j = j + 1
            f.team = 1
            pole.units.append(f)
    for i in range(pole.field_size[1]-2, pole.field_size[1]):
        for j in range(12):
            f = Unit()
            f.i = i + 1
            f.j = j + 1
            f.team = 2
            pole.units.append(f)

def oblast_hoda(x, y):
    r = 3.5*pole.kletka_size
    print(x-r, y-r, x+r, y+r)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=None)
    canvas.create_oval(x-3, y-3, x+3, y+3, fill='blue')

def show():
    global chozen_unit
    canvas.delete(ALL)
    for unit in pole.units:
        if unit.team == 1:
            color = 'red'
        else:
            color = 'blue'
        canvas.create_oval((unit.j-1)*pole.kletka_size, (unit.i-1)*pole.kletka_size,
                           unit.j*pole.kletka_size, unit.i*pole.kletka_size, fill=color)
        canvas.create_text((unit.j-1)*pole.kletka_size, (unit.i-1)*pole.kletka_size, text=str(unit.hp))
    if chozen_unit is not None:
        x = chozen_unit.j * pole.kletka_size - 0.5 * pole.kletka_size
        y = chozen_unit.i * pole.kletka_size - 0.5 * pole.kletka_size
        oblast_hoda(x, y)
    root.after(1000, show)


def clik(event):
    global chozen_unit
    j = event.x//pole.kletka_size + 1
    i = event.y//pole.kletka_size + 1
    if chozen_unit != None:
        for unit in pole.units:
            if i == unit.i and j == unit.j:
                return
        chozen_unit.move(j, i)
        chozen_unit = None
        return
    for unit in pole.units:
        if i == unit.i and j == unit.j:
            if chozen_unit == None:
                chozen_unit = unit
                return


def risuem_pole():
    for i in range(pole.field_size[0]+1):
        canvas.create_line(i*pole.kletka_size, 0, i*pole.kletka_size, pole.field_size[1]*pole.kletka_size, fill='grey')
    for j in range(pole.field_size[1]+1):
        canvas.create_line(0, j*pole.kletka_size, pole.field_size[0]*pole.kletka_size, j*pole.kletka_size, fill='grey')


canvas.bind('<1>', clik)

start()
risuem_pole()
print(len(pole.units))
show()



root.mainloop()
