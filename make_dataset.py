"""Make the alpha-blend control dataset. Just run it: python make_dataset.py"""
import os, csv, random, urllib.request, tarfile
import numpy as np
from PIL import Image

N_PAIRS, SIZE, SEED, NORMALIZE = 20000, 160, 67, True
ALPHAS = [round(a, 2) for a in np.linspace(0, 1, 5)]
URL = "https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz"
CLASSES = {"n01440764": "tench", "n02102040": "english_springer", "n02979186": "cassette_player",
           "n03000684": "chain_saw", "n03028079": "church", "n03394916": "french_horn",
           "n03417042": "garbage_truck", "n03425413": "gas_pump", "n03445777": "golf_ball",
           "n03888257": "parachute"}

if not os.path.isdir("data/imagenette2-160"):
    os.makedirs("data", exist_ok=True)
    if not os.path.isfile("data/imagenette.tgz"):
        print("downloading imagenette...")
        urllib.request.urlretrieve(URL, "data/imagenette.tgz")
    tarfile.open("data/imagenette.tgz").extractall("data")

by_class = {}
for wnid, label in CLASSES.items():
    d = f"data/imagenette2-160/train/{wnid}"
    by_class[label] = [f"{d}/{f}" for f in os.listdir(d)]

def load(path):
    im = Image.open(path).convert("RGB")
    # for some reason the images  arent all the same size.
    s = min(im.size); w, h = im.size
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2)).resize((SIZE, SIZE))
    a = np.asarray(im, np.float32) / 255
    if NORMALIZE:  
        # Normalize everything to N(0.5,1/4)
        a = np.clip((a - a.mean()) / (a.std() + 1e-6) * 0.25 + 0.5, 0, 1)
    return a

random.seed(SEED)
os.makedirs("data/blended", exist_ok=True)
rows = []
for i in range(N_PAIRS):
    if i % 200 == 0:
        print(f"{i}/{N_PAIRS} done")
    c1, c2 = random.sample(list(by_class), 2)
    p1, p2 = random.choice(by_class[c1]), random.choice(by_class[c2])
    img1, img2 = load(p1), load(p2)
    for alpha in ALPHAS:
        blended = alpha * img1 + (1 - alpha) * img2          
        name = f"pair{i:04d}_a{alpha:.1f}.png"
        Image.fromarray((blended * 255).astype(np.uint8)).save(f"data/blended/{name}")
        dom = "image1" if alpha > 0.5 else "image2" if alpha < 0.5 else "tie" # Class lable 
        rows.append([name, c1, c2, alpha, dom])

with open("data/labels.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["file", "image1", "image2", "alpha", "more_prominent"])
    w.writerows(rows)

print(f"done: {len(rows)} images in data/blended/, labels in data/labels.csv")
