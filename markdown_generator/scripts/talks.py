#!/usr/bin/env python
# coding: utf-8

# Talks markdown generator for academicpages (Jekyll GitHub Pages).
#
# Reads a talks table (TSV or CSV) and generates one Markdown file per row
# under the repository's _talks/ -- the Jekyll collection source files the site
# renders. This is the generator side of a source -> generated workflow: edit
# the table, re-run this script, then commit the regenerated Markdown. Do NOT
# hand-edit the generated Markdown files; they will be overwritten on the next
# run.
#
# Usage:
#   python3 scripts/talks.py data/<table>.tsv [output_dir]
#   (run from the markdown_generator/ folder; the input path is relative to
#   your current directory; output_dir defaults to <repo-root>/_talks)
#
# Input -- the first line is a header with these columns:
#   title, type, url_slug, venue, date, location, talk_url, description
# - `title`, `url_slug` and `date` are required; `date` must be YYYY-MM-DD.
# - `type` defaults to "Talk" when missing or too short.
# - `url_slug` becomes the file base name and the permalink tail:
#   YYYY-MM-DD-<url_slug>.md  ->  /talks/YYYY-MM-DD-<url_slug>
#
# Output: <repo-root>/_talks/YYYY-MM-DD-<url_slug>.md  (one per table row)
#
# Uses only the Python standard library (csv); no external dependencies.

import csv
import os
import sys

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    if isinstance(text, str):
        return "".join(html_escape_table.get(c, c) for c in text)
    else:
        return ""


def main(input_file, output_dir=None):
    if output_dir is None:
        # Repo root = two levels up from this script (scripts -> markdown_generator -> repo).
        repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        output_dir = os.path.join(repo_root, "_talks")

    os.makedirs(output_dir, exist_ok=True)

    ext = os.path.splitext(input_file)[1].lower()
    delimiter = "\t" if ext in (".tsv", ".txt") else ","

    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            title = row.get("title", "").strip()
            url_slug = row.get("url_slug", "").strip()
            date = row.get("date", "").strip()
            talk_type = row.get("type", "").strip()
            venue = row.get("venue", "").strip()
            location = row.get("location", "").strip()
            talk_url = row.get("talk_url", "").strip()
            description = row.get("description", "").strip()

            if not title or not url_slug or not date:
                print("Skipping row: missing required field (title, url_slug, or date)", file=sys.stderr)
                continue

            md_filename = date + "-" + url_slug + ".md"
            md_path = os.path.join(output_dir, md_filename)

            md = "---\n"
            md += "title: \"" + title + "\"\n"
            md += "collection: talks\n"
            if len(talk_type) > 3:
                md += 'type: "' + talk_type + '"\n'
            else:
                md += 'type: "Talk"\n'
            md += "permalink: /talks/" + date + "-" + url_slug + "\n"
            if venue:
                md += 'venue: "' + venue + '"\n'
            md += "date: " + date + "\n"
            if location:
                md += 'location: "' + location + '"\n'
            md += "---\n"

            if talk_url:
                md += "\n[More information here](" + talk_url + ")\n"
            if description:
                md += "\n" + html_escape(description) + "\n"

            with open(md_path, "w", encoding="utf-8") as out:
                out.write(md)
            print("Created: " + md_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 talks.py <input_file> [output_dir]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    main(input_file, output_dir)
