import sys
import requests

# GitHub access token (replace with your own token)

def create_github_team(team_name, ACCESS_TOKEN):
    url = "https://api.github.com/orgs/DevOps-Test-akhigbe/teams"
    headers = {
        "Authorization": f"token {ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": team_name,
        "privacy": "closed"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("GitHub team created successfully!")
    else:
        print(f"Failed to create GitHub team. Error: {response.text}")


def add_team_maintainer(team_name, maintainer, ACCESS_TOKEN):
    url = f"https://api.github.com/orgs/DevOps-Test-akhigbe/teams/{team_name}/maintainers/{maintainer}"
    headers = {
        "Authorization": f"token {ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.put(url, headers=headers)
    if response.status_code == 204:
        print(f"Added {maintainer} as a maintainer of {team_name} successfully!")
    else:
        print(f"Failed to add maintainer. Error: {response.text}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python create_github_team.py <team_name> <maintainer>")
        sys.exit(1)

    team_name = sys.argv[1]
    maintainer = sys.argv[2]
    ACCESS_TOKEN = sys.argv[3]

    create_github_team(team_name, ACCESS_TOKEN)
    add_team_maintainer(team_name, maintainer, ACCESS_TOKEN)
