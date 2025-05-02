# GitHub User Activity CLI

This is a Python command-line application that fetches and displays recent activity for a specified GitHub user using the GitHub Events API.

## Features

- Fetches recent events for a GitHub user.
- Displays human-readable descriptions of the events, such as pushes, pull requests, issues, and more.

## Prerequisites

- Python 3.6 or higher
- `requests` library (install using `pip install requests`)

## Installation

1. Clone this repository or download the script:

   ```bash
   git clone https://github.com/your-repo/github_user_activity.git
   cd github_user_activity
   ```

2. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Usage

Run the script using the command-line interface (CLI). The script supports the following command:

### Command: `github-activity`

Fetches and displays the recent activity of a GitHub user.

### Syntax:

```bash
python script.py github-activity <username>
```

### Arguments:

- `github-activity`: The command to fetch GitHub user activity.
- `<username>`: The GitHub username whose activity you want to fetch.

### Example:

To fetch the activity of a user named `octocat`:

```bash
python script.py github-activity octocat
```

### Output:

The script will display a list of recent events for the specified user in a human-readable format. For example:

```
Pushed 3 commits to example-repo
Pull request opened in example-repo
Starred example-repo
```

## Error Handling

- If the username is invalid or there is an issue with the GitHub API, an error message will be displayed.
- If the response cannot be parsed as JSON, the script will notify you with a parsing error.

## Notes

- The GitHub API has rate limits. If you exceed the limit, you may receive a `403 Forbidden` response.
- Ensure you have an active internet connection to fetch data from the GitHub API.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
