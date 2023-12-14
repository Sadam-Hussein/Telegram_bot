

class Scheldue:
    def __init__(self, lesson, teacher, cabinet, para, group):
        self.lesson = lesson
        self.teacher = teacher
        self.cabinet = cabinet
        self.para = para
        self.group = group

    def __str__(self):
        return f"{self.para} / {self.lesson} / {self.teacher} in {self.cabinet} with {self.group}"

class ScheldueInit:
    def __init__(self, file_path, openpyxl):
        self.file_path = file_path
        
        self.wb = openpyxl.load_workbook(self.file_path)

        self.ws = self.wb.active
        self.skip_arr = ["1 пара", "2 пара", "3 пара", "4 пара", "5 пара"]
        self.data_group = []
        self.row_group = self.__get_group_row()
        for gr in range(1, self.ws.max_column - 1):
            val = self.ws.cell(row=self.row_group, column=gr).value
            if val is not None:
                data_group_id = f"{val} ! {gr}"
                self.data_group.append(data_group_id)
        
        self.current_group = "Test group"
        self.data_cabinet = []
        self.data_teacher = []
        self.data_lesson = []
        self.data_para = []
        self.new_data_group = []
        self.current_para = "1 пара"

        for i in range(1, self.ws.max_row - 1):
            for j in range(1, self.ws.max_column - 1):
                val = self.ws.cell(row=i, column=j).value
                
                if val is None or str(val).strip() == "":
                    continue
                elif str(val).strip() in self.skip_arr:
                    current_para = str(val).strip()
                else:
                    current_group = self.__get_group_name(j-1)
                    if "/" in str(val):
                        data_cell = str(val).split("/")
                        self.data_lesson.append(data_cell[0])
                        self.data_teacher.append(data_cell[1])
                    if len(str(val)) == 3 or len(str(val)) == 4 or val == "Академия КП" or val == "Приполье":
                        self.data_cabinet.append(val)
                        self.data_para.append(current_para)
                        self.new_data_group.append(current_group)

        self.data_classes = []
        for all_i in range(len(self.data_cabinet)):
            super_new_obj = f"{self.data_lesson[all_i]}!{self.data_teacher[all_i]}!{self.data_cabinet[all_i]}!{self.data_para[all_i]}!{self.new_data_group[all_i]}"
            self.data_classes.append(super_new_obj)
        self.data_classes = list(set(self.data_classes))
        self.clear_data_classes = []
        for user in self.data_classes:
            user = user.split("!")
            para = user[3]
            lesson = user[0]
            teacher = user[1]
            cabinet = user[2]
            group = user[4]
            obj = Scheldue(lesson, teacher, cabinet, para, group)
            self.clear_data_classes.append(obj)

    def list_main(self):
        repeat = True
        while repeat:
            main = str(input("""
            1. Кто оккупировал кабинет?
            2. Какие у папы суриката пары?
            3. Кто из папы сурикатов свободен?
            4. Какие пары у группы сурикатов?
            5. С кем поменяться ключами?
            6. Какой кабинет свободен?
            Действие: """))
            if main == "1":
                print(self.find_by_cabinet())
            elif main == "2":
                print(self.find_papa_surikat())
            elif main == "3":
                print(self.find_free_surikat())
            elif main == "4":
                print(self.find_for_group_surikat())
            elif main == "5":
                print(self.kuda_nesti_key())
            elif main == "6":
                print(self.find_free_cabinet())
            else:
                print("Не понял")
            

            

            repeat = self.__repeat()

        

    def find_by_cabinet(self, cab:str = "") -> list:
        data = []
        if cab == "":
            cab = input("Кабинет: ")
        for user in sorted(self.clear_data_classes, key=lambda user: user.para):
            user:Scheldue = user
            if cab == str(user.cabinet):
                data.append(str(user))
                #print(str(user))
        return data

    def find_papa_surikat(self, teacher:str = "") -> list:
        data = []
        if teacher == "":
            teacher = input("Папа сурикат: ")
        for user in sorted(self.clear_data_classes, key=lambda user: user.para):
            user:Scheldue = user
            if teacher in user.teacher:
                data.append(str(user))
        return data

    def find_free_surikat(self) -> list:
        data = []
        para = input("""
        1 пара
        2 пара
        3 пара
        4 пара
        5 пара
        Цифра: """)
        all_teacher = list(set(self.data_teacher))
        for user in sorted(self.clear_data_classes, key=lambda user: user.teacher): 
            user:Scheldue = user
            if user.para == f"{para} пара":
                if user.teacher in all_teacher:
                    all_teacher.remove(user.teacher)
        for teach in all_teacher:
            data.append(teach)
            #print(teach)
                #print(str(user))
        return data

    def find_for_group_surikat(self) -> list:
        data = []
        all_group = list(set(self.data_group))
        str_all_group = [f"{group}" for group in all_group]
        str_all_group += "Имя группы: "
        group_name = input(str_all_group)
        for user in sorted(self.clear_data_classes, key=lambda user: user.para): 
            user:Scheldue = user
            if group_name in user.group:
                data.append(str(user))
                #print(str(user))
        return data

    def kuda_nesti_key(self) -> str:
        data = ""
        para = input("Номер пары: ")
        key_cab = input("Ключ который у вас: ")
        key_need = input("Ключ который нужен: ")
        need = ""
        if int(para) < 5:
            for user in sorted(self.clear_data_classes, key=lambda user: user.para): 
                if user.para == f"{int(para) + 1} пара" and user.cabinet == key_cab:
                    data += f"Ваш ключ нужен папе сурикату {user.teacher}"
                    #print(f"Ваш ключ нужен папе сурикату {user.teacher}")
                if user.para == f"{int(para)} пара" and user.cabinet == key_need:
                    need = f"Ключ который нужен вам у папы суриката {user.teacher}"
        if need == "":
            data += "\nСкорее всего ключ на охране."
            #print("Скорее всего ключ на охране.")
        else:
            data += f"\n{need}"
            #print(need)
        return data

    def find_free_cabinet(self) -> str:
        data = []
        para = input("""
        1 пара
        2 пара
        3 пара
        4 пара
        5 пара
        Цифра: """)
        all_cabinet = list(set(self.data_cabinet))
        all_str_cabinet = []
        for item in all_cabinet:
            all_str_cabinet.append(str(item))
            
        for user in sorted(self.clear_data_classes, key=lambda user: user.cabinet): 
            user:Scheldue = user
            if user.para == f"{para} пара":
                if user.cabinet in all_str_cabinet:
                    all_str_cabinet.remove(user.cabinet)
        for cabi in all_str_cabinet:
            data.append(cabi)
            #print(cabi)
        return data

    def __repeat(self) -> bool:
        return input("Continue?[y/n]") == "y"

    def __get_group_row(self):
        for i in range(1, self.ws.max_row - 1):
            for j in range(1, self.ws.max_column - 1):
                val = self.ws.cell(row=i, column=j).value
                if "ИСиП" in str(val):
                    return i
    def __get_group_name(self, index: int):
        for group in self.data_group:
            if "!" in str(group):
                group_arr = str(group).split("!")
                group_id = int(str(group_arr[1]).strip())
                group_name = group_arr[0]
                
                if group_id >= index:
                    #print(f"{index}-{group_id} : {group_name}")
                    return group_name
            

    # def get_data(self):
    #     data = input('Введите номер кабинета:')
    #     return data
