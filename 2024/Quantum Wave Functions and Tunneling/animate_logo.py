from manim import *

class Logo(Scene):
    def construct(self):
        logo = SVGMobject("./Logo_edges.svg", height=10, stroke_color="#20262e")
        self.wait()
        self.play(Write(logo), run_time=4)
        self.wait(2)