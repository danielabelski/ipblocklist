import os
import json
import glob
import shutil
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def extract_ipv4_covered(data: dict) -> int | None:
    """Extract total_ipv4_addresses_covered from both inbound and outbound."""
    try:
        inbound = data["inbound"]["stats"]["top_metrics"]["total_ipv4_addresses_covered"]
        outbound = data["outbound"]["stats"]["top_metrics"]["total_ipv4_addresses_covered"]
        return inbound + outbound
    except (KeyError, TypeError):
        return None


def generate_history():
    """
    Parses stats json files to generate a history of total_ipv4_addresses_covered
    for the last 3 months.
    - Scans both 'stats/' and 'stats/archived/' to build the full history.
    - Moves processed files from 'stats/' to 'stats/archived/'.
    - Only keeps one entry (the latest) per day in the output JSON.
    """
    stats_dir = os.path.join(BASE_DIR, 'stats')
    archive_dir = os.path.join(stats_dir, 'archived')
    output_file = os.path.join(stats_dir, 'history.json')
    ignored_files = {'latest.json', 'history.json'}

    os.makedirs(archive_dir, exist_ok=True)

    cutoff_date = datetime.now() - timedelta(days=90)

    daily_records = {}
    files_to_archive = []

    root_files = glob.glob(os.path.join(stats_dir, '*.json'))
    archived_files = glob.glob(os.path.join(archive_dir, '*.json'))
    all_files = sorted(root_files + archived_files)

    print(f"Scanning {len(all_files)} files (New: {len(root_files)}, Archived: {len(archived_files)})...")

    for filepath in all_files:
        filename = os.path.basename(filepath)

        if filename in ignored_files:
            continue

        is_in_root = os.path.abspath(os.path.dirname(filepath)) == os.path.abspath(stats_dir)
        if is_in_root and filename.startswith("stats_"):
            files_to_archive.append(filepath)

        try:
            clean_name = filename.replace('stats_', '').replace('.json', '')
            try:
                file_date = datetime.strptime(clean_name, '%Y%m%d_%H%M%S')
            except ValueError:
                continue

            if file_date < cutoff_date:
                continue

            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            ipv4_count = extract_ipv4_covered(data)

            if ipv4_count is not None:
                day_key = file_date.strftime('%Y-%m-%d')
                daily_records[day_key] = {
                    'date': file_date.isoformat(),
                    'timestamp': file_date.timestamp(),
                    'total_ipv4_addresses_covered': ipv4_count
                }
            else:
                print(f"Warning: metric not found in {filename}")

        except json.JSONDecodeError:
            print(f"Skipping {filename} (invalid JSON)")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    history_data = sorted(daily_records.values(), key=lambda x: x['date'])

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(history_data, f, indent=4)

    print(f"\nSuccess! Generated '{output_file}' with {len(history_data)} unique daily records.")

    if files_to_archive:
        print(f"Archiving {len(files_to_archive)} files to '{archive_dir}'...")
        for filepath in files_to_archive:
            try:
                shutil.move(filepath, archive_dir)
            except Exception as e:
                print(f"Error moving {os.path.basename(filepath)}: {e}")
        print("Archiving complete.")
    else:
        print("No new files to archive.")


if __name__ == "__main__":
    if not os.path.exists(os.path.join(BASE_DIR, 'stats')):
        print("Error: 'stats' directory not found.")
    else:
        generate_history()
