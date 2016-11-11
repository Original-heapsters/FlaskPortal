# FlaskPortal

Python - 3.5.2
Pycharm - 2016.2.3

Test Coverage:[![codecov](https://codecov.io/gh/Original-heapsters/FlaskPortal/branch/master/graph/badge.svg)](https://codecov.io/gh/Original-heapsters/FlaskPortal)
Continuous Integration:![Build status](https://travis-ci.org/Original-heapsters/FlaskPortal.svg?branch=master)
Stories to be claimed: [![Stories in Ready](https://badge.waffle.io/Original-heapsters/FlaskPortal.png?label=ready&title=Ready)](https://waffle.io/Original-heapsters/FlaskPortal)
Repo Hits:[![ghit.me](https://ghit.me/badge.svg?repo=Original_heapsters/FlaskPortal)](https://ghit.me/repo/Original_heapsters/FlaskPortal)

#### [Build History](https://travis-ci.org/Original_heapsters/FlaskPortal/builds)

Test Coverage: ![codecov.io](https://codecov.io/github/Original-heapsters/FlaskPortal/branch.svg?branch=master)

Project Throughput:[![Throughput Graph](https://graphs.waffle.io/Original-heapsters/FlaskPortal/throughput.svg)](https://waffle.io/Original-heapsters/FlaskPortal/metrics/throughput)

[Issues](https://github.com/Original_heapsters/FlaskPortal/issues) | [Milestones](https://github.com/Original_heapsters/FlaskPortal/milestones) | [Metrics](https://github.com/Original_heapsters/FlaskPortal/graphs/contributors)
___

## About
___
The Flask portal acts as a hub for various experimental applications based around the flask framework. This repository will act as the main portal and the idea is to create repositories anywhere and map them based on their url. Given this information, the main portal will fetch the latest version of any app hosted publicly and host that app within this repo's flask server instance. 

## Development Environment
___
What tools we use
* Python 3.5.2
* PyCharm 2016.2.3
* Flask
* PyTest
* Git
* Github
* Waffle.io
* Hipchat
* Travis CI
* CodeCov

## Contributing
___
How to contribute to the project

1. Clone repo into local machine
    * **git clone http://github.com/Original_heapsters/FlaskPortal.git**
2. Build and run (master branch should be clean)
3. checkout new branch
    *  **git checkout -b {branch-name}**
          * Branch names: "name_of_feature-#issue_number"
          * ex: **git checkout -b adding_login-#12**
4. Add your changes while git adding and git committing often
    * **git checkout...**
    * Open PyCharm and make code changes
    * **git add -A**
    * **git commit -am "Descriptive message explaining what work was done"**
    * make more changes (maybe add more files)
    * **git add -A**
    * **git commit -am "Descriptive message explaining what work was done"**
5. If done working but the feature is not closed:
    * **git add -A**
    * **git commit -am "Descriptive message explaining what work was done"**
    * **git push origin {branch_name}**
        * Enter username and password
6. If done working and your branch closes #issue_number
    * **git add -A**
    * **git commit -am "Description of the changes Fixes #issue_number"**
        * This will close the particular issue once it is merged with master
    * **git push origin {branch_name}**
    * On Github, select your branch from the dropdown menu and click the button to create ***New Pull Request***
    * Either replace the pull requests title with ***Fixes #issue_number*** or put ***Fixes #issue_number*** in the body of the pull request
    * Leave a comment using the @mention for another team memeber to review the code

## Merging into master
___
Merge conflicts required check: No conflicts can be present prior to merging into master
Updated branch required check: The proposed pull request needs to be up to date with the master branch prior to merging
Build status required check: Travis CI will report back whether or not the unit tests completed successfully in order to merge into master
Code Coverage Required check: CodeCov will run after the Travis CI test to report the code coverage of the test suite


## Integration
___
Development will follow a feature branch strategy. Any new development must start with a new branch and, when ready, a pull request must be opened to initiate all CI operations that aide in verifying integrity of changes.
