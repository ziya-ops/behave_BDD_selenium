Feature: orangehrm log in scenario outline
  Scenario : orangehrm login single
    Given hrm- Launch chrome browser
    When hrm- open orangehrm home page
    And hrm- Enter username "Admin" and password "admin123"
    And hrm- Click Login button
    Then hrm -verify Login success or failure

  Scenario Outline: orangehrm login data driven
    Given hrm- Launch chrome browser
    When hrm- open orangehrm home page
    And hrm- Enter username <uname> and password <pwd>
    And hrm- Click Login button
    Then hrm -verify Login success or failure


    Examples:
      | uname | pwd |
      | Admin  | admin123 |
      | admin123  | admin |
      | user  | pwd |
