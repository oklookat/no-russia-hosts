import json
import sys

def domains_to_rules(input_file, output_file):
    domains = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            domains.append(line)

    data = {
        "version": 3,
        "rules": [
            {
                "domain_suffix": domains
            }
        ]
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_file = sys.argv[1]   # ../hosts.txt
    output_file = sys.argv[2]  # tmp file
    domains_to_rules(input_file, output_file)
