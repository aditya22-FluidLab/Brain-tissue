
import numpy as np
from cloudvolume import CloudVolume

cloudpath = "precomputed://https://rhoana.rc.fas.harvard.edu/ng/neha_1mm_roi1_seg0419"
mip = 0
#position = "22528-17408-47"   # MIP 0 voxel coords of CENTER
position="15000-33000-40"
size_nm = np.array([1600, 1600, 1600], dtype=np.float32)

vol = CloudVolume(cloudpath, mip=mip, cache=True, bounded=True)

pos = np.array([int(x) for x in position.split("-")], dtype=np.int64)

size_vox = (size_nm / vol.resolution).astype(np.int64)

print(f"Downloading at MIP 0 (Res: {vol.resolution})")
print(f"Voxel Coordinates: {pos}, Voxel Size: {size_vox}")

img = vol.download_point(pos, size=size_vox).squeeze()

print("Nonzero voxels:", np.count_nonzero(img))
np.save("mouse_loc3_1600nm.npy", img)

