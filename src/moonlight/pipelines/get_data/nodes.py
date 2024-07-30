import os
from pathlib import Path
from typing import Any, Dict, Tuple

import pandas as pd
from dotenv import load_dotenv

_ = load_dotenv(Path.cwd() / "conf" / "local" / ".env")


def split_data(
    data: pd.DataFrame, parameters: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    X_train = data.sample(parameters["train_frac"])
    X_test = data.sample(parameters["test_frac"])
    return X_train, X_test


def generate_report(X_train: pd.DataFrame, X_test: pd.DataFrame) -> None:
    print(X_train.to_string())
    print("-" * 50)
    print(X_test.to_string())
    print("-" * 50)
    print(f"Environment variable: {os.getenv("TEST_VAR")}")
