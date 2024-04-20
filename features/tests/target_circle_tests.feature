Feature: Target Circle page test

  Scenario: Verify there are benefit boxes
    Given Open target main page
    When Click on Target circle link
    Then Verify there are 10 Benefit boxes
