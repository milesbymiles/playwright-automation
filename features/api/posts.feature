@api
Feature: Posts API
  As a client application
  I want to read and create posts
  So that I can show content to users

  @smoke
  Scenario: Get an existing post
    When the client requests post number 1
    Then the response status is 200
    And the post id in the response is 1

  @regression
  Scenario: Create a new post
    When the client creates a post with title "My first post"
    Then the response status is 201
    And the response title is "My first post"

  @regression
  Scenario: Request a post that does not exist
    When the client requests post number 99999
    Then the response status is 404
