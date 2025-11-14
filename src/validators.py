#!/usr/bin/env python3
"""
Dataset Validator — Rahul Personal AI
Checks dataset structure, JSON validity, required keys, and empty or invalid files.
"""

import json, sys, os
from pathlib import Path
from collections import Counter

ROOT = Path(os.getenv("DATA_DIR", "data"))

EXPECTED_JSONS = {
    "profile.json": ["basic_info", "education_info", "professional_info", "skills_summary", "personality_summary", "meta_data"],
    "education.json": ["current_degree", "subjects_and_courses"],
    "skills.json": ["languages", "frontend", "backend"],
    "certifications.json": None,
    "awards.json": None,
    "rankings.json": None,
    "project_summary.json": None,
    "qna_dataset.json": None
}

TEXT_EXTS = {".md", ".txt", ".text"}
JSON_EXTS = {".json"}

errors, warnings = [], []

def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"Encoding error: {path}")
        return None

def check_core_json(filename, required_keys):
    p = ROOT/filename
    if not p.exists():
        warnings.append(f"Missing expected file: {filename}")
        return
    s = read_text(p)
    if s is None:
        return
    try:
        j = json.loads(s)
    except Exception as e:
        errors.append(f"Invalid JSON in {filename}: {e}")
        return
    if required_keys:
        for k in required_keys:
            if k not in j:
                errors.append(f"Missing key '{k}' in {filename}")

def scan_files():
    all_paths = [p for p in ROOT.rglob("*") if p.is_file()]
    names = [p.name for p in all_paths]
    dup = [n for n,c in Counter(names).items() if c>1]
    if dup:
        errors.append(f"Duplicate filenames found: {dup}")

    for p in all_paths:
        if p.suffix.lower() in JSON_EXTS:
            try:
                json.loads(read_text(p))
            except Exception as e:
                errors.append(f"Invalid JSON in {p.relative_to(ROOT)}: {e}")
        elif p.suffix.lower() in TEXT_EXTS:
            txt = read_text(p)
            if txt is not None and len(txt.strip())==0:
                warnings.append(f"Empty file: {p.relative_to(ROOT)}")

def main():
    print(f"Validating dataset in: {ROOT.resolve()}")
    for fname, keys in EXPECTED_JSONS.items():
        check_core_json(fname, keys)
    scan_files()

    if errors:
        print("\n❌ ERRORS FOUND:")
        for e in errors: print(" -", e)
    else:
        print("\n✅ No critical errors found.")

    if warnings:
        print("\n⚠️ WARNINGS:")
        for w in warnings: print(" -", w)

    print("\nSummary:")
    print(f" Total files checked: {sum(1 for _ in ROOT.rglob('*') if _.is_file())}")
    print(f" Errors: {len(errors)} | Warnings: {len(warnings)}")

    if errors: sys.exit(2)
    elif warnings: sys.exit(1)
    else: sys.exit(0)

if __name__ == "__main__":
    main()
