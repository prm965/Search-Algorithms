import pyglet
import random

# สร้างหน้าจอแสดงผล
window = pyglet.window.Window(width=800, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# สร้าง  ar rayในการเก็บค่า  และกำหนดให้ตัวแปร find_number หมายถึงตัวเลขที่ต้องการค้นหา
find_number = 69
numbers = sorted(random.sample(range(1, 100), 19) + [find_number])

# สร้างตัวแปรสำหรับให้เกิดภาพเคลื่อนไหว
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

# กำหนดให้เกิดการเคลื่อนไหว ( เปลี่ยนแปลง)ทุก 0.5 วินาที
pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    # ใส่ text ชื่อ Binary Search
    title_label = pyglet.text.Label('Binary Search', x=window.width/2, y=window.height * 3/4+10, anchor_x='center', anchor_y='center', font_size=20, bold=True, color=(255, 255, 255, 255), batch=batch)
    title_label.draw()

    for i, number in enumerate(numbers):
        # กำหนดตำแหน่งในแต่ละกล่อง
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # สร้างกล่อง
        if left <= i <= right and not search_complete:
            color = (49, 55, 67)  
        elif i == mid and not search_complete:
            color = (49, 55, 67) 
        elif found and i == mid:
            color = (122, 243, 0)
        else:
            color = (225, 225, 225)
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # นำตัวเลขที่สร้างใส่ในกล่อง
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
