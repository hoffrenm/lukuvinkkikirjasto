Feature: Removing a tip
    Once I have added some tips,
    I want to be able to remove them,
    so my tiplist stays up-to-date and organized. 

    Background: User is at the homepage of the application
        Given the homepage is displayed

    Scenario: Removing a tip
        Given there is tip titled "First!"
        When user clicks remove button of "First!"
        And user confirms delete
        Then "First!" should not appear in the list
