Feature: Using tip application in web
  As an user in application web version,
  I want to be able to save and organize tips,
  So I can get back and read them later in organized manner.

  Background: User is at the homepage of the application
    Given the homepage is displayed

  Scenario: Saving simple tip
    When the user enters title "The most awesome blog"
    And user clicks save button
    Then "The most awesome blog" should be added to the list

  Scenario: Removing a tip
    Given there is tip titled "First!"
    When user clicks remove button of "First!"
    And user confirms delete
    Then "First!" should not appear in the list
