import os, csv

img_dir = "data/preprocessed/images"
mask_dir = "data/preprocessed/masks"
out_csv = "data/image_mask_pairs.csv"

img_files = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg','.png'))])
rows = []
for f in img_files:
    mask = os.path.splitext(f)[0] + ".png"
    if os.path.exists(os.path.join(mask_dir, mask)):
        rows.append((f, mask))

with open(out_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["image","mask"])
    writer.writerows(rows)

print("✅ Saved", out_csv)
