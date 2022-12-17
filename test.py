# import torch
# x = torch.rand(5, 3)
# print(x)

# print(torch.cuda.is_available())

languages = ['Python', 'C', 'C++', 'C#', 'Java']

#Bad way
# i = 0 #counter variable
# for language in languages:
#     print(i, language)
#     i+=1

# #Good Way
for i, language in enumerate(languages):
    print(i, language)