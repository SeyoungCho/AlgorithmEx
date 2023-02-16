def left_child(tree, tree_len):
    child_len = (tree_len - 1 ) // 2
    return tree[0:child_len]

def right_child(tree, tree_len):
    child_len = (tree_len - 1) // 2
    return tree[(child_len + 1):]

def dfs(tree, tree_len):
    if (tree_len == 3):
        if tree[1] == '1':
            return True
        return (tree[0] == '0') and (tree[2] == '0')
    child_len = (tree_len - 1) // 2
    if tree[child_len] == '0' and (tree[child_len+(child_len+1)//2] == '1' or tree[child_len-(child_len+1)//2] == '1'):
        return False
    return dfs(left_child(tree, tree_len), child_len) and dfs(right_child(tree, tree_len), child_len)

def get_min_digits(num):
    original_digit = len(num)
    if original_digit == 1:
        return 1
    target_digit = 1
    while original_digit > (target_digit - 1):
        target_digit *= 2
    return target_digit - 1

def solution(numbers):
    answer = []
    for num in numbers:
        f_num = format(num, 'b')
        tree_size = get_min_digits(f_num)
        print(tree_size)
        f_num = f_num.zfill(tree_size)
        child_size = (tree_size - 1) // 2
        if (f_num[child_size] == '0'):
            answer.append(0)
            continue
        if (tree_size <= 3):
            answer.append(1)
            continue
        ans = dfs(left_child(f_num, tree_size), child_size) and dfs(right_child(f_num, tree_size), child_size)
        answer.append(1 if ans == True else 0)
        
    return answer