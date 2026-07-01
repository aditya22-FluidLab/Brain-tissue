import numpy as np
from scipy.ndimage import zoom

# load downloaded chunk
img = np.load("human_loc3.npy")

# original voxel size (nm) for mouse
#orig_res = np.array([8.0, 8.0, 30.0])

# for human
orig_res=np.array([8.0, 8.0, 33.0])

# target isotropic resolution
target = 10.0

# zoom factors
zoom_factors = orig_res / target

print("Zoom factors:", zoom_factors)

# nearest-neighbor resampling (order=0 for labels)
img_iso = zoom(img, zoom_factors, order=0)

print("Original shape:", img.shape)
print("Isotropic shape:", img_iso.shape)

np.save("human_loc3_iso.npy", img_iso)

print("Saved dilated_iso.npy")

# 1. Count voxels assigned to cells (assuming cells are label > 0)
occupied_voxels = np.count_nonzero(img_iso)

# 2. Get total number of voxels
total_voxels = img_iso.size

# 3. Calculate volume fraction
volume_fraction = (occupied_voxels / total_voxels) * 100

print(f"Total Occupied Voxels: {occupied_voxels}")
print(f"Total Voxel Count: {total_voxels}")
print(f"Volume Fraction: {volume_fraction:.2f}%")
