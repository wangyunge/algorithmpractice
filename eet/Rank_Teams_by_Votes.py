"""
In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

 

Example 1:

Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.
Example 2:

Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 
Example 3:

Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter so his votes are used for the ranking.
Example 4:

Input: votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
Output: "ABC"
Explanation: 
Team A was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team B was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team C was ranked first by 2 voters, second by 2 voters and third by 2 voters.
There is a tie and we rank teams ascending by their IDs.
Example 5:

Input: votes = ["M","M","M","M"]
Output: "M"
Explanation: Only team M in the competition so it has the first rank.
"""

class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        if not votes:
            return 
        num_team = len(votes[0]) # different teams numbers ?
        sys = [{} for _ in range(num_team)]
        rank = [('tie',0) for _ in range(num_team)]
        for ticket in votes:
            for idx in range(len(ticket)):
                cnt = sys[idx].setdefault(ticket[idx], 0)
                sys[idx][ticket[idx]] = cnt + 1
                team, max_cnt = rank[idx]
                if cnt + 1 > max_cnt:
                    rank[idx] = (ticket[idx], cnt+1)
                elif cnt + 1 == max_cnt:
                    rank[idx] = ('tie', cnt+1)
        for idx in range(num_team):
            if rank[idx][0] != 'tie':
                return rank[idx][0] 
        return 



class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        def _compare(a,a_name, b, b_name):
            for idx in range(num_team):
                if a[idx] > b[idx]:
                    return True 
                elif a[idx] < b[idx]:
                    return False 
            return a_name > b_name
        def _sort(arr):

        # 
