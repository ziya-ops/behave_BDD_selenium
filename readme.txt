*** This is a sample BDD Testing Project ***

*** Tools Used ***
1. python
2. pycharm IDE
3. Selenium package for python
4. behave package for python
5. behave-allure package for python
6. allure

*** Directory structure ***
1. features :
    a. feature files : BDD tests
    b. steps
        - step definition files
2. reports : Test results generated in the form of json using allure.

*** commands ***
1. to run feature file :
    - behave [feature file name]

2. to run feature file and generate allure reports :
    - behave -f allure_behave.formatter:AllureFormatter -o [output reports dir] [feature files path]

3. to generate HTML reports :
    a. download scoop(windows pkg installer) : using powershell : iwr -useb get.scoop.sh | iex
    b. install allure through scoop : scoop install allure
    c. run command : allure serve [path to json reports generated in step 2]
