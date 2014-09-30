Feature: Go to google  

Scenario: Create an appoitment
    Given I go to "http://127.0.0.1:5000/appointments/create/"  
  	When I fill in field with id "title" with "Una cita"
  	And I fill in field with id "start" with "2010-11-11 12:00:00"
  	And I fill in field with id "end" with "2010-11-11 13:00:00"
  	And I fill in field with id "location" with "The office"
  	And I fill in field with id "description" with "Una descripcion"
  	
