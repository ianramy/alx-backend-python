# fixtures.py
#!/usr/bin/env python3
"""
Fixtures for integration tests.
"""

org_payload = {
    "login": "google",
    "repos_url": "https://api.github.com/orgs/google/repos",
}

repos_payload = [
    {"name": "episodes.dart", "license": {"key": "bsd-3-clause"}},
    {"name": "cpp-netlib", "license": {"key": "bsl-1.0"}},
    {"name": "dagger", "license": {"key": "apache-2.0"}},
    {"name": "ios-webkit-debug-proxy", "license": {"key": "other"}},
    {"name": "google.github.io", "license": None},
    {"name": "kratu", "license": {"key": "apache-2.0"}},
    {"name": "build-debian-cloud", "license": {"key": "other"}},
    {"name": "traceur-compiler", "license": {"key": "apache-2.0"}},
    {"name": "firmata.py", "license": {"key": "apache-2.0"}},
]

expected_repos = [
    "episodes.dart",
    "cpp-netlib",
    "dagger",
    "ios-webkit-debug-proxy",
    "google.github.io",
    "kratu",
    "build-debian-cloud",
    "traceur-compiler",
    "firmata.py",
]

apache2_repos = ["dagger", "kratu", "traceur-compiler", "firmata.py"]

TEST_PAYLOAD = [
    org_payload,
    repos_payload,
    expected_repos,
    apache2_repos,
]
