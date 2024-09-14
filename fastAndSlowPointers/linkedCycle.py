from linked_list import LinkedList
#O(n)时间复杂度，O（1）空间复杂度
def detect_cycle(head):
   #声明2个pointer，一个slow一个fast
   slow = head
   fast = head
   #fast走2步，slow走一步，直到fast的next为null
   while fast and fast.next is not None:
       slow = slow.next
       fast = fast.next.next
       if slow == fast:
           return True
   #如果fast和slow相遇返回True
   return False