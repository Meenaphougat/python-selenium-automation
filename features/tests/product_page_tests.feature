Feature: Add Target product to the cart


  Scenario: User can Add product to cart
    Given Open Target main page
    When Search for Taylors of Harrogate Yorkshire - 160
    Then Click on product
    Then Click on Add to cart button


  Scenario: User can View Cart and verify if it is there
    Given Open Target main page
    When Search for Taylors of Harrogate Yorkshire - 160
    Then Click on product
    Then Click on Add to cart button
    When Click on View cart button to go inside Cart

