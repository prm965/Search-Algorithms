import pyglet
import random

# Create a window
window = pyglet.window.Window(width=800, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list with random numbers ensuring 42 is included
find_number = 69
numbers = sorted(random.sample(range(1, 100), 19) + [find_number])

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == find_number:
            found = True
        elif numbers[mid] < find_number:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# Schedule the binary search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    # Add title for Linear Search
    title_label = pyglet.text.Label('Binary Search', x=window.width/2, y=window.height * 3/4+10, anchor_x='center', anchor_y='center', font_size=20, bold=True, color=(255, 255, 255, 255), batch=batch)
    title_label.draw()

    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # Draw the box
        if left <= i <= right and not search_complete:
            color = (49, 55, 67)  # Blue for the current search interval
        elif i == mid and not search_complete:
            color = (49, 55, 67)   # Red for the middle element
        elif found and i == mid:
            color = (122, 243, 0)  # Green if 42 is found
        else:
            color = (225, 225, 225) # Grey for eliminated elements
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
