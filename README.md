# Nuclei
Kaggle Data Science bowl challenge 2018 *Find the nuclei* 

* [Homepage](https://www.kaggle.com/c/data-science-bowl-2018)
* [Data](https://www.kaggle.com/c/data-science-bowl-2018/data)


#### `read_data.py`

Once the data downloaded and unzipped, run this script to create a
unique file `stage1_train_images.npy` easy to read with all the images.

Usage:
```
python read_data.py <path_to_the_stage1_train_directory>
python read_data.py data  # if files uncompressed in data/stage1_train/...
```

Example for displaying the images in [this notebook](visualize_images.ipynb).
