# NumPy Pixel Art Filters

A lightweight Python project demonstrating how real digital images and photo filters work under the hood using **NumPy** 2D arrays and vectorization.

---

# Features

- **Pixel Grid Canvas:** Represents grayscale pixels ($0$ for black, $255$ for bright white) as a matrix.
- **Instant Filters (Vectorization):**
  - **Invert:** Color negative effect (`255 - image`).
  - **Brightness:** Scale pixel intensities across the whole array.
  - **Mirror / Flip:** Horizontal image reflection using `np.fliplr()`.
- **Terminal Renderer:** Renders numeric grids into clean ASCII block art in the terminal.

---

# Requirements

- Python 3.x
- NumPy

```bash
pip install numpy
