print("Hello World")

# เก็บรายการงานทั้งหมด
tasks = []

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

def edit_task():
    """แก้ไขงาน (empty)"""
    pass

def delete_task():
    """ลบงาน (empty)"""
    pass

def main_menu():
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

if __name__ == "__main__":
    main_menu()