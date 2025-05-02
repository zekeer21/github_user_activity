import argparse
from .core import fetch_github_user_activity


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub user activity")
    parser.add_argument(
        "username", help="GitHub username"
    )  # Only one argument: username
    args = parser.parse_args()
    fetch_github_user_activity(args.username)


if __name__ == "__main__":
    main()
