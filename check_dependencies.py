import subprocess
import sys


def main():
    result = subprocess.run(
        ["poetry", "show", "--outdated", "--top-level"], capture_output=True, text=True
    )
    outdated_packages = result.stdout.strip().split("\n")
    outdated_count = len(outdated_packages) - 1

    print(f"Number of outdated dependencies: {outdated_count}")
    print()
    print(result.stdout)

    if outdated_count > 10:
        print("Too many outdated dependencies! Build failed.")
        sys.exit(1)
    else:
        print("Dependency check passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()