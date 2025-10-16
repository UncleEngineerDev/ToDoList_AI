import json
import os

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")

print("Hello World")

# เก็บรายการงานทั้งหมด
tasks = []

def save_tasks():
    """บันทึก tasks ลงไฟล์ tasks.json"""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"สังเกต: เกิดข้อผิดพลาดตอนบันทึกข้อมูล: {e}")

def load_tasks():
    """โหลด tasks จากไฟล์ tasks.json (ถ้าไม่มีไฟล์ ให้เริ่มจากรายการว่าง)"""
    global tasks
    if not os.path.exists(TASKS_FILE):
        return
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                tasks = data
            else:
                print("ไฟล์ tasks.json ไม่อยู่ในรูปแบบที่ถูกต้อง — เริ่มจากรายการว่าง")
                tasks = []
    except json.JSONDecodeError:
        print("ไฟล์ tasks.json ไม่สามารถอ่านได้หรือไม่ถูกต้อง — เริ่มจากรายการว่าง")
        tasks = []
    except Exception as e:
        print(f"สังเกต: เกิดข้อผิดพลาดตอนโหลดข้อมูล: {e}")
        tasks = []

# โหลดข้อมูลเมื่อเริ่มโปรแกรม
load_tasks()

def add_task():
    """เพิ่มงานใหม่ (empty -> รับข้อมูลจากผู้ใช้และเก็บลง tasks)"""
    title = ""
    while not title.strip():
        title = input("ชื่องาน: ").strip()
        if not title:
            print("ชื่องานห้ามว่าง กรุณากรอกอีกครั้ง")
    description = input("รายละเอียด: ").strip()
    due_date = input("วันครบกำหนด (ตัวอย่าง 2025-10-31 หรือเว้นว่าง): ").strip()

    # หาค่า id ถัดไป
    next_id = max((t['id'] for t in tasks), default=0) + 1

    task = {
        "id": next_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print(f"เพิ่มงานเรียบร้อย (id={next_id})")

def view_tasks():
    """ดูงานทั้งหมด"""
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return

    print("\nรายการงานทั้งหมด:")
    for idx, t in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
        due = t.get("due_date") or "-"
        print(f"{idx}. {t.get('title')} | วันครบกำหนด: {due} | สถานะ: {status}")

def update_task():
    """แก้ไขข้อมูลงาน: เลือกจากลำดับ (index) และแก้ title, description, completed"""
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return

    print("\nรายการงาน:")
    for idx, t in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
        due = t.get("due_date") or "-"
        print(f"{idx}. {t.get('title')} | วันครบกำหนด: {due} | สถานะ: {status}")

    # เลือกงานโดย index (1-based)
    while True:
        sel = input("เลือกหมายเลขงานที่จะแก้ไข (หรือกด q เพื่อยกเลิก): ").strip()
        if sel.lower() == "q":
            print("ยกเลิกการแก้ไข")
            return
        if not sel.isdigit():
            print("กรุณากรอกตัวเลขที่ถูกต้อง")
            continue
        idx = int(sel)
        if not (1 <= idx <= len(tasks)):
            print("เลขลำดับไม่ถูกต้อง กรุณาลองอีกครั้ง")
            continue
        task = tasks[idx - 1]
        break

    # แก้ชื่องาน
    print(f"ชื่องานปัจจุบัน: {task.get('title')}")
    new_title = input("ชื่องานใหม่ (เว้นว่างเพื่อคงเดิม): ").strip()
    if new_title:
        task['title'] = new_title

    # แก้รายละเอียด
    print(f"รายละเอียดปัจจุบัน: {task.get('description')}")
    new_desc = input("รายละเอียดใหม่ (เว้นว่างเพื่อคงเดิม): ").strip()
    if new_desc:
        task['description'] = new_desc

    # แก้สถานะ completed
    cur = "y" if task.get('completed') else "n"
    while True:
        new_comp = input(f"สถานะเสร็จแล้ว? (y/n, เว้นว่างคงเดิม) [ปัจจุบัน: {cur}]: ").strip().lower()
        if new_comp == "":
            break
        if new_comp in ("y", "yes"):
            task['completed'] = True
            break
        if new_comp in ("n", "no"):
            task['completed'] = False
            break
        print("กรุณากรอก y หรือ n หรือเว้นว่างเพื่อคงเดิม")

    print(f"อัปเดตงานเรียบร้อย (id={task.get('id')})")

def edit_task():
    """แก้ไขงาน (wrapper -> update_task)"""
    update_task()

def delete_task():
    """ลบงาน: เลือกจากลำดับ (index) และยืนยันก่อนลบ"""
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return

    print("\nรายการงาน:")
    for idx, t in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
        due = t.get("due_date") or "-"
        print(f"{idx}. {t.get('title')} | วันครบกำหนด: {due} | สถานะ: {status}")

    # เลือกงานโดย index (1-based)
    while True:
        sel = input("เลือกหมายเลขงานที่จะลบ (หรือกด q เพื่อยกเลิก): ").strip()
        if sel.lower() == "q":
            print("ยกเลิกการลบ")
            return
        if not sel.isdigit():
            print("กรุณากรอกตัวเลขที่ถูกต้อง")
            continue
        idx = int(sel)
        if not (1 <= idx <= len(tasks)):
            print("เลขลำดับไม่ถูกต้อง กรุณาลองอีกครั้ง")
            continue
        task = tasks[idx - 1]
        break

    # แสดงรายละเอียดสั้น ๆ ของงานที่เลือกเพื่อยืนยัน
    print("\nงานที่เลือก:")
    due = task.get("due_date") or "-"
    status = "เสร็จแล้ว" if task.get("completed") else "ยังไม่เสร็จ"
    print(f"ชื่องาน: {task.get('title')}")
    print(f"รายละเอียด: {task.get('description')}")
    print(f"วันครบกำหนด: {due}")
    print(f"สถานะ: {status}")

    # ยืนยันการลบ
    while True:
        confirm = input("ต้องการลบงานนี้จริงหรือไม่ (y/n): ").strip().lower()
        if confirm in ("y", "yes"):
            removed = tasks.pop(idx - 1)
            print(f"ลบงานเรียบร้อย (id={removed.get('id')})")
            return
        if confirm in ("n", "no"):
            print("ยกเลิกการลบ")
            return
        print("กรุณาตอบ y หรือ n")

def main_menu():
    try:
        while True:
            print("\nเมนูหลัก:")
            print("1. เพิ่มงานใหม่")
            print("2. ดูงานทั้งหมด")
            print("3. แก้ไขงาน")
            print("4. ลบงาน")
            print("5. ออกจากโปรแกรม")
            choice = input("เลือกเมนู (1-5): ").strip()

            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                edit_task()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                print("ออกจากโปรแกรม")
                break
            else:
                print("ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง")
    except KeyboardInterrupt:
        print("\nยุติโปรแกรมโดยผู้ใช้")
    finally:
        # บันทึกข้อมูลก่อนออกเสมอ
        save_tasks()

if __name__ == "__main__":
    main_menu()