# ASCII Art Image Converter

**File:** `Task_4.ipynb`

A Python notebook that converts an image into ASCII art using NumPy for pixel-level array manipulation and Pillow (PIL) for image I/O and rendering. The project produces two outputs: a classic **grayscale ASCII art** image and a **colored ASCII art** image where each character is tinted with its original pixel color.

---

## How it works

1. **Load the image** – Reads `smile.png` and converts it into a NumPy array (`height x width x channels`).
2. **Convert to grayscale** – Applies the standard luminosity formula:
   `0.299*R + 0.587*G + 0.114*B`
   to collapse the RGB channels into a single brightness value per pixel.
3. **Downsample into blocks** – Crops the image so its dimensions are divisible by a block size (`10x10` pixels), then reshapes and averages each block to shrink the image into a grid of brightness values — each block becomes one ASCII character.
4. **Map brightness to characters** – Uses a gradient of characters from darkest to lightest:
   ```
   @%#*+=-:.
   ```
   `np.interp` maps each block's average brightness (0–255) to an index in this character set.
5. **Render grayscale ASCII art** – Draws each mapped character onto a new blank image using `ImageDraw`, producing `photo_text.png`.
6. **Render colored ASCII art** – Repeats the block-averaging process on the original RGB image (instead of grayscale) to get the average color of each block, then draws each ASCII character in its corresponding original color, producing `photo_colored.png`.

---

## Concepts practiced
- NumPy array manipulation: reshaping, broadcasting, and multi-axis averaging (`.mean(axis=(1,3))`)
- Image-to-array and array-to-image conversion with Pillow
- Grayscale conversion using the luminosity formula
- Block-based downsampling (image pooling)
- Value mapping/interpolation (`np.interp`)
- Handling RGBA-to-RGB conversion (compositing over a white background)
- Programmatic image generation and text rendering with `ImageDraw`

---

## Requirements
- Python 3.x
- `numpy`
- `Pillow`

Install dependencies:
```bash
pip install numpy pillow
```

## How to run
1. Place an input image named `smile.png` in the same directory the notebook expects (originally `/content/smile.png`, a Google Colab path — update this path if running locally).
2. Run all cells in `Task_4.ipynb` sequentially (e.g., in Jupyter Notebook, JupyterLab, or Google Colab).
3. Outputs are saved to the working directory:
   - `photo_text.png` – black-and-white ASCII art
   - `photo_colored.png` – colored ASCII art

## Notes
- The block size (`10x10` pixels) controls the resolution of the ASCII art — smaller blocks produce more detailed output with more characters; larger blocks produce coarser output.
- The character gradient `"@%#*+=-:. "` can be adjusted to change the visual density/style of the output.
- Two markdown cells in the notebook are written in Arabic, indicating the step being performed (drawing the characters into a new image, and coloring each character by its original pixel color).
