Feature: Facebook log in
  Scenario: Facebook login fail
    Given Launch chrome browser
    When open facebook home page
    And Enter email "testacb@gmail.com" and password "admin123"
    And Click Login button
    Then verify Login failure error msg
    And Close browser