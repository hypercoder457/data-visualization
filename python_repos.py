import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    "Accept": "application/vnd.github.v3+json"
}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore info about the repos.
repo_dicts = response_dict['items']
print(f"Repos returned: {len(repo_dicts)}")

# Examine the first repository.
print("\nSelected info about each repo:")


for repo_dict in repo_dicts:
    print('\n')
    print(f"Repo Name: {repo_dict['name']}")
    print(f"Repo Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repo URL: {repo_dict['html_url']}")

    print(f"This repo was created at: {repo_dict['created_at']}")
    print(f"The repo was updated at: {repo_dict['updated_at']}")
    print(f"The repo description: {repo_dict['description']}")

print(f"\nKeys: {len(repo_dict)}")


# Process the results
print(response_dict.keys())
