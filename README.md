# Vnumpy: Vision numpy arrays

## WARNING: This is a simple test version (now it Only can run IN windows OS)!

## Usage

If you have a 3dim numpy arry, And if this data represents a volumetric object. (CT、OCT or other 3dscan date)

### The Vulkan portion of the code will not be open-sourced for now. We use dll。
### your gpu should use vulkan

For example:
```python
import numpy as np
from vnumpy.v3d import npshow2

from batchgenerators.utilities.file_and_folder_operations import join
from nnunetv2.imageio.simpleitk_reader_writer import SimpleITKIO
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor

import nrrd

image_file=r"./input-volume0.nrrd"
image_file2=r"./output-segmentation.nrrd"

print(f"Loading image from {image_file}")
imgs, prop = SimpleITKIO().read_images([image_file])
imgs2, prop2 = SimpleITKIO().read_images([image_file2])

npshow2(imgs[0],imgs2[0])
```
https://github.com/user-attachments/assets/64e736fb-df23-4c56-9836-ce44dab4afb7

## Installation

Install `vnumpy` from [PyPi](https://pypi.org/project/vnumpy):
```
pip install vnumpy
```

## Acknowledgments

This is a Test version now