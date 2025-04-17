# Team Exercise #2

## Review Process

### Issues Identified

Issue 1: No User Input
- The original code uses a hardcoded search term "general artificial intelligence"
- Users cannot specify their own search terms

Issue 2: No Dedicated Output Directory
- Files are saved directly to the current directory
- No organization of downloaded files

Issue 3: Poor Error Handling
- The code lacks proper error handling
- Exceptions could cause the program to crash

Issue 4: Multiprocessing Implementation Issues
- The process function doesn't have access to the output directory
- This could cause issues when trying to save files in the correct location

### Tasks Created

1. Implement user input functionality with validation
2. Create a dedicated "wiki_dl" directory for output files
3. Add proper error handling throughout the code
4. Fix the multiprocessing implementation to handle output directory
5. Add comprehensive documentation and comments
6. Create a main function to organize execution flow
7. Improve file handling with proper encoding

### Description of Issues and Solutions

Issue 1: No User Input
- Solution: Added a `get_search_term()` function that prompts the user for input
- Implemented validation to ensure the term is at least 4 characters
- If the input is too short, it defaults to "generative artificial intelligence"

Issue 2: No Dedicated Output Directory
- Solution: Created a `create_output_directory()` function that creates a "wiki_dl" directory
- Updated all file paths to save files in this directory
- This keeps the downloaded files organized and separate from other files

Issue 3: Poor Error Handling
- Solution: Added try-except blocks throughout the code
- Added error reporting to help identify issues
- Wrapped the main execution in a try-except block to prevent crashes

Issue 4: Multiprocessing Implementation Issues
- Solution: Modified the `dl_and_save_process` function to accept both the item and output directory
- Created a list of tuples to pass both parameters to the process function
- This ensures that processes have access to the correct output directory

### New Functionality Added

1. User Input:
   - Users can now input their own search term
   - If the term is less than 4 characters, it defaults to "generative artificial intelligence"

2. Dedicated Output Directory:
   - A new directory named "wiki_dl" is created to store the .txt files
   - All downloaded files are saved to this directory

3. Improved Structure:
   - Added a main function to organize the execution flow
   - Added proper documentation and type hints
   - Improved error handling and reporting
