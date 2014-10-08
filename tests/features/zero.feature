Feature: Administrar citas 

Scenario: Login into the system
  Given I go to "http://127.0.0.1:5000/appointments/"
  When I fill in field with id "username" with "email@cimat.mx"
  And I fill in field with id "password" with "thepassword"
  And I submit the form