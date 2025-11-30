def main():
    tasks = []  # ลิสต์สำหรับเก็บรายการงาน

    print("=== ยินดีต้อนรับสู่โปรแกรม To-Do List ===")
    print("คำสั่งที่ใช้ได้: add <งาน>, list, remove <เลขลำดับ>, exit")

    while True:
        try:
            # รับคำสั่งจากผู้ใช้
            user_input = input("\n> ").strip()
            
            # แยกคำสั่งและเนื้อหา (เช่น "add อ่านหนังสือ" -> command="add", content="อ่านหนังสือ")
            parts = user_input.split(" ", 1)
            command = parts[0].lower()

            # 1. คำสั่ง Exit
            if command == "exit":
                print("จบการทำงาน ขอบคุณครับ")
                break

            # 2. คำสั่ง Add
            elif command == "add":
                if len(parts) > 1:
                    task = parts[1]
                    tasks.append(task)
                    print(f"เพิ่มรายการ: '{task}' เรียบร้อยแล้ว")
                else:
                    print("กรุณาระบุงานที่จะเพิ่ม (เช่น add อ่านหนังสือ)")

            # 3. คำสั่ง List
            elif command == "list":
                print("รายการสิ่งที่ต้องทำ:")
                if not tasks:
                    print("  (ไม่มีรายการ)")
                else:
                    for index, task in enumerate(tasks, start=1):
                        print(f"  {index}. {task}")

            # 4. คำสั่ง Remove
            elif command == "remove":
                if len(parts) > 1 and parts[1].isdigit():
                    task_index = int(parts[1]) - 1 # แปลงเป็น index ของ list (เริ่มที่ 0)
                    
                    if 0 <= task_index < len(tasks):
                        removed_task = tasks.pop(task_index)
                        print(f"ลบรายการ: '{removed_task}' เรียบร้อยแล้ว")
                    else:
                        print("ไม่พบหมายเลขลำดับนี้ในรายการ")
                else:
                    print("กรุณาระบุหมายเลขลำดับที่จะลบ (เช่น remove 1)")

            # กรณีพิมพ์คำสั่งผิด
            else:
                print("ไม่พบคำสั่งนี้ กรุณาลองใหม่ (add, list, remove, exit)")

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    main()
