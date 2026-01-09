def process_domains(input_file: str, output_file: str) -> None:
    domains = set()

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            if not stripped or stripped.startswith("#"):
                continue

            if "#" in stripped:
                stripped = stripped.split("#", 1)[0].strip()

            if stripped:
                domains.add(stripped)

    with open(output_file, "w", encoding="utf-8") as f:
        for domain in sorted(domains):
            f.write(domain + "\n")


process_domains("hosts.txt", "hosts.txt")
