import math
import random
import tkinter as tk

# Configuration
WIDTH, HEIGHT = 600, 600
OUTLINE_SPEED_MS = 5    # Delay between each star on the outline
ANIMATION_FPS_MS = 60    # Frame update interval (~33 FPS)
MAX_GLITTER = 1500        # Number of active sparkles maintaining the heart fill

# Hex color palettes representing brightness levels (Bright -> Medium -> Dim)
COLOR_PALETTES = [
    ["#FFFFFF", "#FFF8DC", "#FFD700", "#B8860B", "#332A00"],  # Gold
    ["#FFFFFF", "#FFB6C1", "#FF69B4", "#C71585", "#33001A"],  # Pink
    ["#FFFFFF", "#E6E6FA", "#9370DB", "#4B0082", "#120024"],  # Lavender
]

class GlitterSparkle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.symbol = random.choice(["✦", "✧", "•", "✨", "*"])
        self.palette = random.choice(COLOR_PALETTES)
        self.font_size = random.randint(8, 14)
        
        # Life cycle states: 0 to len(palette)-1, then fades out
        self.color_idx = 0
        self.direction = 1  # 1 = brightening/fading in, -1 = fading out
        self.is_dead = False

        # Create canvas text item
        self.id = self.canvas.create_text(
            self.x, self.y,
            text=self.symbol,
            fill=self.palette[0],
            font=("Consolas", self.font_size)
        )

    def update(self):
        """Updates color stage to create a fading/twinkling transition."""
        self.color_idx += self.direction

        if self.color_idx >= len(self.palette):
            # Reached peak brightness; start fading out
            self.color_idx = len(self.palette) - 2
            self.direction = -1
        elif self.color_idx < 0:
            # Fully faded out; mark for removal
            self.is_dead = True
            return

        # Update text item color on canvas
        self.canvas.itemconfig(self.id, fill=self.palette[self.color_idx])

    def destroy(self):
        """Removes the element from the Tkinter canvas."""
        self.canvas.delete(self.id)


class HeartAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Heart & Continuous Twinkle Animation")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.outline_points = []
        self.outline_index = 0
        self.active_glitter = []

        self.generate_heart_points()
        self.draw_outline_step()

    def generate_heart_points(self):
        num_points = 120
        for i in range(num_points):
            t = (i / num_points) * 2 * math.pi
            x = 16 * (math.sin(t) ** 3)
            y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

            canvas_x = WIDTH / 2 + x * 15
            canvas_y = HEIGHT / 2 + y * 15
            self.outline_points.append((canvas_x, canvas_y))

    def is_inside_heart(self, px, py):
        x = (px - WIDTH / 2) / 200
        y = -(py - HEIGHT / 2 - 20) / 200

        term1 = (x**2 + y**2 - 1)**3
        term2 = (x**2) * (y**3)
        return (term1 - term2) <= 0

    def draw_outline_step(self):
        if self.outline_index < len(self.outline_points):
            x, y = self.outline_points[self.outline_index]
            color = random.choice(["#FF1493", "#FF69B4", "#FF4500", "#DC143C"])
            self.canvas.create_text(
                x, y, text="★", fill=color, font=("Consolas", random.randint(12, 16), "bold")
            )
            self.outline_index += 1
            self.root.after(OUTLINE_SPEED_MS, self.draw_outline_step)
        else:
            # Start continuous animation mainloop once outline finishes
            self.animate_glitter_loop()

    def spawn_single_glitter(self):
        """Spawns one new glitter sparkle inside the heart shape."""
        attempts = 0
        while attempts < 100:
            rx = random.uniform(WIDTH / 2 - 220, WIDTH / 2 + 220)
            ry = random.uniform(HEIGHT / 2 - 220, HEIGHT / 2 + 220)
            if self.is_inside_heart(rx, ry):
                sparkle = GlitterSparkle(self.canvas, rx, ry)
                self.active_glitter.append(sparkle)
                break
            attempts += 1

    def animate_glitter_loop(self):
        """Infinite animation loop updating active sparkles and spawning replacements."""
        # 1. Maintain active sparkle count up to MAX_GLITTER
        while len(self.active_glitter) < MAX_GLITTER:
            self.spawn_single_glitter()

        # 2. Update existing sparkles and filter out expired ones
        surviving_glitter = []
        for sparkle in self.active_glitter:
            sparkle.update()
            if sparkle.is_dead:
                sparkle.destroy()
            else:
                surviving_glitter.append(sparkle)

        self.active_glitter = surviving_glitter

        # 3. Schedule next frame tick
        self.root.after(ANIMATION_FPS_MS, self.animate_glitter_loop)


if __name__ == "__main__":
    root = tk.Tk()
    app = HeartAnimation(root)
    root.mainloop()