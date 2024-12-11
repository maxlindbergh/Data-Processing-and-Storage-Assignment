# Data-Processing-and-Storage-Assignment

## Instructions for Use

1. **Set Up**  
   Copy the provided code into the IDE of your choice (e.g., PyCharm, VSCode, or any other Python IDE). Save the file with a `.py` extension, such as `data_processing_assignment.py`.

2. **Testing the Code**  
   The `main` section of the code contains example usage of the `InMemoryDB` class. You can modify this section to test different parts of the database functionality. For example, you can:  
   - Test transactions by adding, committing, or rolling back changes.  
   - Check the behavior of `get`, `put`, and other methods in different scenarios.  

3. **Error Handling**  
   Be mindful that certain actions, such as calling `put` without an active transaction, will intentionally throw an exception. If an exception is thrown, subsequent code will not execute unless you handle the exception (e.g., with a `try-except` block).

4. **Important Notes**  
   - Keys must be strings, and values must be integers. Using other types will result in a `TypeError`.  
   - The `get` method only retrieves committed values, so uncommitted changes are not visible.  

## Assignment Improvement Suggestions

To make this assignment more structured and effective as an official assignment, the instructions should explicitly define expected behaviors for edge cases, such as attempting to retrieve keys that are modified but not yet committed. Additionally, a requirement for automated test cases could be included to evaluate the code more consistently and reduce grading subjectivity. Providing example input-output scenarios for all methods would clarify expectations for students. Lastly, expanding the functionality to include multiple concurrent transactions (with proper isolation levels) could introduce more complexity and realism to the assignment.
