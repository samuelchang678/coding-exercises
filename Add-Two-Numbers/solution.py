# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def addTwoNumbers(self, one: Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
    resultHead = ListNode(0)
    resultLinkedList = resultHead
    carryOver = 0
    currentOne  = one
    currentTwo = two
    while currentOne is not None or currentTwo is not None :
        v1 = currentOne.val if currentOne else 0
        v2 = currentTwo.val if currentTwo else 0
        totalSum = v1 + v2 + carryOver

        resultLinkedList.val = totalSum % 10 
        carryOver = totalSum // 10
    
        resultLinkedList.next = ListNode(0)
        resultLinkedList = resultLinkedList.next

        if currentOne:
            currentOne = currentOne.next   
        if currentTwo:         
            currentTwo = currentTwo.next         
    return resultHead
            
class Solution:
   def addTwoNumbers(self, one: Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
    resultHead = ListNode(0)
    resultLinkedList = resultHead
    carryOver = 0
    currentOne  = one
    currentTwo = two
    while (currentOne is not None or currentTwo is not None):
        v1 = currentOne.val if currentOne else 0
        v2 = currentTwo.val if currentTwo else 0
        totalSum = v1 + v2 + carryOver

        digitValue = totalSum % 10 
        carryOver = totalSum // 10
    
        resultLinkedList.next = ListNode(digitValue)
        resultLinkedList = resultLinkedList.next

        if currentOne:
            currentOne = currentOne.next   
        if currentTwo:         
            currentTwo = currentTwo.next 
    # Final carry over
    if (carryOver > 0 ):
        resultLinkedList.next = ListNode(carryOver)
    return resultHead.next
        



'''

https://leetcode.com/problems/add-two-numbers/description/

My first idea was like , shit gotta write a function to reverse the list

But no, after trying to figure out the third example. I realized that there is no need, we human add from right to left anyway
so the linked list is reverse on purpose.

I DO NOT KNOW HOW TO TRANSVERSE A LINK LIST 
 resultLinkedList.val = totalSum % 10 
   resultLinkedList.next = ListNode(0)
        resultLinkedList = resultLinkedList.next

I initially did the above this would cause me to lose my header which i need to return, when i return at the end I am returning the last node only instead of the whole linked list..... damn

Above is my first iteration i submitted. It's failed the test cases. Below would be the reason why my code fails and the final solution at the end

1.By doing my first, ie creating a new node with value 0 and then overriding it the next iteration. Means that even after i finish I have a tail node that 
is not necessary 

2. I did not account for the final carry over. So the finally, i miss the final List node which should contain the carryOver
'''


class Solution:
   def addTwoNumbers(self, one: Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
    resultHead = ListNode(0)
    resultLinkedList = resultHead
    carryOver = 0
    currentOne  = one
    currentTwo = two
    while (currentOne is not None or currentTwo is not None):
        v1 = currentOne.val if currentOne else 0
        v2 = currentTwo.val if currentTwo else 0
        totalSum = v1 + v2 + carryOver

        digitValue = totalSum % 10 
        carryOver = totalSum // 10
    
        resultLinkedList.next = ListNode(digitValue)
        resultLinkedList = resultLinkedList.next

        if currentOne:
            currentOne = currentOne.next   
        if currentTwo:         
            currentTwo = currentTwo.next 
    # Final carry over
    if (carryOver > 0 ):
        resultLinkedList.next = ListNode(carryOver)
    return resultHead.next