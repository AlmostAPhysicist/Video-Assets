from manim import *

class Anim(Scene):
    def construct(self):

    #Helper Functions
        def int_float(x):
            if x%1:
                return x
            else:
                return int(x)
            
        def frac(num):
            if num == 1:
                return r"\enspace"
            else:
                return r"\enspace \frac{1}{" + str(round(1/num)) + r"} \enspace"
            
        def create_equation(deposit=1, interest_rate=100, interest_period=1):
            count = round(1/interest_period)

            if count == 1:
                return r"\$" + str(deposit) + r"\quad \xrightarrow[\text{per}" + frac(interest_period) + r"\text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**(count)))))

            elif count <= 4:
                starting_arrow = r"\$" + str(deposit) + r"\quad \xrightarrow[\text{per} \enspace" + frac(interest_period) + r"\enspace\text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}}"

                eq = r"\quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**(1))), 2))
                for i in range(2, round(1/interest_period)):
                    eq += r"\quad \xrightarrow[\text{per} \enspace " + frac(interest_period) + r"\enspace \text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**(i))), 2))
            
                ending_arrow = r"\quad \xrightarrow[\text{per} \enspace " + frac(interest_period) + r"\enspace \text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**count)), 2))

                return starting_arrow, eq, ending_arrow
            
            else:
                starting_arrow = r"\$" + str(deposit) + r"\quad \xrightarrow[\text{per} \enspace \text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad \$"

                eq = r"\quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**(1))), 2))
                # eq += r"\quad \xrightarrow[\text{per} \enspace " + frac(interest_period) + r"\enspace \text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**(2))), 2))
                eq += r"\quad \xrightarrow[\text{per} \enspace " + frac(interest_period) + r"\enspace \text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad"
                eq += r"\dots"
                for i in range(count-1, count):
                    eq += r"\quad \xrightarrow[\text{per} \enspace " + frac(interest_period) + r"\enspace \text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**(i))), 2))

                ending_arrow = r"\quad \xrightarrow[\text{per} \enspace " + frac(interest_period) + r"\enspace \text{annum}]{" + str(round(interest_rate, 2)) + r"\% \enspace \text{interest}} \quad \$" + str(round(int_float((deposit)*((1 + (interest_rate/100))**count)), 2))
            
                return starting_arrow , eq, ending_arrow
            

        #Creating the simple Doubling equation

        deposit = MathTex("\$1")
        eq1 = MathTex(create_equation())
        TransformMatchingTex

        self.wait()
        self.play(Write(deposit), run_time=2)
        self.wait()
        self.play(ReplacementTransform(deposit, eq1), run_time=2)
        self.wait(2)


        for i in range(1, 20):
            self.play(Transform(eq1, MathTex(create_equation(2**i))), run_time=0.5*abs(0.5-rate_functions.ease_out_cubic(i/20)))
            

        self.wait(1)

        # text = MathTex(r"\$1 \quad \xrightarrow[\text{per anum}]{100\% \enspace \text{interest}} \quad \$2")
        # text = r""
        # for i in create_equation(1, 100/1000, interest_period=1/1000):
        #     text += i
        # text = MathTex(text)
        # start, middle, end = create_equation(1, 100/4, 1/4)
        # start = MathTex(start)
        # middle = MathTex(middle)
        # end = MathTex(end)

        # start.scale(0.6)
        # middle.scale(0.4)
        # end.scale(0.6)

        # middle.next_to(start, RIGHT, 0.5)
        # end.next_to(middle, RIGHT, 0.5)
        # eq = Group(start, middle, end)
        # eq.move_to(ORIGIN)

        # self.add(start, middle, end)

        # comment = MathTex(r"|\enspace \$1 + \$1")

        #Text and Comment formatting
        # text.set_color("#d8e9e6")
        # comment.set_color("#d8e9e6")
        # comment[0][-2:].set_color("#52b788")
        # comment.set_opacity(0.5)
        # comment.next_to(text, RIGHT, 1)
        
        # eq_writing = [Transform(deposit, text), Write(comment)]

        # text.scale(0.5)

        # self.add(text)
        

        # #Defining Parameters
        # deposit = 1 #dollors
        # interest_rate = 100 #percent
        # interest_period = 1/3 #years - time interval for each calculation of interest
        # final_amt = int_float((deposit)*((1 + (interest_rate/100))**(1/interest_period)))


        # deposit_text = MathTex(rf"\${str(deposit)}")
        # interest_rate_text = MathTex(rf"str(interest_rate)% interest")
        # interest_period_text = MathTex(rf"per str(deposit) annum")
        # final_amt_text = MathTex(rf"\${str(final_amt)}")


        # increments = [
        #     int_float((deposit)*((1 + (interest_rate/100))**(i))) - ((deposit)*(1 + (interest_rate/100))**(i-1)) for i in range(1, 1+round(1/interest_period))
        # ]



        


        # equation = MathTex(equation)
        # self.add(te)
        # comment = MathTex(r"|\enspace \$1 + \$1")
        # self.wait()
        # self.play(Write(deposit), run_time=2)
        # self.wait()
        # self.play(AnimationGroup(*eq_writing, lag_ratio=0.5), run_time=2)
        # self.wait()


class Dial(ThreeDScene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=3, color=WHITE)
        circle.rotate_about_origin(90*DEGREES, RIGHT)
        circle.rotate_about_origin(-90*DEGREES, UP)
        # self.add(circle)
        dial = Group()

        # Parameters
        num_numbers = 21
        angle_increment = 360 / num_numbers

        for i in range(num_numbers):
            angle = i * angle_increment
            number = Text(str(i + 1))
            if i == num_numbers-1:
                number = Text("")
            
            # Position the number on the circle
            number.move_to(circle.point_from_proportion((num_numbers-i) / num_numbers))
            
            # Rotate the number to face radially outwards
            number.rotate(angle * DEGREES, UP)
            
            

            dial.add(number)

        dial.move_to(ORIGIN, OUT)

        black_screen = Square(2)
        black_screen.set_color(RED)
        black_screen.set_fill(RED, opacity=1)
        black_screen.move_to(ORIGIN+2*IN)

        self.add(black_screen)
        self.add(dial)
        
        self.set_camera_orientation(phi=0*DEGREES - 30*DEGREES, theta=-90*DEGREES)
        self.wait()
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES)
        self.wait()
        # self.play(Rotate(dial, (-360*DEGREES) + (2*360/21 * DEGREES), UP), run_time=5)


# # Set opacity based on the number
            # if i == 0:  # Number 1
            #     number.set_opacity(1)
            # elif i == 1:  # Number 2
            #     # number.set_opacity(0.5)
            #     # Create a gradient for number 2
            
            #     number.set_color_by_gradient([WHITE.to_int_rgba_with_alpha(0.75), WHITE.to_int_rgba_with_alpha(0.25)])
            # else:
            #     number.set_opacity(0)
            # if i > 5:
            #     number.set_opacity(0)

            # if i in range(10, 16):
            #     number.set_opacity(1)



class Beauty(Scene):
    def construct(self):
        # self.camera.background_color = WHITE
        line = Line(DOWN*2, DOWN)
        self.wait()
        self.play(Create(line))
        self.wait()
        circle = Circle()
        self.play(ReplacementTransform(line, circle))
        self.wait()

        # svg = SVGMobject("devil.svg")
        # self.wait()
        # self.play(Write(svg), run_time=3, rate_func=rate_functions.ease_in_out_quad)
        # self.wait()



