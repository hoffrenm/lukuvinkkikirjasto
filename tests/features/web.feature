Feature: Using tip application in web
  As an user in application web version,
  I want to be able to save and organize tips,
  So I can get back and read them later in organized manner.

  Scenario: Saving simple tip
    Given the homepage is displayed
    When the user enters title "The most awesome blog"
    And user clicks save button
    Then "The most awesome blog" should be added to the list
