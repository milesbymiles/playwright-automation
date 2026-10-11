@ui
Feature: Products data from Excel
  As a QA engineer
  I want to use Excel files as test data
  So that I can check the app against a data sheet and export what I see

  Background:
    Given the user is logged in as "standard_user"

  @regression
  Scenario: Product prices match the Excel sheet
    Then the product prices match the "prices" sheet in "products.xlsx"

  @regression
  Scenario: Export the product list to an Excel file
    When the user exports the product list to "products_export.xlsx"
    Then the exported file has 6 products
