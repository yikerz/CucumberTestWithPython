Feature: Data Table

    @TableTest
    Scenario: Bill Amount Generation
        Given I placed an order for the following items as table
            | ItemName | Units | UnitPrice |
            | Steak    | 2     | 20        |
            | Salad    | 1     | 15        |
        When I generate the bill
        Then A bill for 55 should be generated