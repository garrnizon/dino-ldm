import os

os.environ['CUDA_VISIBLE_DEVICES'] = '4'
from diffusers.models import AutoencoderKL
import os
import torch
from tqdm import trange
from torchvision.utils import save_image

vae = AutoencoderKL.from_pretrained(f"stabilityai/sd-vae-ft-mse").to('cuda')

dirs = [
    'SiT/283_231_250_0',
    'SiT/283_231_250_50',
    'SiT/283_231_250_100',
    'SiT/283_231_250_150',
    'SiT/283_231_250_200',
    'SiT/283_231_250_250'
]
batch_size = 4


def decode_dir(path):
    print('dir', path)
    ltn_path = path + '/ltn'
    img_path = path + '/img'
    files = sorted(os.listdir(ltn_path))
    
    group_tensors = [torch.load(f'{ltn_path}/{f}', weights_only=False) for f in files]
    group = torch.cat(group_tensors, dim=0)
    size = len(group)
    for i in trange(0, size, batch_size):
        start = i
        end = min(i + batch_size, size)
        latents = group[start: end]
        samples = vae.decode(latents / 0.18215).sample

        for j, sample in enumerate(samples):
            save_image(sample, f"{img_path}/{j + start}.jpg", normalize=True, value_range=(-1, 1))
        # break

    
    save_image(samples, "sample.png", nrow=4, normalize=True, value_range=(-1, 1))


for dir in dirs:
    decode_dir(dir)
