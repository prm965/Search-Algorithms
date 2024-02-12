import pyglet
import random

# สร้างหน้าจอแสดงผล
window = pyglet.window.Window(width=1000, height=800, caption='Search Algorithms Comparison')
batch = pyglet.graphics.Batch()

def reset_searches():
    global numbers, linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found, find_number
    # สร้าง array ในการเก็บค่าโดยการสุ่มตัวเลข กำหนดให้ตัวแปร find_numbe r หมายถึงตัวเลขที่ต้องการค้นหา และสั่งให้จัดเรียงลำดับน้อย-มาก
    find_number = 35
    numbers = random.sample(range(1, 100), 21) + [find_number]
    random.shuffle(numbers)  # Shuffle for linear search
    numbers.sort()  

    # Reset search variables
    linear_index = 0
    linear_found = False
    binary_left, binary_right = 0, len(numbers) - 1
    binary_mid = (binary_left + binary_right) // 2
    binary_found = False

reset_searches()  # Initialize searches

def update_searches(dt):
    global linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found, find_number

    # Update linear search
    if not linear_found and linear_index < len(numbers):
        if numbers[linear_index] == find_number:
            linear_found = True
        linear_index += 1

    # Update binary search
    if not binary_found and binary_left <= binary_right:
        binary_mid = (binary_left + binary_right) // 2
        if numbers[binary_mid] == find_number:
            binary_found = True
        elif numbers[binary_mid] < find_number:
            binary_left = binary_mid + 1
        else:
            binary_right = binary_mid - 1

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.R:
        reset_searches()

# กำหนดให้เกิดการเคลื่อนไหว ( เปลี่ยนแปลง)ทุก 0.5 วินาที
pyglet.clock.schedule_interval(update_searches, 0.5)

@window.event
def on_draw():
    window.clear()
    margin = 5  # Margin between boxes
    box_size = (window.width - margin * (len(numbers) + 1)) // len(numbers)  # Calculate box size based on window width and margin
    
    # Add title for Linear Search
    title_label = pyglet.text.Label('Linear Search', x=window.width/2, y=window.height * 3/4 + 50, anchor_x='center', anchor_y='center', font_size=20, bold=True, color=(255, 255, 255, 255), batch=batch)
    title_label.draw()
    
    # Add a line break
    pyglet.text.Label('', x=window.width/2, y=window.height * 3/4, anchor_x='center', anchor_y='center', font_size=20, color=(255, 255, 255, 255), batch=batch).draw()

    # Draw Linear Search boxes
    for i, number in enumerate(numbers):
        x = i * (box_size + margin) + margin  # Calculate x position with margin
        # Linear search boxes (top half)
        y_linear = window.height * 3/4 - box_size / 2
        color_linear = (0, 175, 250) if linear_found and i == linear_index - 1 else (49, 55, 67) if i == linear_index else (225, 225, 225)
        pyglet.shapes.Rectangle(x, y_linear, box_size, box_size, color=color_linear, batch=batch).draw()
        # Draw the number inside each box for linear search, adjust font size for readability
        label = pyglet.text.Label(str(number), x=x + box_size/2, y=y_linear + box_size/2, anchor_x='center', anchor_y='center', color=(255, 0, 0, 255), batch=batch)
        label.draw()

    # Add a line break
    pyglet.text.Label('', x=window.width/2, y=window.height * 1/2, anchor_x='center', anchor_y='center', font_size=20, color=(255, 255, 255, 255), batch=batch).draw()
    
    # Add title for Binary Search
    title_label = pyglet.text.Label('Binary Search', x=window.width/2, y=window.height / 4 + 50, anchor_x='center', anchor_y='center', font_size=20, bold=True, color=(255, 255, 255, 255), batch=batch)
    title_label.draw()
    
    # Add a line break
    pyglet.text.Label('', x=window.width/2, y=window.height / 4, anchor_x='center', anchor_y='center', font_size=20, color=(255, 255, 255, 255), batch=batch).draw()

    # Draw Binary Search boxes
    for i, number in enumerate(numbers):
        x = i * (box_size + margin) + margin  # Calculate x position with margin
        # Binary search boxes (bottom half)
        y_binary = window.height / 4 - box_size / 2
        color_binary = (122, 243, 0) if binary_found and i == binary_mid else (49, 55, 67) if binary_left <= i <= binary_right else (225, 225, 225)
        pyglet.shapes.Rectangle(x, y_binary, box_size, box_size, color=color_binary, batch=batch).draw()
        # Draw the number inside each box for binary search, adjust font size for readability
        label = pyglet.text.Label(str(number), x=x + box_size/2, y=y_binary + box_size/2, anchor_x='center', anchor_y='center', color=(255, 0, 0, 255), batch=batch)
        label.draw()

pyglet.app.run()
