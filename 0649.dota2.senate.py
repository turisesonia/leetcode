"""
# 649
Medium
Dota2 Senate (參議院)

https://leetcode.com/problems/dota2-senate/

In the world of Dota2, there are two parties: the Radiant and the Dire.
在 Dota2 的世界裡, 有兩方勢力, 分別為 Radiant 和 Dire

The Dota2 senate consists of senators coming from two parties.
Dota2 的參議院是由這兩方所派出來的參議員組成

Now the Senate wants to decide on a change in the Dota2 game.
現在, 參議院要決定遊戲的改動

The voting for this change is a round-based procedure.
遊戲改動的投票方式為回合制

In each round, each senator can exercise one of the two rights:
每一回合, 參議員可以從下面兩個動作中選一個執行:

- Ban one senator's right:
    A senator can make another senator lose all his rights in this and all the following rounds.
禁止另外一位參議員的權利, 被禁止的參議院在接下來的回合就不能做任何事

- Announce the victory:
    If this senator found the senators who still have rights to vote are all from the same party,
    he can announce the victory and decide on the change in the game.
宣告勝利, 如果輪到某一位參議員時, 剩下來有資格 (沒有被禁止) 的參議員均隸屬於同一陣營的話, 則該方勝利

Given a string senate representing each senator's party belonging.
The character 'R' and 'D' represent the Radiant party and the Dire party.
給定一個字串表示為參議院, 其中的字母 R, D 為參議員及其代表的勢力

Then if there are n senators, the size of the given string will be n.
字串的長度及代表參議員的數量

The round-based procedure starts from the first senator to the last senator in the given order.
回合由第一個參議員開始, 並依照字串的排序方式執行下去

This procedure will last until the end of voting.
這個程序會一直執行到投票結束
All the senators who have lost their rights will be skipped during the procedure.
當輪到某參議員但已被禁止時, 則跳過此參議員

Suppose every senator is smart enough and will play the best strategy for his own party.
Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Example 1:
Input: senate = "RD"
Output: "Radiant"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:
Input: senate = "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in round 1.
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Constraints:
n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.

# Queue, Greedy
"""
from collections import deque


def predict_party_victory(senate: str) -> str:
    senate: list = [s for s in senate]

    while len(set(senate)) > 1:
        s = senate.pop(0)

        ban = "D" if s == "R" else "R"

        senate.remove(ban)
        senate.append(s)

    return "Radiant" if senate[0] == "R" else "Dire"


def predict_party_victory(senate: str) -> str:
    queue = deque(senate)

    # 找出兩方參議員數量
    r_qty = senate.count("R")
    d_qty = len(senate) - r_qty

    # 用來記錄各方目前被 ban 掉的參議員數量
    r_banned, d_banned = 0, 0

    while r_qty > 0 and d_qty > 0:
        current = queue.popleft()

        if current == "R":
            if r_banned > 0:
                # 代表此位置的參議員已被前一位反方 ban 了
                r_banned -= 1
                r_qty -= 1  # 減少一位有資格的參議員
            else:
                d_banned += 1
                queue.append(current)
        else:
            if d_banned:
                d_banned -= 1
                d_qty -= 1
            else:
                r_banned += 1
                queue.append(current)

    # 判斷有剩餘有資格的一方就是勝利者
    return "Radiant" if r_qty else "Dire"


if __name__ == "__main__":
    assert predict_party_victory("RD") == "Radiant"
    assert predict_party_victory("RDD") == "Dire"
    assert predict_party_victory("RRDDD") == "Radiant"
    assert predict_party_victory("DDRRRR") == "Radiant"
