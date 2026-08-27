# Python Piscine — Modules 00, 01, 02

Exercises from the 42 Python Piscine (Piscine Python for Data Science), covering the first three modules: basic Python, NumPy (arrays & images), and Pandas/Matplotlib (dataframes & graphs).

## 🗂️ Modules covered

```
Python/
├── 00/   # Module 00 - Starting: Python basics
├── 01/   # Module 01 - Arrays & images (NumPy)
├── 02/   # Module 02 - DataFrames & graphs (Pandas / Matplotlib)
└── README.md
```

---

## 📘 Module 00 — Starting

Introduction to the Python language: basic syntax, data structures, first scripts and functions.

| Exercise | File | Description |
|---|---|---|
| ex00 | `Hello.py` | Print greetings using different data structures (list, tuple, set, dict) |
| ex01 | `format_ft_time.py` | Format and display the current date/time in different ways |
| ex02 | `find_ft_type.py` | Function that prints an object's type and returns 42 |
| ex03 | `NULL_not_found.py` | Function that identifies all the different "null-like" types in Python |
| ex04 | `whatis.py` | Script that reads a CLI argument and prints whether it's odd or even |

> Console-only module — no screenshots needed here, just run the scripts and check the output.

---

## 📗 Module 01 — Arrays & Images (NumPy)

Introduction to `numpy`: manipulating multidimensional arrays and applying that to image processing with `PIL` / `matplotlib`.

| Exercise | File(s) | Description |
|---|---|---|
| ex00 | `give_bmi.py` | Compute BMI from height/weight lists using list comprehensions; filter values above a limit |
| ex01 | `array2D.py` | `slice_me`: validates and slices a 2D list (matrix), printing the shape before and after |
| ex02 | `load_image.py` | Loads an image with NumPy/PIL, prints its metadata (width, height, channels), zooms into the center, and displays it with axes |
| ex03 | `load_image.py`, `rotate.py` | Loads an image and manually transposes/rotates the pixel matrix, then displays the result |

<!-- 📷 Screenshot placeholder: original image loaded (ex02) -->
![Original image](images/01_ex02_original.png)

<!-- 📷 Screenshot placeholder: zoomed image with axis scales (ex02) -->
![Zoomed image](images/01_ex02_zoom.png)

<!-- 📷 Screenshot placeholder: transposed/rotated image (ex03) -->
![Transposed image](images/01_ex03_rotated.png)

---

## 📙 Module 02 — DataFrames & Graphs (Pandas / Matplotlib)

Introduction to `pandas` for loading and manipulating tabular data, and `matplotlib` for visualizing it, using a life-expectancy-by-country dataset.

| Exercise | File(s) | Description |
|---|---|---|
| ex00 | `load_csv.py` | Loads a CSV into a `DataFrame` with `pandas`, prints its shape, and handles file/parsing errors |
| ex01 | `aff_life.py` | Filters the dataset for a given country and plots its life expectancy evolution over the years |
| ex02 | `aff_pop.py` | *(in progress)* — combine population data with life expectancy on the same graph |
| ex03 | `projection_life.py` | *(in progress)* — relate data from two files to build a future projection |

<!-- 📷 Screenshot placeholder: DataFrame shape / head output (ex00) -->
![DataFrame preview](images/02_ex00_dataframe.png)

<!-- 📷 Screenshot placeholder: life expectancy plot for a country (ex01) -->
![Life expectancy plot](images/02_ex01_plot.png)

---

## ⚙️ Running the exercises

```bash
cd 00/exXX   # or 01/exXX, 02/exXX
python <script>.py
```

Some exercises expect arguments or a dataset/image file in the same folder (e.g. `life_expectancy_years.csv`, `animal.jpeg`) — check each exercise's own file for the expected input.

## ✍️ Author

Exercises by [RosseMry](https://github.com/RosseMry) — 42 School, Python Piscine.
