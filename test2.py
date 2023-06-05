import sys
import requests

GITHUB_API = 'https://api.github.com'
TOKEN = 'YOUR_GITHUB_TOKEN'

def validate_team(organization, team):
    url = f'{GITHUB_API}/orgs/{organization}/teams/{team}'
    response = requests.get(url, headers={'Authorization': f'token {TOKEN}'})
    return response.status_code == 200

def validate_member(organization, member):
    url = f'{GITHUB_API}/orgs/{organization}/members/{member}'
    response = requests.get(url, headers={'Authorization': f'token {TOKEN}'})
    return response.status_code == 200

def create_team(organization, team):
    url = f'{GITHUB_API}/orgs/{organization}/teams'
    payload = {'name': team}
    response = requests.post(url, json=payload, headers={'Authorization': f'token {TOKEN}'})
    response.raise_for_status()
    return response.json()['id']

def add_member_to_team(organization, team, member):
    url = f'{GITHUB_API}/orgs/{organization}/teams/{team}/memberships/{member}'
    response = requests.put(url, headers={'Authorization': f'token {TOKEN}'})
    response.raise_for_status()

def promote_to_maintainer(organization, team, member):
    url = f'{GITHUB_API}/orgs/{organization}/teams/{team}/maintainerships/{member}'
    response = requests.put(url, headers={'Authorization': f'token {TOKEN}'})
    response.raise_for_status()

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <organization> <team> <member>")
        return

    organization = sys.argv[1]
    team = sys.argv[2]
    member = sys.argv[3]

    # Validate team and organization
    if not validate_team(organization, team):
        print(f'Team {team} does not exist in organization {organization}')
        return

    # Validate member
    if not validate_member(organization, member):
        print(f'Member {member} does not exist in organization {organization}')
        return

    # Create team
    team_id = create_team(organization, team)
    print(f'Team {team} created with ID {team_id}')

    # Add member to team
    add_member_to_team(organization, team_id, member)
    print(f'Member {member} added to team {team}')

    # Promote member to maintainer
    promote_to_maintainer(organization, team_id, member)
    print(f'Member {member} promoted to maintainer of team {team}')

if __name__ == '__main__':
    main()
