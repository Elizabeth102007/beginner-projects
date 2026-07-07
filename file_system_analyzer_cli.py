import argparse
from pathlib import Path
from collections import defaultdict
import sys
from datetime import datetime
import csv
def parsed_args():
    parser = argparse.ArgumentParser(description="Analyze files in a folder")
    parser.add_argument("folder")
    args = parser.parse_args()
    return args.folder

def scan_folder(folder_path):
    path = Path(folder_path)
    if not path.exists():
        sys.exit("Error: This folder doesn't exist")
    if not path.is_dir():
        sys.exit("Error: Not a folder")
    file_list = []
    for item in path.iterdir():
        if item.is_file():
            file_list.append(item)
    return file_list
        
def group_by_extensions(files):
    grouped = {}
    for file in files:
       extension = file.suffix
       if extension == "":
           extension = "no extension"
       if extension in grouped:
          grouped[extension].append(file)
       else:
          grouped[extension] = [file]
    return grouped

def format_size(bytes):
    if bytes <= 1024:
        return f"{bytes} Bytes"
    
    elif bytes <= 1024 * 1024:
        result = bytes/1024
        return f"{result:.2f}KB"
    
    elif bytes <= 1024*1024*1024:
        result = bytes/(1024*1024)
        return f"{result:.2f}MB"
    
    else:
        result = bytes/(1024*1024*1024)
        return f"{result:.2f}GB"

def get_file_age_days(file_path):
    modified_timestamp = file_path.stat().st_mtime
    modified_date = datetime.fromtimestamp(modified_timestamp)
    today = datetime.today()
    age = (today - modified_date).days
    return age

def find_old_files(files, days=30):
    old_files = []
    for file in files:
        age = get_file_age_days(file)
        if age >=days:
            old_files.append(file)
    return old_files


def find_duplicates(files):
    duplicates = defaultdict(list)

    for file in files:
        key = (
            file.name,
            file.stat().st_size
        )

        duplicates[key].append(file)

    results = []

    for group in duplicates.values():
        if len(group) > 1:
            results.append(tuple(group))

    return results


def print_report(extension_groups, old_files, duplicates):
    
    print("=== Extensions ===")
    for ext, file_list in extension_groups.items():
        total_size = sum(f.stat().st_size for f in file_list)
        print(f"{ext}: {len(file_list)} file(s) | {format_size(total_size)}")

    print("\n=== Old Files (30+ days) ===")
    if old_files:
        for f in old_files:
            print(f"{f.name} — {get_file_age_days(f)} days old")
    else:
        print("No old files found.")
    
    print("\n=== Duplicates ===")
    if duplicates:
        for group in duplicates:
            print(f"Duplicate: {group[0].name}")
            for file in group:
                print(f"  {file}")
    else:
        print("No duplicates found.")

def export_csv(path, extension_groups, old_files, duplicates):
    csv_file = path / "file_system_report.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Extension", "File Count", "Total Size"])
        for ext, file_list in extension_groups.items():
            total_size = sum(f.stat().st_size for f in file_list)
            writer.writerow([ext, len(file_list), format_size(total_size)])
        writer.writerow([])
        writer.writerow(["Filename","Last Modified", "Age (days)"])
        for f in old_files:
            writer.writerow([f.name, datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d"), get_file_age_days(f)])
        writer.writerow([])
        writer.writerow(["Filename", "Size", "Paths"])
        for group in duplicates:
            for duplicate_file in group:
                total_size = sum(f.stat().st_size for f in file_list)
                writer.writerow([group[0].name, format_size(duplicate_file.stat().st_size), duplicate_file])
            writer.writerow([])

def main():
    folder_path = parsed_args()
    path = Path(folder_path)
    files = scan_folder(path)
    extension_groups = group_by_extensions(files)
    old_files = find_old_files(files)
    duplicates = find_duplicates(files)
    print_report(extension_groups, old_files,duplicates)
    export_csv(path, extension_groups, old_files, duplicates)
    print("Report exported to file_system_report.csv")

if __name__ == "__main__":
    main()

                
                



            





    


