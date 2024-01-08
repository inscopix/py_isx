# Read name of a cell in a CellSet

!!! note "Assumptions"
    This section assumes you: 

    1. have the API installed, 
    2. have imported it using `import isx` 
    3. have a ISXD CellSet accessible on your local file system at `cellset.isxd`


Once a cell set is opened using:


```python
cell_set = isx.CellSet.read("cellset.isxd")
```
we can read the name of any cell using:

```python
cell_name = cell_set.get_cell_name(0)
```
