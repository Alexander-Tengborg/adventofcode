def a():
    ans = 0
    block = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                block.append(line)
            else:
                line_idx, col_idx = -1, -1
                left = block[0]
                for i in range(1, len(block)):
                    right = block[i]
                    if left == right:
                        cj = i + 1
                        ci = i - 2
                        while ci >= 0 and cj >= 0 and ci < len(block) and cj < len(block) and block[ci] == block[cj]:
                            ci -= 1
                            cj += 1
                        if ci < 0 or cj == len(block):
                            line_idx = i
                            break
                    left = right
                        
                left = ''.join(l[0] for l in block)
                for i in range(1, len(block[0])):
                    right = ''.join(l[i] for l in block)
                    if left == right:
                        cj = i + 1
                        ci = i - 2
                        while ci >= 0 and cj >= 0 and ci < len(block[0]) and cj < len(block[0]) and ''.join(l[ci] for l in block) == ''.join(l[cj] for l in block):
                            ci -= 1
                            cj += 1
                        if ci < 0 or cj == len(block[0]):
                            col_idx = i
                            break
                    left = right
                
                if line_idx != -1:
                    ans += 100 * line_idx
                else:
                    ans += col_idx
                block = []
    return ans

def fixable_smudge(s1, s2):
    if s1 == s2:
        return True, False
    if sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1:
        return True, True
    return False, False

def b():
    ans = 0
    block = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                block.append(line)
            else:
                line_idx, col_idx = -1, -1
                left = block[0]
                for i in range(1, len(block)):
                    if line_idx != -1:
                        break
                    right = block[i]
                    used = False
                    res, used = fixable_smudge(left, right)
                    if res:
                        cj = i + 1
                        ci = i - 2
                        while ci >= 0 and cj >= 0 and ci < len(block) and cj < len(block):
                            if block[ci] == block[cj]:
                                ci -= 1
                                cj += 1
                            elif not used and fixable_smudge(block[ci], block[cj])[0]:
                                ci -= 1
                                cj += 1
                                used = True
                            else:
                                break
                        if (ci < 0 or cj == len(block)) and used:
                            line_idx = i
                            break
                    left = right

                left = ''.join(l[0] for l in block)
                for i in range(1, len(block[0])):
                    if col_idx != -1:
                        break
                    right = ''.join(l[i] for l in block)
                    used = False
                    res, used = fixable_smudge(left, right)
                    if res:
                        cj = i + 1
                        ci = i - 2
                        while ci >= 0 and cj >= 0 and ci < len(block[0]) and cj < len(block[0]):
                            if ''.join(l[ci] for l in block) == ''.join(l[cj] for l in block):
                                ci -= 1
                                cj += 1    
                            elif not used and fixable_smudge(''.join(l[ci] for l in block), ''.join(l[cj] for l in block))[0]:
                                ci -= 1
                                cj += 1
                                used = True
                            else:
                                break
                        if (ci < 0 or cj == len(block[0])) and used:
                            col_idx = i
                            break
                    left = right
                
                if line_idx != -1:
                    ans += 100 * line_idx
                elif col_idx != -1:
                    ans += col_idx
                block = []
    return ans
    
if __name__ == '__main__':
    print(a())
