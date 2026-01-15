import colorsys


def generate_colors(n: int) -> list[str]:
    """
    Generates n visually distinct colors by evenly spacing
    them across the HSV color wheel.

    Args:
        n (int): The number of colors to generate.

    Returns:
        list[str]: A list of hex color strings.
    """
    unique_colors = []

    for i in range(n):
        # We divide the Hue (0.0 to 1.0) into n equal slices.
        # This ensures the maximum possible 'distance' between each color.
        hue = i / n

        # Saturation 0.8 and Value 0.9 give a vibrant but not 'neon' look.
        saturation = 0.8
        value = 0.9

        # colorsys.hsv_to_rgb returns a tuple of (r, g, b) from 0.0 to 1.0
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)

        # Convert the 0-1 float values to 0-255 integers
        rgb_int = tuple(int(channel * 255) for channel in rgb)

        # Format as a Hex string (e.g., #FFFFFF)
        hex_color = '#%02x%02x%02x' % rgb_int
        unique_colors.append(hex_color)

    return unique_colors


def main():
    print("--- Color Wheel Splitter ---")

    try:
        user_input = input("How many colours would you like to generate? ")
        count = int(user_input)

        if count <= 0:
            print("Please enter a number greater than 0.")
            return

        print(f"\nGenerated {count} colors:\n" + "=" * 20)

        results = generate_colors(count)
        for hex_code in results:
            # We can print the hex code and a small visual 'block'
            # using ANSI escape codes for terminals that support it.
            print(f"{hex_code}  ■")

    except ValueError:
        print("Error: Please enter a valid whole number.")


if __name__ == "__main__":
    main()
