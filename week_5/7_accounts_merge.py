# https://leetcode.com/problems/accounts-merge/
from collections import defaultdict
from typing import List


class DisjointSetUnion:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x) -> int:
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        lx, ly = self.find(x), self.find(y)
        if lx != ly:
            if self.rank[lx] > self.rank[ly]:
                self.par[ly] = lx
            elif self.rank[lx] < self.rank[ly]:
                self.par[lx] = ly
            else:
                self.par[lx] = ly
                self.rank[lx] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DisjointSetUnion(len(accounts))
        email_to_account = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_account:
                    email_to_account[email] = idx
                else:
                    dsu.union(email_to_account[email], idx)
        email_group = defaultdict(list)
        for email, idx in email_to_account.items():
            l_idx = dsu.find(idx)
            email_group[l_idx].append(email)
        result = []
        for idx, emails in email_group.items():
            account_name = accounts[idx][0]
            result.append([account_name] + sorted(emails))
        return result


def test_accounts_merge():
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    actual = Solution().accountsMerge(accounts)
    assert actual == [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
                      ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]], \
        f"Test for accounts merge failed!!!"
    print("Test for accounts merge executed successfully!!!")


if __name__ == "__main__":
    test_accounts_merge()
