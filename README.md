# Image Colour Compression with K-Means Clustering

Reduces the number of colours in an image by clustering pixel colours with K-Means and replacing each pixel with its cluster centre. An interactive Jupyter widget lets you pick an image and choose the number of colours `k`.

All code is in [`image_compression.py`](image_compression.py).

---

## How It Works

1. The image is read as RGB (grayscale images are converted to RGB, alpha channels are dropped) and scaled to [0, 1].
2. All pixels are treated as points in RGB space and grouped into `k` clusters with `MiniBatchKMeans`.
3. Each pixel is replaced by the colour of its cluster centre.
4. The compressed and original images are shown side by side, with the number of colours in each.

With `k` colours, each pixel can be stored as an index of `ceil(log2(k))` bits plus a small colour table, instead of 24 bits per pixel. For example, `k = 16` needs 4 bits per pixel, about one sixth of the original. The script shows this figure; it does not write a compressed file.

---

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook
```

1. Put your images in a folder called `images/` next to the script, or change `img_dir` at the top of `image_compression.py`.
2. In a new notebook, run `%run image_compression.py`.
3. Use the dropdown to choose an image and the slider to set `k` (1 to 256).

---

## Fixes in This Version

* The script did not run: `img_dir =` had no value (syntax error). It now defaults to `images/`.
* Images with an alpha channel (many PNGs) or in grayscale crashed when reshaped to 3 colour channels; both are now handled.
* Only image files are listed in the dropdown.
* Fixed the slider option name (`continuous_update`) and the missing brackets in `plt.show()`.
* Added a fixed random seed so results are repeatable.

---

## Tools

Python, NumPy, scikit-learn, scikit-image, Matplotlib, ipywidgets

## License

Apache License 2.0 (see [LICENSE](LICENSE)).
