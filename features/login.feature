Feature: Login functionality

  @login
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |email                         |password          |
      |assifgshaikh@gmail.com        |Asif@1995         |
      |asifsk1@gmail.com             |Asif@123          |
      |asifsk2@gmail.com             |Asif@123456       |


  @login1
  Scenario: Login with invalid email and valid password
    Given I navigated to login page
    When I enter invalid email and  valid password as "12345" into the fields
    And I click on Login button
    Then I should get a proper warning massage

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I enter valid email as "assifgshaikh@gmail.com" and invalid password as "12345" into the fields
    And I click on Login button
    Then I should get a proper warning massage

  @login
  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I enter invalid email address and invalid password as "12345" into the fields
    And I click on Login button
    Then I should get a proper warning massage

  @login
   Scenario: Login without entering any credentials
    Given I navigated to login page
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning massage
