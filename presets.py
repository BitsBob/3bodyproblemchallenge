import math

PRESET_ORBITS = {
    "simple_three": {
        "bodies": [
            {"x": 640, "y": 360, "vx": 0, "vy": 0, "mass": 1e6, "color": (255, 255, 0)},  # Sun
            {"x": 740, "y": 360, "vx": 0, "vy": 50, "mass": 1, "color": (0, 255, 255)},   # Planet A
            {"x": 540, "y": 360, "vx": 0, "vy": -50, "mass": 1, "color": (255, 0, 255)}   # Planet B
        ]
    },

    "two_to_one_resonance": {
        "bodies": [
            {"x": 640, "y": 360, "vx": 0, "vy": 0, "mass": 1e6, "color": (255, 255, 0)},  # Sun
            {"x": 740, "y": 360, "vx": 0, "vy": 90, "mass": 1, "color": (0, 255, 255)},   # Inner planet (T)
            {"x": 840, "y": 360, "vx": 0, "vy": 90 / math.sqrt(8), "mass": 1, "color": (255, 0, 255)}  # ~2T
        ]
    }
}
