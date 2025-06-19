class SmartFarm: 
    def __init__(self):
        self.tasks = []
        self.task_types = {}

    def run(self):
        while True:
            self.show_menu()
            choice = input("เลือกเมนู (1-5): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.show_summary()
            elif choice == "5":
                print("ขอบคุณที่ใช้โปรแกรม Smart Farm!")
                break

    def show_menu(self): 
        print("====== Smart Farm Task Organizer ======")
        print("1. เพิ่มงานในฟาร์ม")
        print("2. แสดงรายการงานทั้งหมด")
        print("3. ลบงาน")
        print("4. สรุปจำนวนงานในแต่ละประเภท")
        print("5. ออกจากโปรแกรม") 
    def add_task(self):
        name = input(" ป้อนชื่องาน: ")
        date = input(" ป้อนวันที่ (dd/mm/yyyy): ")
        task_type = input(" ประเภทงาน (พืช/ปศุสัตว์/อื่นๆ): ")

        self.tasks.append({"name": name, "date": date, "type": task_type})

        if task_type in self.task_types:
            self.task_types[task_type] += 1
        else:
            self.task_types[task_type] = 1

        print("เพิ่มงานสำเร็จแล้ว")
    def show_tasks(self):
        if not self.tasks:
            print("ไม่มีงานในรายการ")
            return
        print("รายการงานทั้งหมด:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['name']} - {task['date']} - {task['type']}")
    def delete_task(self):
        if not self.tasks:
            print(" ยังไม่มีงานให้ลบ")
            return

        self.show_tasks()
        try:
            index = int(input("ใส่หมายเลขงานที่ต้องการลบ: ")) - 1
            if 0 <= index < len(self.tasks):
                task = self.tasks.pop(index)
                task_type = task["type"]
                self.task_types[task_type] -= 1
                if self.task_types[task_type] == 0:
                    del self.task_types[task_type]
                print(f" ลบงาน '{task['name']}' เรียบร้อยแล้ว")
            else:
                print("ใส่ไม่ถูกต้องไ")
        except ValueError:
            print("ใส่ไม่ถูกต้อง")
    def show_summary(self):
        print("สรุปจำนวนงานในแต่ละประเภท:")
        for task_type, count in self.task_types.items():
            print(f"- {task_type}: {count} งาน")           
if __name__ == "__main__":
    SmartFarm().run()            
