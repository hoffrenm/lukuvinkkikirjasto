Feature: Adding a tip
    I have found some interesting reading topics,
    and I want to be able to save them with some information
    so I can get back and read them later in organized manner.

    Background: User is at the homepage of the application
        Given the homepage is displayed

    Scenario: Saving simple tip
        When the user enters title "The most awesome blog"
        And user clicks save button
        Then "The most awesome blog" should be added to the list
