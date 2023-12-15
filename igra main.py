from tkinter import *
from time import *
from igra import *

world = World()

root = Tk()
root.geometry(f'{world.size}x{world.size}')
canvas = Canvas(bg='light blue')
canvas.place(x=0, y=0, width=world.size, height=world.size)
a = Label(text= f'счёт 0', bg='light blue')
a.place(x=7, y=7)

def start():
    pers1 = Pers(world=world)
    pers1.x = world.size / 2
    pers1.y = world.size / 2
    world.pers.append(pers1)
    stenka = Stenki()
    stenka.napravlenie = choice(stenka.napravlenia)
    world.stenki.append(stenka)


def show():
    canvas.delete(ALL)
    canvas.create_oval(world.pers[0].x - 10, world.pers[0].y - 10, world.pers[0].x + 10, world.pers[0].y + 10,
                       fill='black')
    for stenka in world.stenki:
        if stenka.napravlenie == 'verh':
            canvas.create_rectangle(0, 0, world.size, 5, fill='red')
        if stenka.napravlenie == 'niz':
            canvas.create_rectangle(0, world.size-5, world.size, world.size, fill='red')
        if stenka.napravlenie == 'pravo':
            canvas.create_rectangle(world.size-5, 0, world.size, world.size, fill='red')
        if stenka.napravlenie == 'levo':
            canvas.create_rectangle(0, 0, 5, world.size, fill='red')
    if world.pers[0].status == False:
        canvas.create_text(100, 200, text='game over')
        root.after(3000, root.destroy)


def update():
    world.pers[0].hodit()
    a.config(text=f'счет {world.pers[0].ottalknulsa}')
    print(world.pers[0].ottalknulsa)
    world.stenki[0].update_stenka()
    show()
    root.after(10, update)


def vniz(event):
    world.pers[0].napravlenie = 'vniz'


root.bind('<s>', vniz)


def verh(event):
    world.pers[0].napravlenie = 'verh'


root.bind('<w>', verh)


def vlevo(event):
    world.pers[0].napravlenie = 'vlevo'


root.bind('<a>', vlevo)


def vpravo(event):
    world.pers[0].napravlenie = 'vpravo'


root.bind('<d>', vpravo)

start()
update()
root.mainloop()
