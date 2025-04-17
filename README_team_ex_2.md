# Team Exercise #2: Wikipedia Reference Downloader

## Overview
This project refactors a Wikipedia reference downloader that implements three different approaches:
1. Sequential execution
2. Concurrent execution with threads
3. Concurrent execution with processes

## Improvements Made

### Issue 1: User Input
- Added functionality to get a search term from the user
- Implemented validation to ensure the term is at least 4 characters
- Default to "generative artificial intelligence" if the input is too short

### Issue 2: File Organization
- Created a "wiki_dl" directory to store all downloaded files
- Updated all file paths to save files in this directory

### Issue 3: Code Structure
- Added proper type hints for better code readability
- Added comprehensive docstrings for all functions
- Improved error handling throughout the code
- Created a proper `main()` function to organize the execution flow

### Issue 4: Multiprocessing Fix
- Modified the `dl_and_save_process` function to accept both the item and output directory
- Created a list of tuples to pass both parameters to the process function

### Other Improvements
- Added proper UTF-8 encoding for file operations
- Improved console output with more informative messages
- Made the code more modular and easier to extend
- Added better error handling to prevent crashes

## How to Run
1. Make sure you have the Wikipedia package installed:
   ```
   pip install wikipedia
   ```
2. Run the script:
   ```
   python team_ex_2.py
   ```
3. Enter a search term when prompted (must be at least 4 characters)
4. The script will download references for related topics using all three methods
5. Files will be saved in the "wiki_dl" directory

## Performance Comparison
The script will display the execution time for each method, allowing you to compare their performance.
```

### Step 5: Install the required package

Before running the code, make sure you have the Wikipedia package installed. Open a terminal in VS Code (Terminal > New Terminal) and run:

```bash
pip install wikipedia
```

### Step 6: Commit and push your changes

In VS Code, you can use the Source Control tab (Ctrl+Shift+G) to commit and push your changes:

1. Stage the changes by clicking the + next to each file
2. Enter a commit message like "Add refactored team_ex_2.py with improvements and documentation"
3. Click the checkmark to commit
4. Click the "..." menu and select "Push" to push your changes to GitHub

Alternatively, you can use the terminal in VS Code:

```bash
git add team_ex_2.py README_team_ex_2.md
```

```bash
git commit -m "Add refactored team_ex_2.py with improvements and documentation"
```

```bash
git push
