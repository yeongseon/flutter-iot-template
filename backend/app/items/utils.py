"""
/src/items/utils.py
Utility functions for the items application.
This module provides utility functions for the items application.
"""


def truncate_description(description: str, max_len: int = 100) -> str:
    return description if len(description) <= max_len else description[:max_len] + "..."
