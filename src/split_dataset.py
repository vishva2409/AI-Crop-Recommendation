import os, shutil, random, csv

random.seed(42)
pairs_csv = "data/image_mask_pairs.csv"
img_src = "data/preprocessed/images"
mask_src = "data/preprocessed/masks"

for split in ["train","val","test"]:
    os.makedirs(os.path.join("data",split,"images"), exist_ok=True)
    os.makedirs(os.path.join("data",split,"masks"), exist_ok=True)

with open(pairs_csv) as f:
    rows = list(csv.DictReader(f))
random.shuffle(rows)

n = len(rows)
n_train = int(0.7*n)
n_val = int(0.15*n)

train = rows[:n_train]
val = rows[n_train:n_train+n_val]
test = rows[n_train+n_val:]

def copy_list(lst, split):
    for r in lst:
        shutil.copy(os.path.join(img_src, r['image']), os.path.join("data",split,"images", r['image']))
        shutil.copy(os.path.join(mask_src, r['mask']), os.path.join("data",split,"masks", r['mask']))

copy_list(train, "train")
copy_list(val, "val")
copy_list(test, "test")

print("✅ Dataset split complete:", len(train), "train,", len(val), "val,", len(test), "test")
