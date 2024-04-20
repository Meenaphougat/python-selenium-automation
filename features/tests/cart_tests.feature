Feature: Cart Page tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Verify Item added is visible in Cart
    Given Open target main page
    When Search for Coffee
    Then Click on Add to cart button
    And Store product name
    When Confirm Add to Cart button from side navigation
    When Click on View cart button to go inside Cart
    Then Verify cart has 1 item(s)
    And Verify cart has correct product


