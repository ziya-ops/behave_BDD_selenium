Feature: Facebook logo
  Scenario: Logo presence on facebook home page
    Given Launch chrome browser
    When open facebook home page
    Then verify that logo is present on home page
    And Close browser