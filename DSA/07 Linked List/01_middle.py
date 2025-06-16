def middle(head):
	fast = slow = head 
	while fast and fast.next:
		slow = slow.next
		fast = fast.next
	return slow 
