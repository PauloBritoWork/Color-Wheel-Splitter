# Color Wheel Splitter

A Python implementation for generating n visually distinct colors by evenly partitioning the HSV color spectrum.

## Project Overview

Color Wheel Splitter provides a mathematical solution to color selection. Traditional random RGB generation often produces clusters of similar hues. By leveraging the cylindrical HSV (Hue, Saturation, Value) color model, this script ensures that each generated color is at the maximum possible angular distance from its neighbors on the color wheel.



## Technical Logic

The script transitions from the RGB cube to the HSV cylinder to handle color as a circular frequency:

* **Hue Partitioning:** The hue is calculated as $H = i / n$, where $i$ is the current index. This effectively divides the 360-degree color wheel into $n$ equal segments.
* **Normalization:** Saturation and Value are held at constant levels (0.8 and 0.9 respectively) to maintain uniform visual weight and prevent "washed out" results.
* **Color Space Conversion:** The resulting HSV coordinates are mapped back to the RGB space using the `colorsys` library and formatted as Hexadecimal strings for UI compatibility.

## Implementation Details

* **Type Safety:** Utilizes Python type hinting (PEP 484) for better IDE support and code clarity.
* **Input Validation:** Implements exception handling to manage non-integer or out-of-bounds user inputs.
* **Standard Library:** Built using zero external dependencies to ensure maximum portability.

## Installation and Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PauloBritoWork/Color-Wheel-Splitter.git
   cd Color-Wheel-Splitter
