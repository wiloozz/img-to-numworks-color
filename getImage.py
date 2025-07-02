from PIL import Image
import parameters

if parameters.showResult:
    from kandinsky import *
    
SIMILARITY_THRESHOLD = parameters.similarity_threshold  # // Distance threshold to consider colors "the same"

# // Loads the image
img = Image.open(parameters.SRCimage).convert("RGB")

def getImgPixel(x, y):
    """
    Returns the rgb value a a given pixel of the image
    """
    try:
        r, g, b = img.getpixel((x, y))
        return (r, g, b)
    except:
        return (0, 0, 0)  # // Default color for out-of-bounds (if the image is smaller than 160*120)

# // Function to compute Euclidean distance between two RGB colors
def color_distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5

# // Output text and palette
text = []
palette = [] # // all the colors that will be used
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P","Q","R","S","T","U","V","W","X","Y","Z"] # // the letters that will represent each color (can be changed to any string)

# // Main loop over image pixels
for x in range(160):
    for y in range(120):
        r, g, b = getImgPixel(x, y)
        current_color = (r, g, b)

        # Check if the color is already in the palette (with tolerance)
        found_similar = False
        for col in palette:
            if color_distance(current_color, col) < SIMILARITY_THRESHOLD:
                found_similar = True
                break

        # // If it's not similar and palette has space, add it
        if not found_similar and len(palette) < parameters.colorAmount:
            palette.append(current_color)

        # // Map the pixel to the closest color in the palette
        try:
            # // Find the closest color in the palette
            closest_index = min(range(len(palette)), key=lambda i: color_distance(current_color, palette[i]))
            letter = letters[closest_index]
        except:
            letter = "A"
            closest_index = 0

        text.append(letter)

        if parameters.showResult:
            fill_rect(x*2,y*2,2,2,palette[closest_index])

# // Write result to file
with open(parameters.outputFile, "w") as file:
    file.write("".join(text))

print(f"Palette size: {len(palette)}")
print(f"Palette: {list(palette)}") # // paste this in the palette var in decode.py