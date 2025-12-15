import gradio as gr

# converts user's text input into list of integers
def parse_nums(text): 
    text = (text or "").strip().replace(",", " ")
    if text == "":
        return []
    return [int(x) for x in text.split()]

# bubble sort logic
# runs algorithm and records the state of the list after each swap
def bubble_sort_steps(nums):
    steps = []
    arr = nums.copy()
    steps.append(("start", arr.copy())) # initial state

    n = len(arr)
    for i in range(n): # full pass through list 
        swapped = False
        for j in range(len(arr) - 1 - i): # compares adjacent elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                steps.append((f"swap {j} and {j+1}", arr.copy()))
        if not swapped: # exit loop if already sorted
            break
    steps.append(("done", arr.copy())) # final sorted state             
    return steps

# validates input and prepares slider
def start_bubble(text):
    try:
        nums = parse_nums(text)
    except ValueError:
        slider = gr.update(minimum=1, maximum=1, value=1, interactive=False)
        return None, slider, "Please try again, only integers are accepted.", "" # disables slider if non-integer input

    if len(nums) < 2: # 
        slider = gr.update(minimum=1, maximum=1, value=1, interactive=False)
        return None, slider, "Please try again, bubble sort requires at least two numbers.", ""

    steps = bubble_sort_steps(nums) # runs bubble sort and stores all steps 

    slider = gr.update( # enables slider and sets range to number of steps
        minimum=1, 
        maximum=len(steps), 
        value=1, 
        step=1, 
        interactive=True
    ) 
    label, arr = steps[0]
    return steps, slider, f"step 1 / {len(steps)} — {label}", str(arr)

# displays selected step
def show_step(steps, step_num):
    if steps is None:
        return "click start first.", ""

    # converts slider value to list index
    num_index = int(step_num) - 1
    num_index = max(0, min(num_index, len(steps) -1)) # convert slider position to list index
    label, arr = steps[num_index]
    return f"step {num_index + 1}/ {len(steps)} - {label}", str(arr)

# UI
with gr.Blocks(title="Bubble Sort Visualization 🫧") as demo:
    gr.Markdown(
    """
    # Bubble Sort Visualization 🫧
    **Instructions:**
    1. Enter a list of numbers in the box below (seperated by commas and spaces).
    2. Click the start button to run the algorithm.
    3. Use the slider to view each step.
    """
    )    
    inp = gr.Textbox(label="Numbers", value="13, 74, 48, 2, 99, 31")
    start_btn = gr.Button("Start")

    # stores all precomputed algorithm steps 
    steps_state = gr.State(None)

    # slider appears immediately but is disabled until start is clicked
    slider = gr.Slider(
        minimum=1,
        maximum=1,
        value=1,
        step=1,
        label="Please select a step",
        interactive=False
    )

    status = gr.Textbox(label="Status", interactive=False, value="Click Start.")
    output = gr.Textbox(label="Array at this step", interactive=False)

    # runs algorithm and initializes visualization 
    start_btn.click(
        fn=start_bubble,
        inputs=[inp],
        outputs=[steps_state, slider, status, output]
    )

    # updates display when slider is moved
    slider.change(
        fn=show_step,
        inputs=[steps_state, slider],
        outputs=[status, output],
        trigger_mode="always_last"
    )

demo.launch(share=True, ssr_mode=False)
