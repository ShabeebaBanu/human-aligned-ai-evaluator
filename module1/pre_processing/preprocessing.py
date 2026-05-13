"""Text and dataset preprocessing helpers for the synthetic answer dataset."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pandas as pd


ANSWER_COLUMNS = ( "question" ,"synthetic_answer",  "answer", "evaluation_criteria")


def clean_text(value: object) -> str:
    """Clean one answer string for later NLP processing."""
    if pd.isna(value):
        return ""

    text = unicodedata.normalize("NFKC", str(value))
    text = text.lower()
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"\[\[|\]\]", " ", text)
    text = re.sub(r"[“”]", '"', text)
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"[^a-z0-9.%$'\"\-\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names to lowercase snake_case."""
    renamed = {
        column: (
            str(column)
            .strip()
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
        )
        for column in dataframe.columns
    }
    renamed = {
        source: re.sub(r"_+", "_", target).strip("_")
        for source, target in renamed.items()
    }
    return dataframe.rename(columns=renamed)


def preprocess_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Return a preprocessed copy of the dataset."""
    processed = normalize_column_names(dataframe).copy()

    for column in ANSWER_COLUMNS:
        if column in processed.columns:
            processed[f"{column}_clean"] = processed[column].apply(clean_text)

    if "question" in processed.columns:
        processed["question_clean"] = processed["question"].apply(clean_text)

    if "chapter" in processed.columns:
        processed["chapter"] = processed["chapter"].astype(str).str.strip()

    if "difficulty" in processed.columns:
        processed["difficulty"] = processed["difficulty"].astype(str).str.strip().str.title()

    return processed


def build_preprocessing_summary(dataframe: pd.DataFrame) -> dict[str, object]:
    """Create a small summary for group review."""
    summary: dict[str, object] = {
        "rows": int(len(dataframe)),
        "columns": list(dataframe.columns),
        "missing_values": dataframe.isna().sum().to_dict(),
    }

    if "question_id" in dataframe.columns:
        summary["question_count"] = int(dataframe["question_id"].nunique())

    if "answer_id" in dataframe.columns:
        summary["answer_count"] = int(dataframe["answer_id"].nunique())

    return summary

