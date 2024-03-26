#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Scenario 1: Grocery Shopping List
You are creating a program to manage a grocery shopping list. Users should be able to add items, 
remove items, and display the current list.


# In[ ]:


shopping_list = input("Enter your items, please use ',' after each item:").split(',')

yes_no_add = input("Do you want to delete some items? Enter 'yes' otherwise 'no' or want to add another item Enter 'add':")

if yes_no_add == "no":
    print(f"This is your shopping_list: {shopping_list}")
    
elif yes_no_add == "yes":
    delete_items = input("Enter item you want to remove, please use ',' after each item:").split(',') 
    
    for items in delete_items:
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"This is your updated items list: {shopping_list}")
        else:
            print(f"{item} not found in item list.")
elif yes_no_add == "add":
        add_items = input("Enter item please use ',' after each item:").split(',')
        shopping_list.append(add_items)
        print(f"This is your new items list {shopping_list}")
              
else:
    print("Invalid input. Try again.")

print(shopping_list)


# In[ ]:





# In[ ]:





# In[ ]:


Scenario 2: Student Grades
You are managing student grades using a dictionary. You need to calculate the average grade.take 
atleast 5 Students grades & then calculate the average.


# In[ ]:


def calculate_student_average(student_grades):
    total = sum(student_grades.values())
    num_subjects = len(student_grades)
    if num_subjects == 0:
        return 0  
    average = total / num_subjects
    return average, total

def main():
    
    students_data = {}

    num_students = 5
    student_names = ["Ali", "Babar", "Faisal", "Dawood", "Ahmer"]
    subjects = ["Math", "English", "Science", "History"]

    
    student_name = "Ali"
    student_grades = {"Math": 90, "English": 85, "Science": 92, "History": 84}
    students_data[student_name] = student_grades
    
   
    student_name = "Babar"
    student_grades = {"Math": 91, "English": 85, "Science": 93, "History": 85}
    students_data[student_name] = student_grades
        
    
    student_name = "Faisal"
    student_grades = {"Math": 92, "English": 85, "Science": 94, "History": 86}
    students_data[student_name] = student_grades
       
   
    student_name = "Dawood"
    student_grades = {"Math": 93, "English": 85, "Science": 95, "History": 87}
    students_data[student_name] = student_grades
   
    
   
    student_name = "Ahmer"
    student_grades = {"Math": 94, "English": 85, "Science": 96, "History": 88}
    students_data[student_name] = student_grades
    

    print("\nTotal Numbers Obtained in Each Subject:")
    for subject in subjects:
        total_subject_marks = sum(students_data[student][subject] for student in student_names)
        print(f"{subject}: {total_subject_marks}")

    
    print("\nAverage Grades for Each Student:")
    for student in student_names:
        student_grades = students_data[student]
        student_average, total_student_marks = calculate_student_average(student_grades)
        print(f"{student}: Average Grade: {student_average:.2f}, Total Marks: {total_student_marks}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:


Scenario 3: Word Frequency Counter
You are given a list of words, and you need to count the frequency of each word.
word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]


# In[2]:


word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]
word_frequency = {}

for word in word_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("word_frequency:")

for word, frequency in word_frequency.items():
    print(f"{word}: {frequency} times")


# In[ ]:





# In[ ]:





# In[ ]:


Scenario 3: Password Strength Checker
You are creating a program to check the strength of passwords based on certain criteria.
Password should be at least 8 characters long.
Password should contain at least one digit.
Password should contain at least one letter.


# In[ ]:


def check_password_strength(password):
    
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."

    
    if not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."

    
    return "Strong: Password meets all criteria."


password = input("Enter your password: ")
result = check_password_strength(password)
print(result)


# In[ ]:





# In[ ]:





# In[ ]:


You are developing a simple voting system for a contest. Users can vote for their Favorite option, and 
you need to count the votes.
In a corporate setting, the HR department is organizing the Annual Employee Recognition Awards, 
where employees get the opportunity to vote for their colleagues nominated in different categories. 
The HR team has decided to use a simple voting system to collect and tally votes for the nominees in 
various award categories. The script provided will be utilized for this purpose.
Candidates: The nominees for different award categories, such as "Employee of the Year," "Team 
Player of the Year," and "Innovation Award," are represented by the list of candidates: 'Candidate A,' 
'Candidate B,' and 'Candidate C.'
Voting Process: Employees are requested to input the number of voters participating in the awards. 
Each voter is presented with a list of nominees, and they can vote for their preferred candidate by 
entering the corresponding number.
Validation: The script ensures that the entered vote is within the valid range of candidates. If an 
employee enters an invalid vote, the system prompts them to choose a valid candidate.
Recording Votes: The script records each vote for the selected candidate and prints a confirmation 
message indicating that the vote has been recorded.
Results Display: Once all votes are collected, the system displays the voting results, showing the 
number of votes each candidate received in each category.
Award Winners: Based on the voting results, the HR department can identify the winners for each 
award category and proceed with recognizing and rewarding the selected employees during the 
Annual Employee Recognition Ceremony.
This script provides a straightforward and transparent way for employees to participate in the 
recognition process, fostering a sense of engagement and community within the organization. The 
HR team can use the collected votes to acknowledge and appreciate the efforts of outstanding 
employees in various aspects of their work


# In[1]:


def get_valid_vote():
    while True:
        try:
            vote = int(input("Enter the number corresponding to your preferred candidate (1 for Candidate A, 2 for Candidate B, 3 for Candidate C): "))
            if 1 <= vote <= 3:
                return vote
            else:
                print("Invalid vote! Please choose a valid candidate.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    candidates = ['Candidate A', 'Candidate B', 'Candidate C']

    num_voters = int(input("Enter the number of voters participating in the awards: "))

    votes = [0, 0, 0]

    for i in range(num_voters):
        print(f"\nVoter {i + 1}:")
        vote = get_valid_vote()
        votes[vote - 1] += 1
        print(f"Vote recorded for {candidates[vote - 1]}.\n")

    
    print("\nVoting Results:")
    for i, candidate in enumerate(candidates):
        print(f"{candidate}: {votes[i]} votes")

    
    winners = [candidates[i] for i, count in enumerate(votes) if count == max(votes)]
    print("\nWinners:")
    for winner in winners:
        print(f"{winner} wins in their respective category!")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:


# Voting system programm


# In[6]:


candidates = ['Candidate A', 'Candidate B', 'Candidate C']
votes = {candidate: 0 for candidate in candidates}
num_voters = int(input("Enter the number of voters: "))

for _ in range(num_voters):
    print("candidates:")
    for i, candidate in enumerate(candidates, start=1):
        print(f"{i}, {candidate}")
        
    vote = int(input("Enter the number corrosponding to your vote: "))
    
    if 1 <= vote <= len(candidates):
        selected_candidate = candidates[vote -1]
        votes[selected_candidate] += 1
        print(f"Vote for {selected_candidate} recorded,")
    else:("invalid vote. Please choose a valid candidate.")
        
print("\nVoting results:")
for candidate, vote_count in votes.items():
    print(f"{candidate}: {vote_count} votes")  


# In[ ]:




