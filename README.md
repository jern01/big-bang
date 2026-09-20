# Big Bang

A script that iterates through 1 to 100 and replaces:

- Numbers divisible by 3 with "Big"
- Numbers divisible by 5 with "Bang"
- Numbers divisible by both 3 and 5 with "Big Bang"

## Requirements

- Python 3 (no external libraries required - only standard library `json`)

## How to run

1. CLone the repository:

```bash
git clone https://github.com/jern01/big-bang.git
```

2. Navigate to the project directory:

```bash
cd big-bang
```

3. Run the script:

```bash
python big_bang.py
```

4. The output will be printed to the console and saved to a file named `output.json` in the project directory.

## Expected output

`output.json` contains 100 entries:

```json
[
  "1",
  "2",
  "Big",
  "4",
  "Bang",
  "Big",
  "7",
  "8",
  "Big",
  "Bang",
  "11",
  "Big",
  "13",
  "14",
  "Big Bang",
  "...and so on until 100"
]
```