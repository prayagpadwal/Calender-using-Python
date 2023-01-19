### Find the middle of a given linked list
# Taken from GeeksforGeeks: 
## https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/

# Given a singly linked list, find the middle of the linked list. 
# For example:
# if the given linked list is 1->2->3->4->5 then the output should be 3. 
# If there are even nodes, then there would be two middle nodes, 
# we need to print the second middle element. For example, 
# if the given linked list is 1->2->3->4->5->6 then the output should be 4. 


class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class solution:
    def middleLL(self, head: Node):
        slow , fast = head, head
        count = 0

        while fast: #is NOT NULL
            slow = head.next
            fast = head.next.next

            while fast:
                count += 1

                if count % 2 == 0: # Even nodes
                    return slow.next
                else: # Odd nodes
                    return slow
        

