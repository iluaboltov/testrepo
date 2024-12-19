
def createLinkedList(arr):
Creates a linked list from a given array.
    
    Args:
        arr (list): The array of values to create the linked list from.
    
    Returns:
        ListNode: The head of the created linked list.
        if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def printLinkedList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])
merged = mergeTwoLists(list1, list2)
print(printLinkedList(merged))  # Should print: [1, 1, 2, 3, 4, 4]

list1 = createLinkedList([])
list2 = createLinkedList([])
merged = mergeTwoLists(list1, list2)
print(printLinkedList(merged))  # Should print: []

list1 = createLinkedList([])
list2 = createLinkedList([0])
merged = mergeTwoLists(list1, list2)
print(printLinkedList(merged))  # Should print: [0]


def mergeTwoLists_alternative(l1, l2):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode(0)
    current = dummy
    
    # Convert linked lists to arrays
    arr1 = []
    arr2 = []
    
    while l1:
        arr1.append(l1.val)
        l1 = l1.next
    
    while l2:
        arr2.append(l2.val)
        l2 = l2.next
    
    # Merge and sort arrays
    merged_arr = sorted(arr1 + arr2)
    
    # Create new linked list from merged array
    for val in merged_arr:
        current.next = ListNode(val)
        current = current.next
    
    return dummy.next

# Test the alternative solution
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])
merged = mergeTwoLists_alternative(list1, list2)
print(printLinkedList(merged))  # Should print: [1, 1, 2, 3, 4, 4]

list1 = createLinkedList([])
list2 = createLinkedList([])
merged = mergeTwoLists_alternative(list1, list2)
print(printLinkedList(merged))  # Should print: []

list1 = createLinkedList([])
list2 = createLinkedList([0])
merged = mergeTwoLists_alternative(list1, list2)
print(printLinkedList(merged))  # Should print: [0]
