#!/usr/bin/env python3
"""
Team Exercise #2: Wikipedia Reference Downloader

This script downloads references for related pages to a specified topic using
the Wikipedia API. It implements sequential, threaded, and multiprocessing approaches.
"""

# Standard library imports
import os      # For file and directory operations
import time    # For performance timing
# Third-party imports
import wikipedia  # For accessing Wikipedia content
# Concurrent execution imports
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# Type hinting for better code readability and IDE support
from typing import List, Any


def create_output_directory(directory_name: str = "wiki_dl") -> str:
    """
    Create a directory to store downloaded Wikipedia references.
    
    Args:
        directory_name: Name of the directory to create
        
    Returns:
        Path to the created directory
    """
    # IMPROVEMENT: Create a dedicated directory for output files
    # Check if directory exists, create it if it doesn't
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name


def get_search_term() -> str:
    """
    Get search term from user input.
    
    Returns:
        Valid search term (at least 4 characters)
    """
    # IMPROVEMENT: Allow user to input their own search term
    default_term = "generative artificial intelligence"
    
    # Prompt user for input and remove leading/trailing whitespace
    user_input = input("Enter a search term (min 4 characters): ").strip()
    
    # IMPROVEMENT: Validate input length and use default if too short
    if len(user_input) < 4:
        print(f"Search term too short. Using default: '{default_term}'")
        return default_term
    
    return user_input


def convert_to_str(obj: Any) -> str:
    """
    Convert an object to string representation.
    
    Args:
        obj: Object to convert
        
    Returns:
        String representation of the object
    """
    # IMPROVEMENT: Enhanced type checking with isinstance() instead of type()
    # For lists, join elements with newlines
    if isinstance(obj, list):
        return '\n'.join(obj)
    # For basic types, convert directly to string
    elif isinstance(obj, (str, int, float)):
        return str(obj)
    # IMPROVEMENT: Added fallback for other types
    else:
        try:
            return str(obj)
        except Exception as e:
            return f"Error converting to string: {e}"


def wiki_sequentially(search_term: str, output_dir: str) -> None:
    """
    Download Wikipedia references sequentially.
    
    Args:
        search_term: Term to search for on Wikipedia
        output_dir: Directory to save the references
    """
    # IMPROVEMENT: Added function parameters instead of hardcoded values
    print('\nSequential function:')
    # Start timing execution
    t_start = time.perf_counter()
    
    # Search Wikipedia for the given term
    results = wikipedia.search(search_term)
    
    # Define inner function to download and save references
    def dl_and_save(item):
        try:
            # IMPROVEMENT: Added error handling with try-except
            # Get Wikipedia page for the item
            page = wikipedia.page(item, auto_suggest=False)
            title = page.title
            # Convert references to string format
            references = convert_to_str(page.references)
            # IMPROVEMENT: Save files to the specified output directory
            out_filename = os.path.join(output_dir, f"{title}.txt")
            print(f'Writing to {out_filename}')
            # IMPROVEMENT: Added UTF-8 encoding for better text handling
            with open(out_filename, 'w', encoding='utf-8') as fileobj:
                fileobj.write(references)
        except Exception as e:
            # IMPROVEMENT: Added error reporting
            print(f"Error processing {item}: {e}")
    
    # Process each search result sequentially
    for item in results:
        dl_and_save(item)
    
    # Calculate and display execution time
    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    # IMPROVEMENT: Formatted time output to 2 decimal places
    print(f'Code executed in {t_lapse:.2f} seconds')


def concurrent_threads(search_term: str, output_dir: str) -> None:
    """
    Download Wikipedia references using multiple threads.
    
    Args:
        search_term: Term to search for on Wikipedia
        output_dir: Directory to save the references
    """
    # IMPROVEMENT: Added function parameters instead of hardcoded values
    print('\nThread pool function:')
    # Start timing execution
    t_start = time.perf_counter()
    
    # Search Wikipedia for the given term
    results = wikipedia.search(search_term)
    
    # Define inner function for thread execution
    def dl_and_save_thread(item):
        try:
            # IMPROVEMENT: Added error handling with try-except
            # Get Wikipedia page for the item
            page = wikipedia.page(item, auto_suggest=False)
            title = page.title
            # Convert references to string format
            references = convert_to_str(page.references)
            # IMPROVEMENT: Save files to the specified output directory
            out_filename = os.path.join(output_dir, f"{title}.txt")
            print(f'Writing to {out_filename}')
            # IMPROVEMENT: Added UTF-8 encoding for better text handling
            with open(out_filename, 'w', encoding='utf-8') as fileobj:
                fileobj.write(references)
        except Exception as e:
            # IMPROVEMENT: Added error reporting
            print(f"Error processing {item}: {e}")
    
    # Use ThreadPoolExecutor to process items concurrently
    with ThreadPoolExecutor() as executor:
        executor.map(dl_and_save_thread, results)
    
    # Calculate and display execution time
    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    # IMPROVEMENT: Formatted time output to 2 decimal places
    print(f'Code executed in {t_lapse:.2f} seconds')


# This function needs to be at module level for ProcessPoolExecutor
def dl_and_save_process(item_and_dir):
    """
    Helper function for multiprocessing execution.
    
    Args:
        item_and_dir: Tuple containing (item, output_directory)
    """
    # IMPROVEMENT: Modified to accept both item and output directory
    # Unpack the tuple to get item and output directory
    item, output_dir = item_and_dir
    try:
        # IMPROVEMENT: Added error handling with try-except
        # Get Wikipedia page for the item
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        # Convert references to string format
        references = convert_to_str(page.references)
        # IMPROVEMENT: Save files to the specified output directory
        out_filename = os.path.join(output_dir, f"{title}.txt")
        print(f'Writing to {out_filename}')
        # IMPROVEMENT: Added UTF-8 encoding for better text handling
        with open(out_filename, 'w', encoding='utf-8') as fileobj:
            fileobj.write(references)
    except Exception as e:
        # IMPROVEMENT: Added error reporting
        print(f"Error processing {item}: {e}")


def concurrent_process(search_term: str, output_dir: str) -> None:
    """
    Download Wikipedia references using multiple processes.
    
    Args:
        search_term: Term to search for on Wikipedia
        output_dir: Directory to save the references
    """
    # IMPROVEMENT: Added function parameters instead of hardcoded values
    print('\nProcess pool function:')
    # Start timing execution
    t_start = time.perf_counter()
    
    # Search Wikipedia for the given term
    results = wikipedia.search(search_term)
    
    # IMPROVEMENT: Create a list of tuples to pass both item and directory
    # This solves the issue of processes not sharing memory
    items_with_dir = [(item, output_dir) for item in results]
    
    # Use ProcessPoolExecutor to process items concurrently
    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save_process, items_with_dir)
    
    # Calculate and display execution time
    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    # IMPROVEMENT: Formatted time output to 2 decimal places
    print(f'Code executed in {t_lapse:.2f} seconds')


def main():
    """Main function to run the Wikipedia reference downloader."""
    # IMPROVEMENT: Added a main function to organize execution flow
    
    # Create output directory for storing files
    output_dir = create_output_directory("wiki_dl")
    
    # Get search term from user with validation
    search_term = get_search_term()
    print(f"Searching for: '{search_term}'")
    
    try:
        # IMPROVEMENT: Added error handling for the entire execution
        
        # Run all three implementations with the user's search term
        wiki_sequentially(search_term, output_dir)
        concurrent_threads(search_term, output_dir)
        concurrent_process(search_term, output_dir)
        
        # IMPROVEMENT: Added success message and file location information
        print("\nAll downloads completed successfully!")
        print(f"Files saved to: {os.path.abspath(output_dir)}")
        
    except Exception as e:
        # IMPROVEMENT: Added error reporting for the main execution
        print(f"Error in main execution: {e}")


# Standard Python idiom to check if the script is being run directly
if __name__ == "__main__":
    main()
