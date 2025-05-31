# 0x03. Unittests and Integration Tests

This project focuses on learning how to write unit and integration tests in Python using the `unittest` framework. The goal is to test functionality, isolate components, and ensure code reliability without relying on external systems.

## Learning Objectives

By the end of this project, you should be able to explain:

- The difference between **unit tests** and **integration tests**
- How to write **parameterized tests**
- How to **mock** external dependencies like APIs
- What **fixtures**, **patching**, and **memoization** mean in testing

---

## Project Structure

```bash
0x03-Unittests_and_integration_tests/
├── client.py                  # GithubOrgClient class implementation
├── fixtures.py                # Predefined data payloads for integration tests
├── test_client.py             # Unit and integration tests for GithubOrgClient
├── test_utils.py              # Tests for utils module
├── utils.py                   # Utility functions used throughout
└── README.md                  # This file!
```

## File Descriptions

`utils.py`

- access_nested_map: Safely access keys in nested dictionaries

- get_json: Fetch and parse JSON from a URL

- memoize: Decorator to cache results of a method

`client.py`

- GithubOrgClient: Class to interact with GitHub's organization APIs

- .org - fetch org data

- .public_repos - fetch public repos with optional license filter

`fixtures.py`

- Contains pre-baked mock payloads used in integration testing

`test_utils.py`

- Unit tests for all functions in utils.py

- Uses parameterized tests and mocking

`test_client.py`

- Unit and integration tests for GithubOrgClient

- Uses mock patches for external API calls

- Includes parameterized_class for full integration test suites
