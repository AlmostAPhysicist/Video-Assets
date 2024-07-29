from manim import *

class Txt(Scene):
    def construct(self):
        self.camera.background_color="#f2faff"
        self.play(Create(NumberPlane(axis_config={"color":"#20262e"}, background_line_style={"stroke_color":"#20262e"})))
        b = Text("Hello World", font="Arima", weight=MEDIUM, gradient=("#283d53", "#37867e"))
        self.play(Write(b))
        self.wait()
        self.play(Create(Dot(color="#f03e50").next_to(b, UP)), Create(Dot(color="#20262e").next_to(b, DOWN)))
        self.wait()


class Anim(Scene):
    def construct(self):
        sq = Square()
        self.play(Create(sq))


class Test(Scene):
    def construct(self):
        text = Tex("$x^2$")
        self.play(Write(text))