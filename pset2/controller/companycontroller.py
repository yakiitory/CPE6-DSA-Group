from model.company import Company
from view.hierarchy_view import display_hierarchy, indent 
 
class CompanyController:
    def __init__(self):
        self.company = Company()
        self.departments = {
            1: "Human Resource (HR)",
            2: "Develoment",
            3: "Finance",
            4: "Marketing",
            5: "Sales"
        }

    def run(self):
        ceo_name = input("Enter CEO Name: ")
        ceo = self.company.add_ceo(ceo_name)

        num_managers = int(input("Enter number of Department Managers under CEO: "))
        
        for i in range(1, num_managers + 1):
            print(f"\nManager {i}")
            manager_name = input("Enter Manager Name: ")

            print("Choose Manager Department:")
            for key, value in self.departments.items():
                print(f"{key}. {value}")

            while True: 
                dept_choice = int(input("Enter choice (1-5): "))
                if 1 <= dept_choice <= 5:
                    break
                print("Invalid choice. Plase enter a number from 1 to 5")
            
            dept_name = self.departments[dept_choice]
            manager = self.company.add_manager(manager_name, dept_name, ceo)

            num_staff = int(input(f"Enter number of Staff under {dept_name} Manager {manager_name}: "))

            for j in range(1, num_staff + 1):
                staff_name = input(indent(1) + f"Enter Staff {j} Name: ")
                self.company.add_staff(staff_name, manager)

        print("\n=== Company Organizational Hierarchy ===")
        display_hierarchy(self.company.get_nodes())
