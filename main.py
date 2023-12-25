from FileHandlerJson import FileHandlerJson
from ServiceNote import ServiceNote

service1 = ServiceNote(FileHandlerJson())
service1.add_note("Доброе утро","Как дела?")
service1.add_note("Добрый день","Как дела днем?")
service1.add_note("Добрый вечер","Как дела вечером?")
# #
# # service1.to_string()
# # print("++++++++++++++++++++++++")
service1.to_string()
print(service1)
service1.save()

# # service1.remove_notes()
# service1.to_string()
# print("++++++++++++++++++++++")
# service1.remove_notes()
# service1.to_string()
# print("+++++++++++++++++++++++++")

service1.remove_notes()

print("+++++++++++++++++++++++++++")

service1.read()
service1.to_string()




















