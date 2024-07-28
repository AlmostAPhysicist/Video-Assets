from manim import *

class Test(Scene):
    def construct(self):
        plane = Axes(x_axis_config={"include_numbers": True})
        step = 0.05
        x_max = 5
        num_of_dots = int(x_max / step)
        dots = VGroup(
            *[
                Dot(point=plane.c2p(x, 0), radius=step / 2, color=RED)
                for x in np.arange(0, x_max + step, step)
            ]
        )
        self.add(plane, dots)

        t = ValueTracker(0)
        A = 1  # max displacement
        L = 2  # wavelength => if L (Wavelength)  = 2 then there is one wave every 2 units
        k = (2 * np.pi) / L  # Angular Period / Wavelength (1/wavelength = wavenumber)
        f = 1  # 1 cycle every second
        T = 1 / f # time period
        w = (2 * np.pi) / T # angular frequency
        pulse_speed = L*f
        #NOTE: Pulse end would be at pulse_speed*t at any given time

        for i in range(num_of_dots):
            dots[i].add_updater(
                lambda m, i=i: m.move_to(
                    plane.c2p(
                        step * i, 
                        int((step * i)< pulse_speed*t.get_value() and (step*i)>pulse_speed*(t.get_value()-T))
                        *A * np.sin(k * (step * i) - w * t.get_value())*(-1)
                    )
                ),
                call_updater=True,
            )
        self.add(plane, dots)
        self.play(t.animate.set_value(T*step*num_of_dots/L + T), run_time=5, rate_func=linear)
        self.wait()

class Txt(Scene):
    def construct(self):
        self.camera.background_color="#f2faff"
        self.play(Create(NumberPlane(axis_config={"color":"#20262e"}, background_line_style={"stroke_color":"#20262e"})))
        b = Text("Hello World", font="Arima", weight=MEDIUM, gradient=("#283d53", "#37867e"))
        self.play(Write(b))
        self.wait()
        self.play(Create(Dot(color="#f03e50").next_to(b, UP)), Create(Dot(color="#20262e").next_to(b, DOWN)))
        self.wait()