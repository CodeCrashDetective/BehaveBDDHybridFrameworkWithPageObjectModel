Feature: Register feature

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register page
    When I enter below details into mandatory fields
         |firstname  |lastname  |telephone  |password  |
         |Asif       |Shaikh    |1234567890 |12345     |
    And I select Privacy policy option
    And I click on Continue button
    Then Account should get created


  @register
  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter below details into all fields
         |firstname  |lastname  |telephone  |password  |
         |Asif       |Shaikh    |1234567890 |12345     |
    And I select Privacy policy option
    And I click on Continue button
    Then Account should get created

#  @register1
#  Scenario: Register with duplicate email address
#    Given I navigate to Register page
#    When I enter details into all fields except email
#    And I enter existing email into email field
#    And I select Privacy policy option
#    And I click on Continue button
#    Then Proper warning massage informing about duplicate account should be displayed

  @register
  Scenario: Register without providing any details
    Given I navigate to Register page
    When I dont enter any details into the fields
    And I click on Continue button
    Then Proper warning massage for every mandatory fields should be displayed
