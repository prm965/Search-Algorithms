import pyglet
import random

# Create a window
window = pyglet.window.Window(width=800, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a list with random numbers ensuring 42 is included
find_number = 69
numbers = random.sample(range(1, 100), 19) + [find_number]
random.shuffle(numbers)

# Variables to control the animation and search
current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == find_number:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

# Schedule the linear search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    # Add title for Linear Search
    title_label = pyglet.text.Label('Linear Search', x=window.width/2, y=window.height * 3/4+10, anchor_x='center', anchor_y='center', font_size=20, bold=True, color=(255, 255, 255, 255), batch=batch)
    title_label.draw()

    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # Draw the box
        if i == current_index and not search_complete:
            color = (49, 55, 67)  # Red for the current box being checked
        elif i == found_index:
            color = (0, 175, 250) # Green if 42 is found
        else:
            color = (225, 225, 225)  # Grey for unchecked or passed boxes
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
