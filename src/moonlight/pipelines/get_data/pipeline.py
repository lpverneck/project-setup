"""
This is a boilerplate pipeline 'get_data'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import generate_report, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["example_data", "parameters"],
                outputs=["X_train", "X_test"],
                name="split_data",
                namespace="Data Preparation",
            ),
            node(
                func=generate_report,
                inputs=["X_train", "X_test"],
                outputs=None,
                name="generate_report",
                namespace="Data Preparation",
            ),
        ]
    )
