import os
import tarfile
import tempfile
import shutil
import subprocess
import urllib.request

SING_BOX_URL = "https://github.com/SagerNet/sing-box/releases/download/v1.12.15/sing-box-1.12.15-linux-amd64.tar.gz"
ARCHIVE_NAME = "sing-box.tar.gz"

RULES_JSON = "rules.json"
OUTPUT_SRS = "ruleset.srs"


def download_file(url, dest):
    print(f"Downloading {url}")
    urllib.request.urlretrieve(url, dest)


def find_sing_box_binary(root_dir):
    for root, _, files in os.walk(root_dir):
        if "sing-box" in files:
            return os.path.join(root, "sing-box")
    return None


def main():
    temp_dir = tempfile.mkdtemp(prefix="singbox_")

    try:
        archive_path = os.path.join(temp_dir, ARCHIVE_NAME)

        # download
        download_file(SING_BOX_URL, archive_path)

        # extract
        with tarfile.open(archive_path, "r:gz") as tar:
            tar.extractall(temp_dir)

        # find binary
        sing_box_path = find_sing_box_binary(temp_dir)
        if not sing_box_path:
            raise RuntimeError("sing-box binary not found")

        # make executable (на всякий случай)
        os.chmod(sing_box_path, 0o755)

        # run compile
        cmd = [
            sing_box_path,
            "rule-set",
            "compile",
            RULES_JSON,
            "-o",
            OUTPUT_SRS,
        ]

        print("Running:", " ".join(cmd))
        subprocess.run(cmd, check=True)

        print(f"Rule-set compiled to {OUTPUT_SRS}")

    finally:
        # cleanup
        shutil.rmtree(temp_dir)
        print("Temporary files removed")


if __name__ == "__main__":
    main()
