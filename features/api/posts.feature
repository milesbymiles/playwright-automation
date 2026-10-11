@api
Feature: Posts API
  As a client application
  I want to read, create and update posts
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

  @regression
  Scenario: Create a post using a payload file
    When the client creates a post using the "create_post" payload
    Then the response status is 201
    And the response title is "Post created from payload file"
    And the response body is "This body comes from data/payloads/create_post.json"

  @regression
  Scenario: Update a post using a payload file
    When the client updates post 1 using the "update_post" payload
    Then the response status is 200
    And the post id in the response is 1
    And the response title is "Post updated from payload file"
