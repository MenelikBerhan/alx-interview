#!/usr/bin/python3
"""Contains a function to solve Lockboxes puzzle"""


def canUnlockAll(boxes: 'list[list]') -> bool:
    """Checks if all boxes in the list can be opened.

    Args:
        boxes: a list of boxes. Each box in boxes is numbered sequentially
        from 0 to n - 1 and each box may contain keys to the other boxes.

    Returns:
        bool: True if all boxes could be opened, else False.
    """
    if len(boxes) == 0:
        return True
    # a list containg a set of opened boxes & a set of acquired keys
    queue = [{0}, set(k for k in boxes[0] if k != 0 and k < len(boxes))]

    # separate set of keys found. used to stop loop if all keys are found
    keys_found = {0}
    keys_found.update(boxes[0])

    boxes_len = len(boxes)
    # all_keys = {k for k in range(boxes_len)}
    # loop as long as all boxes are not opened & there is unused key
    while len(queue[0]) != boxes_len and queue[1]:
        # print(f'keys_found:{keys_found}\nqueue:{queue}')

        # if all keys are found return
        if len(keys_found) == boxes_len:
            return True

        # get nxt box key and remove key from set of keys in queue
        next_box = queue[1].pop()
        # print(f'next_box: {next_box}')
        # add box to be opened (next_box) to set of opened boxes in queue
        queue[0].add(next_box)

        # open box and take keys of boxes not visited sofar (not in queue[0])
        # new_keys = set(boxes[next_box]).difference(queue[0])
        new_keys = {
            k for k in boxes[next_box] if k < boxes_len
            }.difference(queue[0])
        # print(f'new keys: {new_keys}')

        # add new keys to set of keys in queue and to set of keys found
        queue[1].update(new_keys)
        keys_found.update(new_keys)

    # if all boxes
    if len(queue[0]) == boxes_len:
        return True
    return False
