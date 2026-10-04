import numpy as np


original_art = np.array([
    [  0, 255,   0, 255,   0],  
    [  0, 255,   0, 255,   0],  
    [  0,   0,   0,   0,   0],  
    [255,   0,   0,   0, 255],  
    [  0, 255, 255, 255,   0]   
])


def draw_pixels(grid, title):
    print(f"\n--- {title} ---")
    for row in grid:
        
        line = "".join("██" if val > 100 else "  " for val in row)
        print(line)


draw_pixels(original_art, "Original Smiley")


inverted_art = 255 - original_art
draw_pixels(inverted_art, "Inverted Filter (Negative)")


dimmed_art = original_art // 2
print("\n--- Dimmed Raw Numbers ---")
print(dimmed_art)


flipped_art = np.fliplr(original_art)
draw_pixels(flipped_art, "Mirrored Smiley")
