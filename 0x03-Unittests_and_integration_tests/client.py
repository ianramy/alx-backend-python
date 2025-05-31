# client.py
#!/usr/bin/env python3
"""
Client module to interact with GitHub organizations.
"""

from typing import List, Dict
from utils import get_json, memoize


class GithubOrgClient:
    """GithubOrgClient class for interacting with GitHub APIs."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str):
        self.org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Fetch the organization information."""
        return get_json(self.ORG_URL.format(org=self.org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for public repositories of the organization."""
        return self.org["repos_url"]

    def public_repos(self, license: str = None) -> List[str]:
        """Return a list of public repository names filtered by license."""
        repos = get_json(self._public_repos_url)
        names = [
            repo["name"]
            for repo in repos
            if not license or self.has_license(repo, license)
        ]
        return names

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if a repo has the specified license."""
        return repo.get("license", {}).get("key") == license_key
