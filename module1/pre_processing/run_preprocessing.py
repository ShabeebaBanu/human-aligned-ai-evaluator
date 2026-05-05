"""Command-line runner for checking dataset preprocessing."""

from __future__ import annotations

from pathlib import Path
from data.data_loader import load_raw_data, save_processed_data

from module1.pre_processing.preprocessing import (
    build_preprocessing_summary,
    preprocess_dataframe,
)


def main():
    raw_dataframe = load_raw_data()
    processed_dataframe = preprocess_dataframe(raw_dataframe)
    
    print("ready to preprocess...")
    save_processed_data(processed_dataframe)

    summary = build_preprocessing_summary(processed_dataframe)
    print(summary)


if __name__ == "__main__":
    main()
