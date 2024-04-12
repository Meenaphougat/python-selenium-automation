Feature: Cart Page tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Verify Item added is visible in Cart
    Given Open target main page
     When Search for Taylors of Harrogate Yorkshire - 160
    Then Click on product
    Then Click on Add to cart button
    When Click on View cart button to go inside Cart
    Then Verify Item is visible in cart