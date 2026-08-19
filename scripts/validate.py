#!/usr/bin/env python3
"""Validate the Awesome File Converters dataset using the standard library."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "converters.json"

REQUIRED = {
    "name", "url", "documentation_url", "types", "categories", "inputs", "outputs", "platforms",
    "free", "account_required", "local_processing", "open_source", "batch",
    "watermark", "notes", "last_verified",
}
TRISTATE = {"yes", "no", "mixed", "unknown"}
FREE_VALUES = {"yes", "limited", "no", "unknown"}
ACCOUNT_VALUES = {"yes", "no", "optional", "unknown"}
ALLOWED_TYPES = {"api", "cli", "desktop", "library", "mobile", "self-hosted", "web-app"}
ALLOWED_CATEGORIES = {"archive", "audio", "data", "document", "ebook", "image", "presentation", "video"}


def main() -> int:
    errors: list[str] = []
    try:
        payload = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Could not read {DATA_FILE}: {exc}", file=sys.stderr)
        return 1

    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    converters = payload.get("converters")
    if not isinstance(converters, list):
        errors.append("converters must be an array")
        converters = []

    names: set[str] = set()
    urls: set[str] = set()
    today = date.today()

    for index, item in enumerate(converters):
        label = f"converters[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = REQUIRED - item.keys()
        extra = item.keys() - REQUIRED
        if missing:
            errors.append(f"{label} missing: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{label} has unknown fields: {', '.join(sorted(extra))}")
        if missing:
            continue

        name = item["name"].strip() if isinstance(item["name"], str) else ""
        normalized_name = name.casefold()
        if not name:
            errors.append(f"{label}.name must be a non-empty string")
        elif normalized_name in names:
            errors.append(f"{label}.name duplicates {name!r}")
        names.add(normalized_name)

        url = item["url"]
        parsed = urlparse(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{label}.url must be a valid HTTPS URL")
        elif url in urls:
            errors.append(f"{label}.url duplicates {url!r}")
        urls.add(url)

        documentation_url = item["documentation_url"]
        documentation_parsed = urlparse(documentation_url) if isinstance(documentation_url, str) else None
        if not documentation_parsed or documentation_parsed.scheme != "https" or not documentation_parsed.netloc:
            errors.append(f"{label}.documentation_url must be a valid HTTPS URL")

        for field in ("types", "categories", "inputs", "outputs", "platforms"):
            value = item[field]
            if not isinstance(value, list) or not value or not all(isinstance(v, str) and v for v in value):
                errors.append(f"{label}.{field} must be a non-empty string array")
            elif value != sorted(set(value)):
                errors.append(f"{label}.{field} must be sorted with no duplicates")

        if isinstance(item["types"], list) and not set(item["types"]) <= ALLOWED_TYPES:
            errors.append(f"{label}.types contains an unsupported value")
        if isinstance(item["categories"], list) and not set(item["categories"]) <= ALLOWED_CATEGORIES:
            errors.append(f"{label}.categories contains an unsupported value")
        if item["free"] not in FREE_VALUES:
            errors.append(f"{label}.free must be one of {sorted(FREE_VALUES)}")
        if item["account_required"] not in ACCOUNT_VALUES:
            errors.append(f"{label}.account_required must be one of {sorted(ACCOUNT_VALUES)}")
        for field in ("local_processing", "open_source", "batch", "watermark"):
            if item[field] not in TRISTATE:
                errors.append(f"{label}.{field} must be one of {sorted(TRISTATE)}")
        try:
            verified = date.fromisoformat(item["last_verified"])
            if verified > today:
                errors.append(f"{label}.last_verified cannot be in the future")
        except (TypeError, ValueError):
            errors.append(f"{label}.last_verified must use YYYY-MM-DD")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(converters)} converters in {DATA_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
