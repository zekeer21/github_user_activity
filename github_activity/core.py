import requests


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
        "PushEvent": lambda e: f"\tPushed {e['payload']['size']} commits to {e['repo']['name']}",
        "PullRequestEvent": lambda e: f"\tPull request {e['payload']['action']} in {e['repo']['name']}",
        "CreateEvent": lambda e: f"\tCreated {e['payload']['ref_type']} {e['payload']['ref']} in {e['repo']['name']}",
        "ForkEvent": lambda e: f"\tForked {e['repo']['name']}",
        "WatchEvent": lambda e: f"\tStarred {e['repo']['name']}",
        "IssueCommentEvent": lambda e: f"\tCommented on issue {e['payload']['action']} in {e['repo']['name']}",
        "IssuesEvent": lambda e: f"\tIssue {e['payload']['action']} in {e['repo']['name']}",
        "ReleaseEvent": lambda e: f"\tRelease {e['payload']['action']} in {e['repo']['name']}",
        "DeleteEvent": lambda e: f"\tDeleted {e['payload']['ref_type']} {e['payload']['ref']} in {e['repo']['name']}",
        "MemberEvent": lambda e: f"\tMember {e['payload']['action']} in {e['repo']['name']}",
        "CommitCommentEvent": lambda e: f"C\tommented on commit {e['payload']['action']} in {e['repo']['name']}",
        "PublicEvent": lambda e: f"\tPublic {e['repo']['name']}",
        "GollumEvent": lambda e: f"\tollum {e['repo']['name']}",
        "DeploymentEvent": lambda e: f"\tDeployment {e['payload']['action']} in {e['repo']['name']}",
        "DeploymentStatusEvent": lambda e: f"\tDeployment status {e['payload']['action']} in {e['repo']['name']}",
        "CheckRunEvent": lambda e: f"\tCheck run {e['payload']['action']} in {e['repo']['name']}",
        "CheckSuiteEvent": lambda e: f"\tCheck suite {e['payload']['action']} in {e['repo']['name']}",
        "StatusEvent": lambda e: f"\tStatus {e['payload']['state']} in {e['repo']['name']}",
        "PullRequestReviewEvent": lambda e: f"\tPull request review {e['payload']['action']} in {e['repo']['name']}",
        "PullRequestReviewCommentEvent": lambda e: f"\tPull request review comment {e['payload']['action']} in {e['repo']['name']}",
        "RepositoryEvent": lambda e: f"\tRepository {e['payload']['action']} in {e['repo']['name']}",
        "RepositoryDispatchEvent": lambda e: f"\tRepository dispatch {e['payload']['action']} in {e['repo']['name']}",
        "WorkflowRunEvent": lambda e: f"\tWorkflow run {e['payload']['action']} in {e['repo']['name']}",
        "WorkflowDispatchEvent": lambda e: f"\tWorkflow dispatch {e['payload']['action']} in {e['repo']['name']}",
        "WorkflowJobEvent": lambda e: f"\torkflow job {e['payload']['action']} in {e['repo']['name']}",
        "SecurityAdvisoryEvent": lambda e: f"\tSecurity advisory {e['payload']['action']} in {e['repo']['name']}",
    }
    print("Output:")
    for event in data:
        event_type = event.get("type")
        if event_type in event_messages:
            try:
                print(event_messages[event_type](event))
            except KeyError as e:
                print(f"Missing key in event data: {e}")
