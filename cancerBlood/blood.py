import os
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

import matplotlib.pyplot as plt

class MyDataset(Dataset):
    def __init__(self, root_dir, crop_size=(16, 16)):
        self.root_dir = root_dir
        self.img_list = os.listdir(root_dir)
        self.transform = transforms.Compose([
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomVerticalFlip(p=0.5),
            transforms.RandomRotation(degrees=30),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
            transforms.ToTensor()
        ])
        self.crop_size = crop_size

    def __len__(self):
        return len(self.img_list)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.img_list[idx])
        img = Image.open(img_path)
        img = self.transform(img)
        x = torch.randint(0, img.shape[-2] - self.crop_size[0] + 1, size=(1,))
        y = torch.randint(0, img.shape[-1] - self.crop_size[1] + 1, size=(1,))
        img1 = img[:, x:x+self.crop_size[0], y:y+self.crop_size[1]]
        return img, img1


dataset = MyDataset('./Blood_Cancer')
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
# dataset[2][0],dataset[2][1]
plt.imshow(dataset[2][0].permute(1,2,0).numpy())
plt.show()
plt.imshow(dataset[2][1].permute(1,2,0).numpy())
plt.show()

