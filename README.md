# Image Compression using K-Means Clustering

## Overview

This project implements an image compression technique using K-Means Clustering. The project allows users to interactively compress images by reducing the number of colors using the K-Means algorithm. The interface is built using ipywidgets, enabling easy adjustment of the number of clusters (colors) for compression.

## Features

- Interactive user interface for selecting images and adjusting the number of clusters.
- Real-time image compression and visualization.
- Easy-to-use widgets for a seamless user experience.

## Usage

1. Ensure you have a directory of images you want to use for compression. Update the `img_dir` variable in the script with the path to your image directory.
   
   ```python
   img_dir = 'path_to_your_image_directory/'
   ```

2. Run the script:
   ```sh
   jupyter notebook
   ```
   
3. Open the notebook containing the code and run all cells. An interactive widget will appear allowing you to:
   - Select an image from the directory.
   - Adjust the number of clusters (colors) for K-Means compression using a slider.

## Code Description

1. **Dependencies:**
   - Imports necessary libraries for image processing, clustering, and interactive widgets.

2. **Interactive Function:**
   - Defines an interactive function `color_compression` that uses ipywidgets to create a user interface.
   - Reads and processes the selected image.
   - Applies K-Means clustering for color compression.
   - Displays the original and compressed images side-by-side.

3. **Widgets:**
   - Uses `interact` and `IntSlider` from ipywidgets to create a slider for adjusting the number of clusters (colors) interactively.

## Project Structure

- `image_compression_kmeans.py`: Main script for image compression using K-Means Clustering.
- `requirements.txt`: List of required Python packages.

## Example

1. Update the `img_dir` variable with the path to your image directory.
   ```python
   img_dir = 'path_to_your_image_directory/'
   ```

2. Run the Jupyter notebook:
   ```sh
   jupyter notebook
   ```

3. Open and run the notebook containing the code. Use the interactive widgets to select an image and adjust the number of clusters for compression.

## Dependencies

- NumPy: For numerical operations.
- Matplotlib: For plotting images.
- scikit-learn: For K-Means clustering.
- scikit-image: For image reading and processing.
- ipywidgets: For interactive widgets in Jupyter notebooks.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or issues, please open an issue or submit a pull request.

## Acknowledgements

- scikit-learn and scikit-image libraries for providing image processing and clustering capabilities.
- ipywidgets for enabling interactive elements in Jupyter notebooks.
