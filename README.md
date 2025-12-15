## Algorithm Name: bubble_sort_visualization 

## Visualization Demonstration Video:
https://github.com/user-attachments/assets/91733600-17a9-4c2e-8b57-2d2f3007f9b8

## Problem Breakdown & Computational Thinking
1. Decomposition:

- Receive and validate user input (list of numbers)
- Prompt bubble sort with start button
- Compare adjacent numbers in the list
- Swap elements if they are out of order
- Record each swap
- Display each recorded step using slider

2. Pattern Recognition:

Bubble sort repeatedly follows the same pattern:
- Compare two adjacent values
- Swap the values if the left one is larger
- Larger items "bubble" up through list as this process is repeated
- Continue until no swaps are needed

3. Abstraction:

- This program should hide implementation details such as swap performances and conditional checks from the user, providing only a simplified visualization.
- Algorithm should be presented in sequential manner rather than computational.
- Implementing user input and slide bar engages users and facilitates interactive learning.
- This program should only provide details on meaningful changes in algorithm in order to simplify understanding.

4. Algorithm Design:

- Program will be broken down into three main functions: input handling, algorithm processing, and output visualization.
- Each step will be recorded, demonstrating which elements are being compared and the resulting state of the list after each swap.
- The use of a slider will allow users to look through the steps without having to re-run the algorithm, enabling interactive exploration.


## Steps to Run

1. Enter list of numbers seperated by commas and spaces.
2. Click start to execute bubble sort algorithm
3. Use the slider to move through each recorded step of the algorithm.
4. Observe the changes in the list after each comparison and swap. 

## Hugging Face Link
https://huggingface.co/spaces/alexataylor/bubble_sort_visualization

## Author and Acknowledgement 

Author Name: Alexa Taylor

Acknowledgement:
1. I consulted the official gradio website to help me understand how to properly configure the slider component in my program. On this website I learned how to set up the slider's range and connect it to a function that displayed the output.
https://www.gradio.app/main/docs/gradio/slider
2. I used ChatGPT (level 4) to help me identify why my code kept continually producing runtime errors, which it pointed out was caused by mismatched return values in callback functions which were causing Gradio to call errors.
3. I also used ChatGPT (level 4) to help me debug why my code would run but the output displayed would be inconsistent or buggy. ChatGPT helped clarify certain logical issues where the UI components were not behaving as expected and provided solutions for how to improve the visualization such as properly resetting the slider after each run and preventing unnessecary re-execution of the function by storing the steps and states.

## Testing and Verification

The following images detail some test cases I explored to see how my program handled different user inputs:
<img width="1280" height="800" alt="Screenshot 2025-12-15 at 3 03 45 AM" src="https://github.com/user-attachments/assets/c0cfda4d-d91f-4f2d-b085-5046ae7d2d05" />
1. Identical elements only✅

This was handled well as only 1 step was recorded as this is how bubble sort behaves when only the outer loop runs.

  <img width="1280" height="800" alt="Screenshot 2025-12-15 at 3 04 49 AM" src="https://github.com/user-attachments/assets/4d3738c1-af15-4003-bb08-a50c82115277" />

2. No commas✅

Although I put in the description that commas were required, I included this second case in code where they are only seperated by spaces to prevent unnecessary errors.

<img width="1280" height="800" alt="Screenshot 2025-12-15 at 3 05 05 AM" src="https://github.com/user-attachments/assets/76326e24-04e7-4036-a27b-fbffa8371d89" />

3. Input > 1✅

This program validates that the user has provided more than one element before running the algorithm as sorting requires at least two in order to perform comparisons.

<img width="1280" height="800" alt="Screenshot 2025-12-15 at 3 06 15 AM" src="https://github.com/user-attachments/assets/3ec87cd9-6e8a-4697-9475-9db2a4b0ca19" />

4. Handles non numerical input✅

This program validates user input and detects and handles non-numerical input to prevent runtime errors. 
