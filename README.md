# Hospital-DBMS
Hospital-DBMS is a database management system that contains all the details required for the hospital’s official use and the hospital’s employees as the end-users. </br>
This is project was implemented in four phases: 

- **Phase 1** - Defining the mini-world and listing the database requirements and the functional requirements.
- **Phase 2** - Use the requirements defined to draw out an ER diagram.
- **Phase 3** - Convert the ER Diagram to a relational model and then normalize (1st, 2nd and 3rd normal forms).
- **Phase 4** - Set up the hospital database in SQL using the MySQL CLI and create a CLI using Python to access it. 

## Queries that can be run using the CLI
We have used MySQL and PyMySQL client library to interact with the SQL Database. We have implemented several functional requirements, some of which have been listed below: </br>
**1. View details**</br>
The details of several tables namely, Patients, Doctors, Appointments, Departments, Nurses, Services and Staff can be obtained using this query after the user chooses the name of the table.</br>

**2. Searching for details of a patient of a particular birth year**</br>
This query allows the user to input a birth year and outputs the patient details for the patients borm in that year.</br>

**3. Display the total cost for items required in the inventory.**</br>
This query outputs the total amount of money that would be required to buy all the items needed in the inventory.  This is calculated by doing PRICE * COUNT_NEEDED for each entry and summing it across entries. </br>

**4. Insert details**</br>
This query allows the user to add a new row of details to the table required. The user can choose among patients, doctors and appointments here.</br>

**5. Delete details**</br>
This query allows the user to delete a row of details in the table required using its primary key (ID). The user can choose among patients, doctors, nurses and appointments here. The cascading effect has been taken care of.</br>

**6. Updating salary details for the staff**</br>
This query allows the user to update the salary of a member of the hospital staff i.e. any among the doctors, nurses and staff.</br>

**7. Update the details of a patient**</br>
This query allows the user to update the details of a particular patient accessed using the patient ID.</br>

**8. Number of doctors and nurses in a department**</br>
This query outputs the total number of nurses and doctors for the department that the user wants (inputted using department ID).</br>

**9. Display patient details**</br>
This query acts as a projection to give the user the details of all patients in the database.</br>

**10. Display doctors with a certain specialisation**</br>
This query provides a list of all doctors corresponding to the specialization given by the user.</br>

**11. Logout**</br>

## Running

Feed the dump using the following command: </br>
`mysql -h 127.0.0.1 -u username --port==<port number> -p < dump.sql`</br>

Run the python code using the following command: </br>
`python3 main.py`
