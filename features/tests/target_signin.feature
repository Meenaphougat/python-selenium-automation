Feature: SignIn tests

  Scenario: User can check SignIn page
    Given Open Target main page
    When Click on SignIn icon
    When From right side navigation menu, click Sign In
    Then Verify “Sign into your Target account” message is shown


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click on SignIn icon
    When From right side navigation menu, click Sign In
    #Given Open sign in page ### This direct URL is not working so Using another approach
    Given Store original Window
    When Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window