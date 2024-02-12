import pyglet
import random

# สร้างหน้าจอแสดงผล
window = pyglet.window.Window(width=800, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# สร้าง array ในการเก็บค่าโดยการสุ่มตัวเลข และกำหนดให้ตัวแปร find_number หมายถึงตัวเลขที่ต้องการค้นหา
find_number = 69
numbers = random.sample(range(1, 100), 19) + [find_number]
random.shuffle(numbers)

# สร้างตัวแปรสำหรับให้เกิดภาพเคลื่อนไหว
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

# กำหนดให้เกิดการเคลื่อนไหว(เปลี่ยนแปลง)ทุก 0.5 วินาที
pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    # ใส่ text ชื่อ Linear Search
    title_label = pyglet.text.Label('Linear Search', x=window.width/2, y=window.height * 3/4+10, anchor_x='center', anchor_y='center', font_size=20, bold=True, color=(255, 255, 255, 255), batch=batch)
    title_label.draw()

    for i, number in enumerate(numbers):
        # กำหนดตำแหน่งในแต่ละกล่อง
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # สร้างกล่อง
        if i == current_index and not search_complete:
            color = (49, 55, 67)  
        elif i == found_index:
            color = (0, 175, 250) 
        else:
            color = (225, 225, 225)
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # นำตัวเลขที่สร้างใส่ในกล่อง
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
