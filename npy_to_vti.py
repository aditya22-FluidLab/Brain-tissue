
import numpy as np
import pyvista as pv

# 1. Load your processed data
img = np.load("human_loc3_iso.npy")

# 2. Define the grid parameters
# Ensure spacing matches your actual voxel resolution (e.g., 10nm)
spacing = (10, 10, 10)
dims = img.shape

# 3. Create the Uniform Grid (ImageData)
grid = pv.ImageData()
grid.dimensions = dims
grid.spacing = spacing
grid.origin = (0, 0, 0)

# 4. Assign the data correctly to 'point_data'
# The error was likely here; assigning directly to grid["data"]
# doesn't always register the array for the VTK writer.
grid.point_data["values"] = img.flatten(order="F")

# 5. Save the file
grid.save("human_loc3_iso.vti")

print("Successfully saved vf27_ecs_1500nm.vti")

