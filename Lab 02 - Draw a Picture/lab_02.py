import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.MEDIUM_VIOLET_RED)


arcade.start_render()

arcade.draw_circle_filled(500, 550, 40, arcade.color.BLUE)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.BLUE, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.BLUE, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.BLUE, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.BLUE, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.BLUE, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.BLUE, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.BLUE, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.BLUE, 3)

arcade.draw_rectangle_filled(200, 250, 260, 55, arcade.color.GRAY)
arcade.draw_rectangle_filled(250, 250, 260, 69, arcade.color.GRAY)
arcade.draw_rectangle_filled(200, 250, 260, 55, arcade.color.GRAY)
arcade.draw_rectangle_filled(300, 250, 140, 30, arcade.color.YELLOW)
arcade.draw_circle_filled(200, 250, 50, arcade.color.GRAY)
arcade.draw_rectangle_filled(30, 250, 200, 30, arcade.color.ORANGE)

arcade.finish_render()

arcade.run()