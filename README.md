# 🧠 Pure Sudoku Solver (TXT Only)

This is a pure algorithmic Sudoku generator and solver project that works **exclusively with `.txt` files**. It supports standard Sudoku sizes: **4x4**, **9x9**, and **16x16**. The project focuses on improving core programming skills and logic implementation without relying on external interfaces.

---

## 📦 Project Structure

### ✅ 1. `generate_sudoku_txt.py`
Generates a valid Sudoku puzzle with a unique solution, removes a specified number of cells, and writes the result to a `.txt` file.

```bash
python generate_sudoku_txt.py
```

#### 🔧 Configuration (inside the file):
```python
size = 9           # Must be one of [4, 9, 16]
empty_cells = 40   # Number of cells to leave empty
```

---

### 📄 2. TXT File Format

Each line represents one row of the Sudoku board. Values are space-separated. Use a `.` (dot) for empty cells.

#### Example:
```
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
```

---

### 🔍 3. `preparation_txt.py`
Reads a `.txt` Sudoku puzzle, replaces empty cells (`.`) with `0`, and returns a `NumPy` array for the solver to use. Includes validation of board size and format.

---

### 🧠 4. `solver.py`
Efficiently solves Sudoku puzzles of size 4x4, 9x9, or 16x16 using **backtracking algorithm**. Designed for readability and performance.

---

### 🚀 5. `main.py`
Runs the full process: loads the `.txt` file, solves the Sudoku puzzle, and optionally prints or saves the solution.

---

## ⚠️ Limits
- Only supports Sudoku sizes **4x4**, **9x9**, and **16x16**.
- If any other size is used, the system will raise an error.
- TXT format only. CSV is not supported in this version.

---

## ✅ Features
- Pure algorithmic logic
- Easy to read and modify
- Fast solving via backtracking
- Fully TXT-based input and output
- Great for practice or integration into a bigger AI/ML project

---

## 🧪 Future Ideas
- Add `.csv` support
- Build GUI using Tkinter or PyQt
- Add puzzle difficulty rating
- Integrate with ML model for puzzle generation

---

## 👨‍💻 Author
Developed by a passionate algorithm enthusiast aiming for mastery in logic-based problem solving.

---