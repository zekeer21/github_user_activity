import requests
import argparse


def fetch_github_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    try:
        data = response.json()
    except ValueError:
        print("Error parsing JSON response")
        return

    event_messages = {
        "PushEvent": lambda e: f"Pushed {e['payload']['size']} commits to {e['repo']['name']}",
        "PullRequestEvent": lambda e: f"Pull request {e['payload']['action']} in {e['repo']['name']}",
        "CreateEvent": lambda e: f"Created {e['payload']['ref_type']} {e['payload']['ref']} in {e['repo']['name']}",
        "ForkEvent": lambda e: f"Forked {e['repo']['name']}",
        "WatchEvent": lambda e: f"Starred {e['repo']['name']}",
        "IssueCommentEvent": lambda e: f"Commented on issue {e['payload']['action']} in {e['repo']['name']}",
        "IssuesEvent": lambda e: f"Issue {e['payload']['action']} in {e['repo']['name']}",
        "ReleaseEvent": lambda e: f"Release {e['payload']['action']} in {e['repo']['name']}",
        "DeleteEvent": lambda e: f"Deleted {e['payload']['ref_type']} {e['payload']['ref']} in {e['repo']['name']}",
        "MemberEvent": lambda e: f"Member {e['payload']['action']} in {e['repo']['name']}",
        "CommitCommentEvent": lambda e: f"Commented on commit {e['payload']['action']} in {e['repo']['name']}",
        "PublicEvent": lambda e: f"Public {e['repo']['name']}",
        "GollumEvent": lambda e: f"Gollum {e['repo']['name']}",
        "DeploymentEvent": lambda e: f"Deployment {e['payload']['action']} in {e['repo']['name']}",
        "DeploymentStatusEvent": lambda e: f"Deployment status {e['payload']['action']} in {e['repo']['name']}",
        "CheckRunEvent": lambda e: f"Check run {e['payload']['action']} in {e['repo']['name']}",
        "CheckSuiteEvent": lambda e: f"Check suite {e['payload']['action']} in {e['repo']['name']}",
        "StatusEvent": lambda e: f"Status {e['payload']['state']} in {e['repo']['name']}",
        "PullRequestReviewEvent": lambda e: f"Pull request review {e['payload']['action']} in {e['repo']['name']}",
        "PullRequestReviewCommentEvent": lambda e: f"Pull request review comment {e['payload']['action']} in {e['repo']['name']}",
        "RepositoryEvent": lambda e: f"Repository {e['payload']['action']} in {e['repo']['name']}",
        "RepositoryDispatchEvent": lambda e: f"Repository dispatch {e['payload']['action']} in {e['repo']['name']}",
        "WorkflowRunEvent": lambda e: f"Workflow run {e['payload']['action']} in {e['repo']['name']}",
        "WorkflowDispatchEvent": lambda e: f"Workflow dispatch {e['payload']['action']} in {e['repo']['name']}",
        "WorkflowJobEvent": lambda e: f"Workflow job {e['payload']['action']} in {e['repo']['name']}",
        "SecurityAdvisoryEvent": lambda e: f"Security advisory {e['payload']['action']} in {e['repo']['name']}",
    }

    for event in data:
        event_type = event.get("type")
        if event_type in event_messages:
            try:
                print(event_messages[event_type](event))
            except KeyError as e:
                print(f"Missing key in event data: {e}")


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub user activity")
    parser.add_argument(
        "command",
        choices=["github-activity"],
        help="Command to execute",
    )
    parser.add_argument("username", help="GitHub username")

    if len(vars(parser.parse_args())) == 0:
        parser.print_help()
        return

    args = parser.parse_args()

    if args.command == "github-activity":
        fetch_github_user_activity(args.username)


if __name__ == "__main__":
    main()
