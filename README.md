# FlaskPortal

Python - 3.5.2
Pycharm - 2016.2.3

Test Coverage:[![codecov.io](https://codecov.io/github/Original_heapsters/FlaskPortal/coverage.svg?branch=master)](https://codecov.io/github/Original_heapsters/FlaskPortal?branch=master)
Continuous Integration:![Build status](https://travis-ci.org/Original-heapsters/FlaskPortal.svg?branch=master)
Stories to be claimed: [![Stories in Ready](https://badge.waffle.io/Original_heapsters/FlaskPortal.png?label=ready&title=Ready)](https://waffle.io/Original_heapsters/FlaskPortal)
Repo Hits:[![ghit.me](https://ghit.me/badge.svg?repo=Original_heapsters/FlaskPortal)](https://ghit.me/repo/Original_heapsters/FlaskPortal)

#### [Build History](https://travis-ci.org/Original_heapsters/FlaskPortal/builds)

<!--Test Coverage: ![codecov.io](https://codecov.io/github/Mosquito-Mashers/Decisionator/branch.svg?branch=master)-->

Project Throughput:[![Throughput Graph](https://graphs.waffle.io/Original-heapsters/FlaskPortal/throughput.svg)](https://waffle.io/Original-heapsters/FlaskPortal/metrics/throughput)

[Issues](https://github.com/Original_heapsters/FlaskPortal/issues) | [Milestones](https://github.com/Original_heapsters/FlaskPortal/milestones) | [Metrics](https://github.com/Original_heapsters/FlaskPortal/graphs/contributors)
___

## About
General info about the FlaskPortal
* What does it do?
* Who is the target audience
* what cloud aspects are there?

## Development Environment
___
What tools we use
* Python 3.5.2
* PyCharm
* Flask
* PyTest
* Git
* Github
* Waffle.io
* Hipchat
* Travis CI

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

## Integration
___
Our integration strategy

The master branch is protected based on the build results from Travis CI, this way we are guaranteed a working build on the master branch. We are implementing the feature branch workflow. A developer will checkout a branch and label it in accordance with the task they plan to achieve. After they have made their changes and commited them to their checked out branch they will initiate an automated build through travis-ci.org; this is done by pushing to their checked out branch. Upon a successful build, they will initiate a pull request which will be reviewed and tested before being merged with the master branch.
