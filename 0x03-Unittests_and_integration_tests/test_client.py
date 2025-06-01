#!/usr/bin/env python3
# test_client.py
"""
Unittests for GithubOrgClient class in client.py
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class methods that interact
    with the GitHub API using mocked responses.
    """

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    def test_org(self, org_name) -> None:
        """Test that org returns the correct organization data."""
        with patch("client.get_json") as mock_get_json:
            mock_get_json.return_value = {"login": org_name}
            client = GithubOrgClient(org_name)
            self.assertEqual(client.org, {"login": org_name})
            mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
            )

    def test_public_repos_url(self) -> None:
        """Test that _public_repos_url returns the repos_url correctly."""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test/repos"
            }
            client = GithubOrgClient("test")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/test/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json) -> None:
        """
        Test the `public_repos` method.
        Mocks the get_json method and _public_repos_url property
        to ensure correct parsing of repository names.
        """
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "other"}},
            {"name": "repo3", "license": None},
        ]
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test/repos",
        ) as mock_url:
            client = GithubOrgClient("test")
            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test/repos"
            )
            mock_url.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected) -> None:
        """
        Test if repo has the specified license.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0],
            "repos_payload": TEST_PAYLOAD[1],
            "expected_repos": TEST_PAYLOAD[2],
            "apache2_repos": TEST_PAYLOAD[3],
        }
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for public_repos using fixtures."""

    # CHANGE setUpClass to setUp
    def setUp(self) -> None:
        """Start patching requests.get with fixture payloads for EACH test."""
        self.get_patcher = patch("requests.get")
        self.mock_get = self.get_patcher.start()

        self.mock_get.side_effect = [
            Mock(json=lambda: type(self).org_payload),
            Mock(json=lambda: type(self).repos_payload),
        ]

    # CHANGE tearDownClass to tearDown
    def tearDown(self) -> None:
        """Stop patching requests.get after EACH test."""
        self.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test that public_repos returns expected repos list."""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public_repos returns only repos with apache-2.0 license."""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
