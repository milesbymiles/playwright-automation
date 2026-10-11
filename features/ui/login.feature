@ui
Feature: Login
  As a shopper
  I want to log in to the store
  So that I can buy products

  @smoke
  Scenario: Login with valid credentials
    Given the user is on the login page
    When the user logs in with username "standard_user" and the correct password
    Then the Products page is shown

  @regression
  Scenario Outline: Login fails with invalid details
    Given the user is on the login page
    When the user logs in with username "<username>" and password "<password>"
    Then the error message contains "<message>"

    Examples:
      | username        | password     | message               |
      | locked_out_user | secret_sauce | locked out            |
      | standard_user   | wrong_pass   | do not match any user |
