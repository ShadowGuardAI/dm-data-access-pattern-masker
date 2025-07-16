import argparse
import logging
import random
import pandas as pd
import os
from typing import List, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Sets up the argument parser for the command-line interface.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(description="Masks access patterns to data during masking operations by shuffling data.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_file", help="Path to the output CSV file.")
    parser.add_argument("--seed", type=int, default=None, help="Optional seed for the random number generator (for reproducibility).")
    parser.add_argument("--header", action="store_true", help="Specify if the input CSV file has a header row. Defaults to False.")  # Added header argument

    return parser

def shuffle_data(input_file: str, output_file: str, seed: Union[int, None] = None, header: bool = False) -> None:
    """
    Shuffles the rows of a CSV file to mask access patterns.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        seed (int, optional): Seed for the random number generator (for reproducibility). Defaults to None.
        header (bool, optional): Specifies whether the CSV file has a header. Defaults to False.
    Raises:
        FileNotFoundError: If the input file does not exist.
        Exception: If an error occurs during file processing.
    """
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        logging.info(f"Reading data from {input_file}...")
        try:
            df = pd.read_csv(input_file, header='infer' if header else None) # Explicitly set the header argument
        except Exception as e:
            raise Exception(f"Error reading CSV file: {e}")

        if seed is not None:
            random.seed(seed)
            logging.info(f"Using seed {seed} for shuffling.")

        logging.info("Shuffling data...")
        indices = list(df.index)
        random.shuffle(indices)
        shuffled_df = df.iloc[indices]

        logging.info(f"Writing shuffled data to {output_file}...")
        try:
            shuffled_df.to_csv(output_file, index=False, header=header) # Preserve header setting
        except Exception as e:
            raise Exception(f"Error writing to CSV file: {e}")

        logging.info("Data shuffling complete.")

    except FileNotFoundError as e:
        logging.error(f"File error: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def main():
    """
    Main function to execute the data access pattern masking tool.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    try:
        shuffle_data(args.input_file, args.output_file, args.seed, args.header)
    except Exception as e:
        logging.error(f"Failed to mask data access patterns: {e}")
        exit(1)  # Exit with a non-zero code to indicate failure

if __name__ == "__main__":
    # Usage Examples:
    # 1. Shuffle data in input.csv and save to output.csv:
    #    python main.py input.csv output.csv
    # 2. Shuffle with a specific seed:
    #    python main.py input.csv output.csv --seed 42
    # 3. Input file has a header row:
    #    python main.py input.csv output.csv --header
    # 4. Shuffle data with a specific seed and a header row:
    #    python main.py input.csv output.csv --seed 42 --header
    main()