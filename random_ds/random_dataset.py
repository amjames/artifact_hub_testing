import torch

from maite import protocols as pr
from torch.utils.data import Dataset

class RandomDataset(Dataset):
    def __init__(self, n_img: int, img_size: int):
        self.data = torch.randn(n_img, 3, img_size, img_size)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return self.data.size(0)
