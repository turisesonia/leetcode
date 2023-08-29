class ListNode:
    def __repr__(self):
        ret = f"{self.val}"

        nex = self.next
        while nex is not None:
            ret += f" -> {nex.val}"
            nex = nex.next

        return ret

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def list_to_linked(ls: list):
    if len(ls) <= 0:
        return None

    if len(ls) == 1:
        return ListNode(ls[0])

    return ListNode(ls[0], list_to_linked(ls[1:]))


def linked_to_list(link: ListNode):
    if not link:
        return []

    l = [link.val]
    next_ = link.next
    while next_ is not None:
        l.append(next_.val)
        next_ = next_.next

    return l
