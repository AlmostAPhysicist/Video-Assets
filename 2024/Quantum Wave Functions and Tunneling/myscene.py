from manim import *
class MyScene(ThreeDScene):
    def construct(self):
        self.camera.focal_distance_tracker.set_value(2000)
#Value Trackers
    #QMWave
        phase = ValueTracker(0)
        median_tracker = ValueTracker(-1.25)
        wave_num_tracker = ValueTracker(15.0)
        std_tracker = ValueTracker(0.3)

        #Real_part
        real_wave_end_tracker = ValueTracker(0)
        #Imaginary_part
        imaginary_wave_end_tracker = ValueTracker(0)

        #Probability Density Function
        prob_density_end_tracker = ValueTracker(0)


    #Axes
        x_axis_tracker = ValueTracker(0)
        y_axis_tracker = ValueTracker(0)
        z_axis_tracker = ValueTracker(0)


        def update_phase(phase, dt):
            phase.increment_value(-dt)
        phase.add_updater(update_phase)

# Defining Render Mobjects

    #Axes

        dummy_ax = Axes(x_range=[-2, 2], y_range=[-2, 2], x_length=12)
        x_axis = always_redraw(
                lambda: NumberLine(
                x_range=[-2, -2+4*x_axis_tracker.get_value()],
                stroke_width=3,
                include_tip=False,
                include_ticks=True,
                tick_size=0.075,
                length=12*x_axis_tracker.get_value(),
                color="#f2faff"
            ).shift(LEFT*6 + RIGHT*x_axis_tracker.get_value()*6)
        )
        y_axis = always_redraw(
                lambda: NumberLine(
                x_range=[-2, -2+4*y_axis_tracker.get_value()],
                stroke_width=3,
                include_tip=False,
                include_ticks=True,
                tick_size=0.075,
                length=6*y_axis_tracker.get_value(),
                color="#f2faff"
            ).rotate(PI/2, about_point=ORIGIN).shift(DOWN*3 + UP*y_axis_tracker.get_value()*3)
        )

    #QM Waves and other graphs
        real_wave = always_redraw(
            lambda: dummy_ax.plot(
                lambda x: self.gaussian(x, median_tracker.get_value(), std_tracker.get_value())*self.osc(x, wave_num_tracker.get_value(), phase.get_value()),
                stroke_width = 3,
                color="#2a6f97",
                x_range=[-2,-2+4*real_wave_end_tracker.get_value(), 0.01]
                )
        )


#Manimations        
    #Initial Setting
        self.add(phase, x_axis_tracker, real_wave_end_tracker, x_axis, real_wave)
        self.play(x_axis_tracker.animate(run_time=2).set_value(1), real_wave_end_tracker.animate(run_time=2).set_value(1))

        self.wait(6)
    #XF into other bizzare Waves    
        self.play(median_tracker.animate(run_time=3, rate_func=lambda x: rate_functions.ease_in_out_sine(x)*rate_functions.ease_out_back(x)**6).set_value(0), std_tracker.animate(run_time=6, rate_func=lambda x: rate_functions.there_and_back(1-x)*rate_functions.wiggle(x)).set_value(0.1), wave_num_tracker.animate(run_time=3).set_value(20))
        self.wait(0.1)
        self.add(y_axis_tracker, y_axis)
        self.play(y_axis_tracker.animate(run_time=2).set_value(1))
        self.wait(1.5)

    #Adding the Probability Dist Gaussian
        prob_dist_curve = dummy_ax.plot(
            lambda x: self.gaussian(x, median_tracker.get_value(), std_tracker.get_value())**2,
                x_range=[-2, 2, 0.01],
                stroke_width=3,
                color="#98c1d9"
                )
        dummy_wave = dummy_ax.plot(
            lambda x: self.gaussian(x, median_tracker.get_value(), std_tracker.get_value())*self.osc(x, wave_num_tracker.get_value(), phase.get_value()),
                stroke_width = 3,
                color="#2a6f97",
                x_range=[-2,-2+4*real_wave_end_tracker.get_value(), 0.01]
                )
        self.add(dummy_wave)
        self.play(ReplacementTransform(dummy_wave, prob_dist_curve), run_time=2)
        self.wait(5)

    #Adding the actual Square
        dummy_wave = dummy_ax.plot(
                lambda x: self.gaussian(x, median_tracker.get_value(), std_tracker.get_value())*self.osc(x, wave_num_tracker.get_value(), phase.get_value()),
                stroke_width = 3,
                color="#2a6f97",
                x_range=[-2,-2+4*real_wave_end_tracker.get_value(), 0.01]
                )
        real_square_wave = dummy_ax.plot(
                lambda x: (self.gaussian(x, median_tracker.get_value(), std_tracker.get_value())*self.osc(x, wave_num_tracker.get_value(), phase.get_value()))**2,
                stroke_width = 3,
                color="#2a9d8f",
                x_range=[-2,-2+4*real_wave_end_tracker.get_value(), 0.01]
                )
        self.add(dummy_wave)
        self.play(ReplacementTransform(dummy_wave, real_square_wave), run_time=2)
        self.wait(1)

    #Extrapolating into 3D - The IMAGINARY Axis and Complex Plane
        z_axis = NumberLine(
                x_range=[-2, 2],
                stroke_width=3,
                include_tip=False,
                include_ticks=True,
                tick_size=0.075,
                length=6,
                color="#f07167"
            ).rotate(PI/2, UP, about_point=ORIGIN)
        imaginary_wave = always_redraw(
            lambda: dummy_ax.plot(
                lambda x: self.gaussian(x, median_tracker.get_value(), std_tracker.get_value())*self.osc(PI/2 - x, wave_num_tracker.get_value(), phase.get_value()),
                stroke_width = 3,
                color="#f07167",
                x_range=[-2,2, 0.01]
                ).rotate(PI/2, RIGHT, about_point=ORIGIN)
        )
        self.wait(1)
        self.play(
            ReplacementTransform(real_square_wave, imaginary_wave), 
        )
        self.add(z_axis)
        self.play(self.camera.phi_tracker.animate(run_time=2).set_value(-60*DEGREES))
        self.play(self.camera.theta_tracker.animate(run_time=5, rate_func=rate_functions.ease_in_out_cubic).set_value(-275*DEGREES))
        self.play(Uncreate(real_wave), Uncreate(imaginary_wave), self.camera.phi_tracker.animate.set_value(0*DEGREES), self.camera.theta_tracker.animate.set_value(-90*DEGREES), run_time=3)
    #Now We're back in 2d Gaussians
        self.play(FadeOut(x_axis), FadeOut(y_axis), FadeOut(z_axis), run_time=2)
        self.wait(2)






    
    





    #my functions

    def gaussian(self, x, mu, sigma):
        """
        Calculate the value of a Gaussian distribution at point x
        with mean mu and standard deviation sigma.
        """
        exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
        coefficient = 1 / (sigma * np.sqrt(2 * np.pi))

        return coefficient * np.exp(exponent)
    def osc(self, x, wavenumber, phase):
        return np.sin((wavenumber*x + phase))
    


from manim import *

class Al(Scene):
    def construct(self):
        v = ValueTracker(0)
        dummy_ax = Axes(x_range=[-2, 2], x_length=12)
        # a.coords_to_point()
        nl = always_redraw(lambda: NumberLine(
            x_range=[-2,-2+4*v.get_value()],
            length=12*v.get_value()
        ).shift(LEFT*6 + RIGHT*v.get_value()*6)
        )
        # nl.coords
        pointer = always_redraw(lambda: Dot(dummy_ax.coords_to_point(-2+4*v.get_value(), 0)+UP))
        self.add(nl, pointer)
        self.play(v.animate(run_time=2).set_value(1))

class Test(ThreeDScene):
    def construct(self):
        self.camera.focal_distance_tracker.set_value(20000)
        ax = Axes()
        def gaussian(x, mu, sigma):
            """
            Calculate the value of a Gaussian distribution at point x
            with mean mu and standard deviation sigma.
            """
            exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
            coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
            return coefficient * np.exp(exponent)
        
        graph = ax.plot(lambda x: gaussian(x, 0, 2)).rotate(PI/2, RIGHT, about_point=ORIGIN)
        self.add(ax, graph)