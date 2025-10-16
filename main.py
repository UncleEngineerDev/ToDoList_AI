print("Hello World")

def add_task():
    """เพิ่มงานใหม่ (empty)"""
    pass

def view_tasks():
    """ดูงานทั้งหมด (empty)"""
    pass

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