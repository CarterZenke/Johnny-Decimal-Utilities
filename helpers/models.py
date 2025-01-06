import os
import re


class JohnnyDecimalArea:
    def __init__(self, dir_entry: os.DirEntry):
        self.entry = dir_entry
        self._area_min, self._area_max, self._area_name = self._parse_jd_name(
            dir_entry.name
        )

    def _parse_jd_name(self, directory_name: str):
        pattern = r"^(\d{2})-(\d{2})\s+(.*)$"
        match = re.match(pattern, directory_name)
        if not match:
            return (None, None, None)

        area_min_str, area_max_str, area_name = match.groups()

        return (area_min_str, area_max_str, area_name)

    @property
    def min(self) -> str:
        return self._area_min

    @property
    def max(self) -> str:
        return self._area_max

    @property
    def name(self) -> str:
        return self._area_name


class JohnnyDecimalCategory:
    def __init__(self, dir_entry: os.DirEntry):
        self.entry = dir_entry
        self._category_number, self._category_name = self._parse_jd_name(dir_entry.name)

    def _parse_jd_name(self, directory_name: str):
        pattern = r"^(\d{2})\s+(.*)$"
        match = re.match(pattern, directory_name)
        if not match:
            return (None, None)

        category_number, category_name = match.groups()

        return (category_number, category_name)

    @property
    def number(self) -> str:
        return self._category_number

    @property
    def name(self) -> str:
        return self._category_name


class JohnnyDecimalID:
    def __init__(self, dir_entry: os.DirEntry):
        self.entry = dir_entry
        self._category, self._id, self._name = self._parse_jd_name(dir_entry.name)

    def _parse_jd_name(self, directory_name: str):
        pattern = r"^(?P<id>(?P<category>\d{2}).\d{2})\s+(?P<name>.*)$"
        match = re.match(pattern, directory_name)
        if not match:
            return (None, None, None)

        return (match.group("category"), match.group("id"), match.group("name"))

    @property
    def category(self) -> str:
        return self._category

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name
