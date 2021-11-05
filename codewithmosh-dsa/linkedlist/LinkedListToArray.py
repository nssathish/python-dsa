from LinearLinkedListOps import LinkedList


def ConvertLinkedListToArray(linked_list):
	array_from_given_list = []
	head = linked_list.head
	while head is not None:
		array_from_given_list.append(head.data)
		head = head.next
	
	return array_from_given_list


if __name__ == '__main__':
	newList = LinkedList(1)
	newList.addLast(2); newList.addLast(3); newList.addLast(4)
	newList.addFirst(0)
	print('Input linked list:')
	newList.print()
	print(ConvertLinkedListToArray(newList))
