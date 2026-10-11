@ui
Feature: Product sorting (dropdown)
  As a shopper
  I want to sort products using the dropdown
  So that I can find items by name or price

  Background:
    Given the user is logged in as "standard_user"

  @regression
  Scenario: Sort products by name Z to A
    When the user sorts products by "Name (Z to A)"
    Then the first product is "Test.allTheThings() T-Shirt (Red)"

  @smoke
  Scenario: Sort products by price low to high
    When the user sorts products by "Price (low to high)"
    Then the first product is "Sauce Labs Onesie"
