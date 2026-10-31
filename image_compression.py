# Image colour compression with K-Means clustering.
# Run in Jupyter: the @interact widget gives an image dropdown and a slider for k (number of colours).
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from skimage import io
from ipywidgets import interact, IntSlider

plt.style.use("ggplot")

# Folder containing the images to compress (change this to your own folder)
img_dir = "images/"

IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")


def load_rgb(path):
    """Read an image and return it as an RGB float array in [0, 1]."""
    img = io.imread(path)
    if img.ndim == 2:  # grayscale -> RGB
        img = np.stack([img] * 3, axis=-1)
    img = img[..., :3]  # drop alpha channel if present
    if img.dtype != np.uint8:
        img = (img / img.max() * 255).astype(np.uint8) if img.max() > 1 else (img * 255).astype(np.uint8)
    return img.astype(np.float64) / 255.0


def compress(img, k, seed=0):
    """Replace every pixel with the nearest of k cluster-centre colours."""
    pixels = img.reshape(-1, 3)
    kmeans = MiniBatchKMeans(n_clusters=k, random_state=seed, n_init=3).fit(pixels)
    k_colors = kmeans.cluster_centers_[kmeans.predict(pixels)]
    return k_colors.reshape(img.shape)


image_files = sorted(f for f in os.listdir(img_dir) if f.lower().endswith(IMAGE_EXTENSIONS)) if os.path.isdir(img_dir) else []


@interact
def color_compression(image=image_files,
                      k=IntSlider(min=1, max=256, step=1, value=16,
                                  continuous_update=False, layout=dict(width='100%'))):
    input_img = load_rgb(os.path.join(img_dir, image))
    k_image = compress(input_img, k)

    n_original = len(np.unique((input_img * 255).astype(np.uint8).reshape(-1, 3), axis=0))
    bits = max(1, int(np.ceil(np.log2(k))))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('K-Means Image Compression', fontsize=20)

    ax1.set_title(f'Compressed ({k} colours, {bits} bits/pixel)')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.imshow(k_image)

    ax2.set_title(f'Original ({n_original} colours, 24 bits/pixel)')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.imshow(input_img)

    plt.subplots_adjust(top=0.85)
    plt.show()
