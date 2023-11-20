#!/usr/bin/python3
"""object from JSON file"""
import json


def load_from_json_file(filename):
    """creating object"""

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
