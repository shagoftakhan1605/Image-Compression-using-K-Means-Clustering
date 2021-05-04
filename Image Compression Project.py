from __future__ import print_function
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
#from plot_utils import plot_utils
from sklearn.cluster import MiniBatchKMeans

plt.style.use("ggplot")

from skimage import io
#from sklearn.cluster import KMeans

from ipywidgets import interact, interactive, fixed, interact_manual, IntSlider
import ipywidgets as widgets

plt.rcParams['figure.figsize']  = (20,12)

img = io.imread('C:/Users/This PC/Pictures/Super Heroes/contact_spiderman2.jpg')
#ax = plt.axes(xticks=[],yticks=[])
#ax.imshow(img)

img_data = (img/255.0).reshape(-1,3)
print(img_data.shape)

#x=plot_utils(img_data, title="Input color space: Over 16 million possible colors")
#x.colorSpace()
kmeans = MiniBatchKMeans(16).fit(img_data)
k_colors = kmeans.cluster_centers_[kmeans.predict(img_data)]

img_dir = 'C:/Users/This PC/Pictures/Super Heroes/'

@interact
def color_compression(image=os.listdir(img_dir),
                      k=IntSlider(min=1,max=256,
                                  step=1,value=16,continous_update=False,
                                        layout=dict(width='100%'))):
    input_img = io.imread(img_dir+image)
    img_data = (input_img/255.0).reshape(-1,3)
    kmeans = MiniBatchKMeans(k).fit(img_data)
    k_colors = kmeans.cluster_centers_[kmeans.predict(img_data)]
    
    k_image = np.reshape(k_colors,(input_img.shape))
    
    fig, (ax1,ax2) = plt.subplots(1,2)
    fig.suptitle('K-Means Image Compression',fontsize=20)
    
    ax1.set_title('Compressed')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.imshow(k_image)
    
    ax2.set_title('Original (26,214,4000 colors)')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.imshow(input_img)
    
    
    plt.subplots_adjust(top=0.85)
    plt.show
