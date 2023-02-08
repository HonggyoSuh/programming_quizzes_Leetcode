from collections import deque


def connect(self, root):
    # curr = root

    # while curr and curr.left:
    #     left = curr.left

    #     while curr:
    #         curr.left.next = curr.right
    #         curr.right.next = curr.next and curr.next.left
    #         curr = curr.next
    #     curr = left

    # return root

    if not root:
        return None

    queue = deque()
    queue.extend([root, None])

    while queue:
        curr = queue.popleft()
        if curr:
            curr.next = queue[0]
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        elif queue:
            queue.append(None)

    return root
