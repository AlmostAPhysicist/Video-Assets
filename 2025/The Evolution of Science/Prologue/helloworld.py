#Create a Manim Scene with a simple text: "Chapter 1"

from manim import *

class ChapterOneScene(Scene):
    def construct(self):
        # Create text object
        title = Text("Chapter 1", font_size=70)
        
        # Position the text slightly above center
        title.shift(UP * 0.5)
        
        # Animate the text creation with fade in and grow
        self.play(
            Write(title),
            run_time=2
        )
        
        # Hold the frame for a moment
        self.wait(2)