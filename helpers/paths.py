import os
import re

from helpers.models import JohnnyDecimalArea, JohnnyDecimalCategory, JohnnyDecimalID


def get_ids(path: str) -> list[JohnnyDecimalID]:
    return [
        JohnnyDecimalID(entry) for entry in get_matching_entries(path, r"\d{2}.\d{2}")
    ]


def get_categories(path: str) -> list[JohnnyDecimalCategory]:
    return [
        JohnnyDecimalCategory(entry)
        for entry in get_matching_directories(path, r"\d{2} ")
    ]


def get_areas(path: str) -> list[JohnnyDecimalArea]:
    return [
        JohnnyDecimalArea(entry)
        for entry in get_matching_directories(path, r"\d{2}-\d{2} ")
    ]


def get_matching_directories(path: str, pattern: str) -> list[os.DirEntry]:
    return [entry for entry in get_matching_entries(path, pattern) if entry.is_dir()]


def get_matching_entries(path: str, pattern: str) -> list[os.DirEntry]:
    regex = re.compile(pattern)
    return [entry for entry in os.scandir(path) if regex.search(entry.name)]
