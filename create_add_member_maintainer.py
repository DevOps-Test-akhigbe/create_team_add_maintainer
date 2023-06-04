import sys
import requests

def create_github_team(team_name, organization, github_token):
    url = f"https://api.github.com/orgs/{organization}/teams"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "name": team_name,
        "privacy": "closed"  # You can change the privacy setting if needed
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        print("GitHub team created successfully!")
        return response.json()["id"]
    else:
        print(f"Failed to create GitHub team. Error: {response.text}")
        return None

def add_team_member(team_id, username, organization, github_token):
    url = f"https://api.github.com/teams/{team_id}/memberships/{username}"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "role": "member"
    }
    response = requests.put(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Team member added successfully!")
    else:
        print(f"Failed to add team member. Error: {response.text}")

def promote_member_to_maintainer(team_id, username, organization, github_token):
    url = f"https://api.github.com/teams/{team_id}/memberships/{username}"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "role": "maintainer"
    }
    response = requests.put(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Team member promoted to maintainer successfully!")
    else:
        print(f"Failed to promote team member to maintainer. Error: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python github_script.py <team_name> <organization> <github_token> <member_username>")
        sys.exit(1)

    team_name = sys.argv[1]
    organization = sys.argv[2]
    github_token = sys.argv[3]
    member_username = sys.argv[4]

    team_id = create_github_team(team_name, organization, github_token)
    if team_id:
        add_team_member(team_id, member_username, organization, github_token)
        promote_member_to_maintainer(team_id, member_username, organization, github_token)
