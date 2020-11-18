import openpyxl


class GetExcel:
    def load(self, workbook, worksheet):
        '''加载Excel文件。workbook:是工作簿路径
        worksheet:是工作表名'''
        # 打开工作簿
        book = openpyxl.load_workbook(workbook)
        # 获取指定的工作表
        sheet = book[worksheet]
        data = [tuple(cell.value for cell in row) for row in sheet]
        return data[1:]
#
# class Parent(object):
#     def __init__(self, sex, age):
#         self.sex = sex
#         self.age = age
#         print(sex)
#
#     def spam(self):
#         print('Parent.spam')
#
#
# class Child(Parent):
#
#     def __init__(self, sex, age):
#         print(23)
#
#     def spam(self):
#         print('Child.spam')
#         super().spam()  # Call parent spam()
#
#
# if __name__ == "__main__":
#     c = Child(23, 56)
#     c.spam()
