#!/usr/bin/env python3
"""
Team Exercise #2: Wikipedia Reference Downloader

This script downloads references for related pages to a specified topic using
the Wikipedia API. It implements sequential, threaded, and multiprocessing approaches.
"""

import os
import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List, Any


def create_output_directory(directory_name: str = "wiki_dl") -> str:
    """
    Create a directory to store downloaded Wikipedia references.
    
    Args:
        directory_name: Name of the directory to create
        
    Returns:
        Path to the created directory
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name


def get_search_term() -> str:
    """
    Get search term from user input.
    
    Returns:
        Valid search term (at least 4 characters)
    """
    default_term = "generative artificial intelligence"
    
    user_input = input("Enter a search term (min 4 characters): ").strip()
    
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
    if isinstance(obj, list):
        return '\n'.join(obj)
    elif isinstance(obj, (str, int, float)):
        return str(obj)
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
    print('\nSequential function:')
    t_start = time.perf_counter()
    
    results = wikipedia.search(search_term)
    
    def dl_and_save(item):
        try:
            page = wikipedia.page(item, auto_suggest=False)
            title = page.title
            references = convert_to_str(page.references)
            out_filename = os.path.join(output_dir, f"{title}.txt")
            print(f'Writing to {out_filename}')
            with open(out_filename, 'w', encoding='utf-8') as fileobj:
                fileobj.write(references)
        except Exception as e:
            print(f"Error processing {item}: {e}")
    
    for item in results:
        dl_and_save(item)
    
    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'Code executed in {t_lapse:.2f} seconds')


def concurrent_threads(search_term: str, output_dir: str) -> None:
    """
    Download Wikipedia references using multiple threads.
    
    Args:
        search_term: Term to search for on Wikipedia
        output_dir: Directory to save the references
    """
    print('\nThread pool function:')
    t_start = time.perf_counter()
    
    results = wikipedia.search(search_term)
    
    def dl_and_save_thread(item):
        try:
            page = wikipedia.page(item, auto_suggest=False)
            title = page.title
            references = convert_to_str(page.references)
            out_filename = os.path.join(output_dir, f"{title}.txt")
            print(f'Writing to {out_filename}')
            with open(out_filename, 'w', encoding='utf-8') as fileobj:
                fileobj.write(references)
        except Exception as e:
            print(f"Error processing {item}: {e}")
    
    with ThreadPoolExecutor() as executor:
        executor.map(dl_and_save_thread, results)
    
    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'Code executed in {t_lapse:.2f} seconds')


# This function needs to be at module level for ProcessPoolExecutor
def dl_and_save_process(item_and_dir):
    """
    Helper function for multiprocessing execution.
    
    Args:
        item_and_dir: Tuple containing (item, output_directory)
    """
    item, output_dir = item_and_dir
    try:
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        out_filename = os.path.join(output_dir, f"{title}.txt")
        print(f'Writing to {out_filename}')
        with open(out_filename, 'w', encoding='utf-8') as fileobj:
            fileobj.write(references)
    except Exception as e:
        print(f"Error processing {item}: {e}")


def concurrent_process(search_term: str, output_dir: str) -> None:
    """
    Download Wikipedia references using multiple processes.
    
    Args:
        search_term: Term to search for on Wikipedia
        output_dir: Directory to save the references
    """
    print('\nProcess pool function:')
    t_start = time.perf_counter()
    
    results = wikipedia.search(search_term)
    
    # Create a list of tuples (item, output_dir) to pass to the process function
    items_with_dir = [(item, output_dir) for item in results]
    
    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save_process, items_with_dir)
    
    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'Code executed in {t_lapse:.2f} seconds')


def main():
    """Main function to run the Wikipedia reference downloader."""
    # Create output directory
    output_dir = create_output_directory("wiki_dl")
    
    # Get search term from user
    search_term = get_search_term()
    print(f"Searching for: '{search_term}'")
    
    try:
        # Run all three implementations
        wiki_sequentially(search_term, output_dir)
        concurrent_threads(search_term, output_dir)
        concurrent_process(search_term, output_dir)
        
        print("\nAll downloads completed successfully!")
        print(f"Files saved to: {os.path.abspath(output_dir)}")
        
    except Exception as e:
        print(f"Error in main execution: {e}")


if __name__ == "__main__":
    main()
