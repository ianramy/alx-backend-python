# fixtures.py
#!/usr/bin/env python3
"""
Fixtures for integration tests.
"""

TEST_PAYLOAD = (
    {"login": "test", 
     "repos_url": "https://api.github.com/orgs/test/repos"},
    [
        {"name": "repo1", "license": {"key": "apache-2.0"}},
        {"name": "repo2", "license": {"key": "other"}},
        {"name": "repo3", "license": {"key": "apache-2.0"}},
    ],
    ["repo1", "repo2", "repo3"],
    ["repo1", "repo3"],
)
