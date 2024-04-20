Feature: Add Target product to the cart


#  Scenario: User can Add product to cart
#    Given Open Target main page
#    When Search for Taylors of Harrogate Yorkshire - 160
#    Then Click on product
#    Then Click on Add to cart button
#
#
#  Scenario: User can View Cart and verify if it is there
#    Given Open Target main page
#    When Search for Taylors of Harrogate Yorkshire - 160
#    Then Click on product
#    Then Click on Add to cart button
#    When Click on View cart button to go inside Cart

Scenario Outline: User can select color selection for product
    Given Open target product <product_url> page
    Then Verify user can click through <product_name> colors

    Examples:
      | product_url                                    | product_name |
      | https://www.target.com/p/A-91511634            | A-91511634   |
      | https://www.target.com/p/A-54551690            | A-54551690   |


