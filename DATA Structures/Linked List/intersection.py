def intersetPoint(head1,head2):
    #code here
    l1 = []
    l2 = []
    temp1 = head1
    temp2 = head2
    
    while temp1:
        l1.append(temp1)
        temp1 = temp1.next
        
    while temp2:
        l2.append(temp2)
        temp2 = temp2.next
        
    if len(l1)>len(l2):
        l2.reverse()
        for _ in range(len(l1)-len(l2)):
            l2.append(0)
        l2.reverse()
    elif len(l2)>len(l1):
        l1.reverse()
        for _ in range(len(l2)-len(l1)):
            l1.append(0)
        l1.reverse()
    m = len(l1)
    curr = 0
    prev = -1
    for i in reversed(range(m)):
        curr = l1[i]
        if l1[i] != l2[i]:
            break
        else:
            prev = curr
            
    return prev.data