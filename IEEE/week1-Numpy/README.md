# NumPy Practice Notebook

A collection of hands-on NumPy exercises covering array creation, dimensions,
shape vs. size, reshaping, transposing, unique values, broadcasting, and
slicing.

## Contents

`Numpy.ipynb` walks through the following exercises:

1. **1D array creation** — build an array of numbers 1–10 using `np.array()` / `np.arange()`.
2. **2D array creation** — construct a 3×4 array from nested lists.
3. **Array of zeros** — create a `(2, 3)` array of zeros with `np.zeros()`.
4. **Odd numbers 1–1000** — generate a sequence with `np.arange()`.
5. **`ndim`** — demonstrate how `ndim` reports the number of dimensions of an array.
6. **`shape` vs. `size`** — explain and show the difference: `shape` returns a tuple describing rows/columns, `size` returns the total element count.
7. **Flattening** — collapse a multi-column array into 1D with `.flatten()`.
8. **Transposing** — swap axes of a nested array using `np.transpose()`.
9. **Unique values** — count and print the distinct entries in an array of country names.
10. **Shapes & broadcasting** — inspect the shapes of `A[1]` and `B`, and explain why `A[1] * B` fails under NumPy's broadcasting rules.
11. **Slicing challenge** — embed a 3×3 array of ones into the center of a 5×5 array of nines using slice assignment (no loops).
12. **Dimensions deep-dive** — interpret `(3,)` vs. `(3, 2)` vs. `(3, 1)` shapes and what each axis represents.

## Requirements

- Python 3
- [NumPy](https://numpy.org/)
- Jupyter Notebook or JupyterLab

## Setup

```bash
pip install numpy jupyter
jupyter notebook Numpy.ipynb
```

## Topics Covered

- Array creation (`np.array`, `np.arange`, `np.zeros`, `np.full`, `np.ones`)
- Array attributes (`ndim`, `shape`, `size`)
- Reshaping and flattening (`.flatten()`, `np.transpose()`)
- Finding unique values (`np.unique`)
- Broadcasting rules
- Slicing and in-place assignment
