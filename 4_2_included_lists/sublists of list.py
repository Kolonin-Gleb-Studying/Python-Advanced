# ��� ��������� ��������� ������

lst = [el for el in input().split()]
print(lst) # a b v

# ��������� ����� 0
list_of_sublists = [[], ]

# ������������ ���������� ���� �� 1 �� ����� ������ ������ - 1
sub_list_size = 1

while sub_list_size != len(lst):
	sub_lst = []
	for el in range(len(lst)): # ��������� ��������� ������� �����.TODO: �������� ��� ����� ����� while, �.�. ��������� ���� for �� ��������� ������������ ��������?
		
		sub_lst.append(el)
		list_of_sublists.append(list(el))


# ��������� ������������ ���� �� 2 �� ����� ������ -1




# ��������� ������������ ����� = ��� ������
list_of_sublists.append(lst)

print(list_of_sublists) # [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]

