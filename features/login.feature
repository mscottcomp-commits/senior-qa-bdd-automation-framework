Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given I am on the SauceDemo login page
    When I login with valid credentials
    Then I should see the products page

  Scenario: Invalid login shows error message
    Given I am on the SauceDemo login page
    When I login with invalid credentials
    Then I should see a login error message