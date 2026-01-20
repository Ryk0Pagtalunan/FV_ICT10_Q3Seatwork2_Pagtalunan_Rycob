from pyscript import display, document

def sign_up(e):
    registration = document.querySelector('input[name="registration"]:checked').value #All of these get the values needed for the next code/to check if they can participate in Intramurals and tells the teams
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade_level = int(document.getElementById("level").value)
    section = int(document.getElementById('section').value)

    if registration == "yes": #First checks if registration is picked yes, as it's the most vital info
        if clearance == "yes": #Secondly, checks if the student has gotten their clearance letter, leading to the next set of codes
            if section == 1: #Runs the code when Emerald is picked whilst also checking if they're in the grades 7-10 and then tells their Intramurals team
                if grade_level >= 1 and grade_level <= 4:
                    display("Congratulations! You are part of the Red Bulldogs!", target="output", append=False)
                else:
                    display("Only Grades 7-10 are eligible for Intramurals, sorry.", target="output", append=False)
            elif section == 2: #Runs the code when Topaz is picked whilst also checking if they're in the grades 7-10 and then tells their Intramurals team
                if grade_level >= 1 and grade_level <= 4:
                    display("Congratulations! You are part of the Blue Bears!", target="output", append=False)
                else:
                    display("Only Grades 7-10 are eligible for Intramurals, sorry.", target="output", append=False)
            elif section == 3: #Runs the code when Ruby is picked whilst also checking if they're in the grades 7-10 and then tells their Intramurals team
                if grade_level >= 1 and grade_level <= 4:
                    display("Congratulations! You are part of the Green Hornets!", target="output", append=False)
                else:
                    display("Only Grades 7-10 are eligible for Intramurals, sorry.", target="output", append=False)
            elif section == 4: #Runs the code when Sapphire is picked whilst also checking if they're in the grades 7-10 and then tells their Intramurals team
                if grade_level >= 1 and grade_level <= 4:
                    display("Congratulations! You are part of the Yellow Tigers!", target="output", append=False)
                else:
                    display("Only Grades 7-10 are eligible for Intramurals, sorry.", target="output", append=False)
            elif section == 5: #Runs the code when Jade is picked whilst also checking if they're in the grades 7-10 and then tells their Intramurals team
                if grade_level >= 1 and grade_level <= 4:
                    display("Congratulations! You are part of the Blue Bears!", target="output", append=False)
                else:
                    display("Only Grades 7-10 are eligible for Intramurals, sorry.", target="output", append=False)
        else:
            display("Please get your clearance letter, and you're all set!", target="output", append=False)
    else:
        display("First of all, please register before anything to participate in Intramurals, thank you.", target="output", append=False)