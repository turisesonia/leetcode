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
    if len(ls) == 1:
        return ListNode(ls[0])

    return ListNode(ls[0], list_to_linked(ls[1:]))
