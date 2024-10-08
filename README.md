# Automation tests using Playwright-pytest
### Performed on https://www.bstackdemo.com

Requires installation of:
- python 3.12
- pytest-playwright
- pytest-xdist
- pytest-html

To run the code, navigate to bstackdemo_automation_testing/tests and run the command:
```
pytest
```
Files:
+ /conftest: configures html test report
+ /tests/pytest.ini: runs tests in msedge with added cli commands
+ /tests/html-test-report: step by step execution of tests
