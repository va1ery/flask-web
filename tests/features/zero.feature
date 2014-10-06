Feature: Administrar citas 

Scenario: Create an appoitment
    Given I go to "http://127.0.0.1:5000/appointments/create/"  
  	When I fill in field with id "title" with "Una cita"
  	And I fill in field with id "start" with "2010-11-11 12:00:00"
  	And I fill in field with id "end" with "2010-11-11 13:00:00"
  	And I fill in field with id "location" with "The office"
  	And I fill in field with id "description" with "Una descripcion"
  	And save the appointment in the bottom "saveApp"
  	

Scenario: Consult an appoitment
	Given I go to "http://127.0.0.1:5000/appointments/8/"
	Then The element with class of "appointment-detail" contains "algo"

Scenario: Consult an appoitment that does not exist
	Given I go to "http://127.0.0.1:5000/appointments/0/"
	Then I see that the title of the page contains "Not Found"

Scenario: Edit a given appointment
  Given I go to "http://127.0.0.1:5000/appointments/1/edit"
  When I update the field with id "title" with "Titulo Nuevo"
  And save the appointment in the bottom "saveApp"
  Then The element with class of "appointment-detail" contains "Titulo Nuevo"

Scenario: Edit a date given appointment
  Given I go to "http://127.0.0.1:5000/appointments/1/edit"
  When I update the field with id "start" with actual date
  And save the appointment in the bottom "saveApp"
  Then The element with class of "appointment-detail" contains the actual date

Scenario: List all appoitments    
  Given I go to "http://127.0.0.1:5000/appointments/"
  Then I see at least "2" appoitments with the class "appointment-detail"