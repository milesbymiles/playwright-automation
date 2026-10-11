@ui
Feature: Shopping cart
  As a shopper
  I want to add products to my cart
  So that I can buy them later

  Background:
    Given the user is logged in as "standard_user"

  @smoke
  Scenario: Add a product to the cart
    When the user adds "Sauce Labs Backpack" to the cart
    Then the cart badge shows "1"

  @regression
  Scenario: Added product is listed in the cart
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    Then the cart page lists "Sauce Labs Backpack"
