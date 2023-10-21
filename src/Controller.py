import Storage


class Controller:
    """Класс, представляющий контроллер системы."""

    def __init__(self, m, h, r, C, L, canvas_width, canvas_height, x0, y0):
        self.storage = Storage.Storage(m, h, r, C, L, canvas_width, canvas_height, x0, y0)

    def get_t(self):
        return self.storage.t

    def set_t(self, t):
        self.storage.t = t

    def get_m(self):
        return self.storage.m

    def set_m(self, m):
        self.storage.m = m

    def get_h(self):
        return self.storage.h

    def set_h(self, h):
        self.storage.h = h

    def get_r(self):
        return self.storage.r

    def set_r(self, r):
        self.storage.r = r

    def get_C(self):
        return self.storage.C

    def set_C(self, C):
        self.storage.C = C

    def get_L(self):
        return self.storage.L

    def set_L(self, L):
        self.storage.L = L

    def get_x0(self):
        return self.storage.x0

    def set_x0(self, x0):
        self.storage.x0 = x0

    def get_y0(self):
        return self.storage.y0

    def set_y0(self, y0):
        self.storage.y0 = y0

    def get_canvas_width(self):
        return self.storage.canvas_height

    def get_canvas_height(self):
        return self.storage.canvas_height

    def set_running(self, running):
        self.storage.running = running

    def get_running(self):
        return self.storage.running

    def set_running(self, running):
        self.storage.running = running

    def get_running(self):
        return self.storage.running

    def get_about(self):
        return self.storage.about

    def get_version(self):
        return self.storage.version

    def get_help(self):
        return self.storage.help
