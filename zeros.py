import argparse
import os

from helpers.models import JohnnyDecimalArea, JohnnyDecimalCategory, JohnnyDecimalID
from helpers.paths import get_areas, get_categories, get_ids


def main():
    parser = argparse.ArgumentParser(
        prog="zeros.py",
        description="Add zero files and folders to a Johnny Decimal system",
    )
    parser.add_argument("root")
    args = parser.parse_args()

    areas = get_areas(args.root)
    for area in areas:
        if area.min == "00":
            continue
        create_area_zero_category(area, rename=True)
        for category in get_categories(area.entry.path):
            create_category_zero_ids(category, rename=True)


def create_category_zero_ids(
    category: JohnnyDecimalCategory, rename: bool = False
) -> None:
    ZERO_IDS = {
        f"{category.number}.00": f"{category.number}.00 {category.name} Index.md",
        f"{category.number}.01": f"{category.number}.01 {category.name} Inbox",
        f"{category.number}.02": f"{category.number}.02 {category.name} Work in Progress",
        f"{category.number}.03": f"{category.number}.03 {category.name} TODOs.md",
        f"{category.number}.04": f"{category.number}.04 {category.name} Links.md",
        f"{category.number}.05": f"{category.number}.05 {category.name} Templates",
        f"{category.number}.08": f"{category.number}.08 {category.name} Someday",
        f"{category.number}.09": f"{category.number}.09 {category.name} Archive",
    }

    current_ids = {id.id: id for id in get_ids(category.entry.path)}
    for zero_id in ZERO_IDS.keys():
        zero_id_path = os.path.join(category.entry.path, ZERO_IDS[zero_id])
        found_id = current_ids.get(zero_id)
        if not found_id:
            create_id(zero_id_path)
        elif found_id.entry.path != zero_id_path and rename:
            os.rename(found_id.entry.path, zero_id_path)


def create_area_zero_category(area: JohnnyDecimalArea, rename=False) -> None:
    zero_category_path = os.path.join(
        area.entry.path, f"{area.min} {area.name} Management"
    )

    zero_category = None
    for category in get_categories(area.entry.path):
        if category.number == area.min:
            zero_category = category

    if not zero_category:
        os.mkdir(zero_category_path)
    elif rename:
        os.rename(zero_category.entry.path, zero_category_path)


def create_id(path: str) -> JohnnyDecimalID:
    if not path.endswith(".md"):
        os.mkdir(path)
    else:
        with open(path, "a") as _:
            pass


if __name__ == "__main__":
    main()
