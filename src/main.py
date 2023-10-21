from math import e, sqrt, cos
from tkinter import Canvas, Tk, Menu, messagebox, Label
import Controller

root = Tk()
main_menu = Menu()
label = Label()
controller = Controller.Controller(0.15, 0.1, 40, 10, 1, 700, 800, 400, 350)
canvas = Canvas(root, width=controller.get_canvas_width(), height=controller.get_canvas_height())
spring = [canvas.create_line(0, 0, 0, 0) for i in range(20)]
circle = canvas.create_oval(controller.get_x0() - controller.get_r(), controller.get_y0() - controller.get_r(),
                            controller.get_x0() + controller.get_r(), controller.get_y0() + controller.get_r())


def close():  # Функция для закрытия окна
    controller.set_running(False)


def help():
    messagebox.showinfo("Help", controller.get_help())


def about():
    messagebox.showinfo("About", controller.get_about())


def version():
    messagebox.showinfo("Version", controller.get_version())


def update(canvas):
    dy = 100 * controller.get_h() * pow(e, (-controller.get_t() * sqrt(controller.get_C() * controller.get_m()) / (
            2 * controller.get_L()))) * cos(sqrt(controller.get_C() / controller.get_m()) * controller.get_t())
    controller.set_y0(controller.get_y0() + dy)
    controller.set_t(controller.get_t() + 0.01)
    spring_height = controller.get_y0() - 0.1 * controller.get_canvas_height() - controller.get_r() + dy
    x1 = controller.get_x0() - 0.3 * controller.get_r()
    x2 = controller.get_x0() + 0.3 * controller.get_r()
    # Отрисовка пружины
    canvas.delete(spring[0])
    spring[0] = canvas.create_line(controller.get_x0(), 0.1 * controller.get_canvas_height(),
                                   x2, 0.1 * (controller.get_canvas_height() + spring_height))
    for i in range(1, 9):
        canvas.delete(spring[i])
        spring[i] = canvas.create_line(x1, 0.1 * (controller.get_canvas_height() + spring_height * i),
                                       x2, 0.1 * (controller.get_canvas_height() + spring_height * (i + 1)))
    canvas.delete(spring[9])
    spring[9] = canvas.create_line(x1, 0.1 * controller.get_canvas_height() + spring_height * 0.9,
                                   controller.get_x0(), controller.get_y0() - controller.get_r())
    for i in range(9):
        canvas.delete(spring[i + 10])
        spring[i + 10] = canvas.create_line(x1, 0.1 * (controller.get_canvas_height() + spring_height * (i + 1)),
                                            x2, 0.1 * (controller.get_canvas_height() + spring_height * (i + 1)))
    # Отрисовка шарика
    canvas.move(circle, 0, dy)


canvas.pack()
main_menu.add_cascade(label="About", command=about)
main_menu.add_cascade(label="Version", command=version)
main_menu.add_cascade(label="Help", command=help)
root.config(menu=main_menu)
root.protocol("WM_DELETE_WINDOW", close)  # Привязка кнопки закрытия окна к функции close
canvas.create_line(0.3 * controller.get_canvas_width(),
                   0.1 * controller.get_canvas_height(),
                   0.7 * controller.get_canvas_width(),
                   0.1 * controller.get_canvas_height())

for i in range(10):
    canvas.create_line((0.3 + 0.04 * (i + 1)) * controller.get_canvas_width(),
                       (0.1 - 0.02 * sqrt(2)) * controller.get_canvas_height(),
                       (0.3 + 0.04 * i) * controller.get_canvas_width(),
                       0.1 * controller.get_canvas_height())

while controller.get_running():
    update(canvas)
    canvas.after(1, canvas.update())
root.destroy()
