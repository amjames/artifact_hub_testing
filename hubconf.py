dependencies = ['torch']
from random_ds import RandomDataset

def get_random_dataset(n_img: int, img_size: int) -> RandomDataset:
    return RandomDataset(n_img, img_size)


def get_ref():
    return "main-latest"



