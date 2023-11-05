Feature: Menu Management

@SmokeTest
Scenario: Add menu item
    Given I have a menu item with name "Steak" and price 20
    When I add the item into the menu
    Then The menu should include the item "Steak"
