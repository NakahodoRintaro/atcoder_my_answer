def calc_min_op(n, stone, left_red):
    ans = float('inf')
    for i in range(n+1):
        # stone[:i] は R, stone[i:] は W にするときの最小回数
        left_excess_w = i - left_red[i]
        right_excess_r = left_red[n] - left_red[i]
        operations = max(left_excess_w, right_excess_r)
        ans = min(ans, operations)
    return ans
 
 
def main():
    n = int(input())
    stone = input()
    # stone[:i] のうち R であるものの数
    left_red = [0] * (n + 1)
    for i in range(1, n + 1):
        left_red[i] = left_red[i-1] + (1 if stone[i-1] == 'R' else 0)
    print(calc_min_op(n, stone, left_red))
 
 
if __name__ == '__main__':
    main()
