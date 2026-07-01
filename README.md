# Brain-tissue
This repository consists of codes that could be used to download datasets from neuroglancer, convert anisotropic dataset to isotropic, and convert them to surface mesh.
First download the data using download_data.npy, then resmaple it to get data in isotropic resolution. Next, convert the output .npy file to .vti file
Use surface_mesh.py to convert the ouput .vti file to .ply file format.
To run surface mesh, use:
python3 surface_mesh.py --infile <Input_file.vti> --outdir <Output_folder> --ncpus 4
