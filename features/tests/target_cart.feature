Feature: Search tests

  Scenario: User can check the cart
    Given Open Target page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown



