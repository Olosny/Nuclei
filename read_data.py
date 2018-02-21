from pathlib import Path

import numpy as np
from skimage.io import imread


def main(datadir):
    datapath = Path(datadir) / "stage1_train"
    image_list = datapath.glob("*/images/*.png")

    image_cube = []
    for img in image_list:
        image_cube.append(imread(img))

    outpath = datapath.parent / "stage1_train_images.npy"
    np.save(outpath, np.asarray(image_cube))


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
