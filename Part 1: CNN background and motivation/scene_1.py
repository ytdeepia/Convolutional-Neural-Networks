from manim import *
import matplotlib.pyplot as plt
from manim_voiceover import VoiceoverScene


class Scene1_1(VoiceoverScene):
    def construct(self):

        img = ImageMobject("images/0_mnist.png").set_resampling_algorithm(
            RESAMPLING_ALGORITHMS["box"]
        )
        img_values = plt.imread("images/0_mnist.png")[:, :, 0]

        img.scale(35)
        img_rect = SurroundingRectangle(img, buff=0, color=GRAY, stroke_width=2)

        # Create a lattice (grid) with the same dimensions as the image
        lattice = NumberPlane(
            x_range=(-14, 14, 1),
            y_range=(-14, 14, 1),
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 1,
            },
            axis_config={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "include_numbers": False,
            },
            faded_line_ratio=0,  # Disable fading of grid lines
        )

        lattice.scale(img.get_height() / lattice.get_height())

        # Create a TexMobject with the coordinate values
        values = []

        cell_width = lattice.get_x_unit_size()
        for i in range(-14, 14):
            for j in range(-13, 15):

                val = int(img_values[14 - j][14 + i] * 255)
                text = Tex(f"{val}")

                coords = lattice.coords_to_point(i, j)
                text.move_to(
                    coords + RIGHT * cell_width / 2 + DOWN * cell_width / 2
                ).scale(img.get_height() / 28)

                values.append(text)

        # Add the values to the scene
        values = VGroup(*values)

        self.wait(2)

        # Display the question

        txt = Tex("What is an image?").scale(1.5)
        self.play(Write(txt))
        self.wait()

        self.play(FadeOut(txt), run_time=1)

        # Display the image and lattice

        self.play(FadeIn(img, img_rect))
        self.wait()

        self.play(FadeIn(lattice))

        # Display the values

        self.play(FadeOut(img), FadeIn(values))

        # Highlight one pixel

        rect_high_value = SurroundingRectangle(
            values[8 * 28 + 12], color=GREEN, stroke_width=3
        )
        rect_low_value = SurroundingRectangle(
            values[25 * 28 + 20], color=RED, stroke_width=3
        )

        self.play(Create(rect_high_value))

        self.play(Create(rect_low_value))

        self.play(
            FadeOut(lattice, img_rect, rect_low_value, rect_high_value),
            FadeOut(values),
            run_time=2,
        )

        text = Tex("An image is a 2D array of values")
        self.play(Write(text))
        self.wait()

        self.play(FadeOut(text), run_time=1)

        self.wait(2)


# Render the scene
if __name__ == "__main__":

    scene = Scene1_1()
    scene.render()
