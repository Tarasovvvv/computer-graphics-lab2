class Storage:
    """Класс, представляющий хранилище."""

    def __init__(self, m, h, r, C, L, canvas_width, canvas_height, x0, y0):
        self.t = 0
        self.m = m
        self.h = h
        self.r = r
        self.C = C
        self.L = L
        self.x0 = x0
        self.y0 = y0
        self.running = True
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.about = "A Python application with tkinter that allows you to look at the damped vibrations of a ball suspended on a spring"
        self.version = "v0.0.1\n\nAdded\n\n- Working header menu with About, Version and Help\n\n- All program logic is divided into two classes: Storage, Controller"
        self.help = "The program displays an animation of a decaying oscillation of a ball suspended on a spring."

    def get_t(self):
        return self.t

    def set_t(self, t):
        self.t = t

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h

    def get_r(self):
        return self.r

    def set_r(self, r):
        self.r = r

    def get_C(self):
        return self.C

    def set_C(self, C):
        self.C = C

    def get_L(self):
        return self.L

    def set_L(self, L):
        self.L = L

    def get_x0(self):
        return self.x0

    def set_x0(self, x0):
        self.x0 = x0

    def get_y0(self):
        return self.y0

    def set_y0(self, y0):
        self.y0 = y0

    def get_canvas_width(self):
        return self.canvas_height

    def set_canvas_width(self, canvas_width):
        self.canvas_width = canvas_width

    def get_canvas_height(self):
        return self.canvas_height

    def set_canvas_height(self, canvas_height):
        self.canvas_height = canvas_height

    def get_running(self):
        return self.running

    def set_running(self, running):
        self.running = running

    def get_about(self):
        return self.about

    def get_version(self):
        return self.version

    def get_help(self):
        return self.help
