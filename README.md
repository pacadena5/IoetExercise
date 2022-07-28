# IoetExercise

# Execution process
I have performed the exercise in python.
1. Open a terminal in the folder
2. Navigate to the solution folder "ACME work hours coincided" with 'cd ACME work hours coincided' or alternative
you can directly open a terminal here
3. Execute the command "python .\App\main.py" and the app start running

# Methodology / Approach
I have focused on reading the data and separating that from the matching hours comparison algorithm.
First I declare my models, which are: Person to manage the information, Hour for the comparisons and 
LaborHour to manage the hours. Then I create my controllers which are: FileReader to read the data, 
HoursChecker to manage the hours and compare them, and WorkHoursController to execute the algorithm 
to compare the matching hours.
Finally i use my controlles in main.py to display the output required.

# Architecture
I use a MVC architecture with the following working tree
ACME Work Hours Coincided
	|-App
		|-Models
			|- Hour
			|- LaborHour
			|- Person
		|-Controllers
			|- FilerReader
			|- HoursChecker
			|- WorkHoursController
		|-main.py
	|-Test
		|- ControllersTest
		|- ModelsTest