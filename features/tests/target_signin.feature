Feature: SignIn tests

  Scenario: User can check SignIn page
    Given Open Target main page
    When Click on SignIn icon
    When From right side navigation menu, click Sign In
    Then Verify “Sign into your Target account” message is shown
