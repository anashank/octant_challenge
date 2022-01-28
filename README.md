# Octant code challenge

# Required packages:
1. snakemake
2. pandas
3. statsmodels
4. numpy

# Instructions to run
Provide all input and output file names in the ```config.yaml``` file

To run pipeline:
```bash
Dry run: snakemake -n
Actual run: snakemake --cores [number of cores]

Run snakemake --unlock if directory is locked

When re-running pipeline, clean previous files by running:
rm x_y_vals.npy
snakemake --delete-all-output --cores [number of cores]
```
