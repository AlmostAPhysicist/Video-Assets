from manim import *  # Import all necessary classes from Manim

# Sample data (assuming you have years and feature_sizes lists)
years = [2007, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
feature_sizes = [65, 45, 40, 28, 28, 20, 14, 14, 10, 7, 7, 7, 4, 4, 4]

class FeatureSizeAnimation(Scene):
    def construct(self):
        # Create axes (step 1)
        axes = Axes(
            x_range=[min(years) - 1, max(years) + 1],
            y_range=[0, max(feature_sizes) + 5],
            x_label="Year",
            y_label="Feature Size (nm)",
            x_label_buff=0.7,
            y_label_buff=0.5,
        )
        self.play(Create(axes))  # Animate the creation of axes

        # Create data points (step 2)
        dots = Dot(color=RED)  # You can change the color here
        data_points = VGroup()
        for year, size in zip(years, feature_sizes):
            point = dots.copy().move_to(np.array([year, size, 0]))
            data_points.add(point)
        self.play(Create(data_points))  # Animate the creation of data points

        # Create a graph (line) (step 3)
        graph = VMobject()
        for i in range(len(years) - 1):
            start_point = np.array([years[i], feature_sizes[i], 0])
            end_point = np.array([years[i + 1], feature_sizes[i + 1], 0])
            line = Line(start_point, end_point, stroke_width=2)
            graph.add(line)
        self.play(Create(graph))  # Animate the creation of the graph

        # Add a title (optional)
        title = Text("Snapdragon Feature Size over Years", font_size=24).to_corner(UP)
        self.add(title)  # Add the title to the scene

# Run the animation
if __name__ == "__main__":
    animation = FeatureSizeAnimation()
    animation.render()
