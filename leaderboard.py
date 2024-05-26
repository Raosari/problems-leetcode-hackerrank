def leader_board(ranked, player):
    rank = sorted(list(set(ranked)),reverse=True)  #ascending order
    order = []
    
    for target in player:
        start,end = 0,len(rank)-1
        while start <= end:
            m = start + (end-start)//2
            if target == rank[m]:
                order.appendnd(m+1)
                break
            if target < rank[m]:   #right side
                start = m+1
            else:   #left side
                end = m-1
        else:
            order.append(start+1)
    return order 




ranking = [100,90,90,80,75,60]
player_score = [50,65,77,90,102]
a = leader_board(ranking,player_score)
print(a)





















# class LeaderBoard:
#     def __init__(self, rank) -> None:
#         self.rank = sorted(list(set(rank)), reverse=True)

#     def find_player(self, target):
#         start, end = 0, len(self.rank) - 1
#         while start <= end:
#             m = start + (end - start) // 2
#             if target == self.rank[m]:
#                 return m + 1
#             elif target < self.rank[m]:   # Right side
#                 start = m + 1
#             else:   # Left side
#                 end = m - 1
#         return start + 1

# ranking = [100, 90, 90, 80, 75, 60]
# player_score = [50, 65, 77, 90, 102]
# leaderboard = LeaderBoard(ranking)

# for score in player_score:
#     rank = leaderboard.find_player(score)
#     print(f"Player with score {score} has a rank of {rank}")


# class Leaderboard:
#     def __init__(self, ranked):
#         self.rank = sorted(list(set(ranked)), reverse=True)

#     def find_rank(self, player):
#         order = []
#         for target in player:
#             start, end = 0, len(self.rank) - 1
#             while start <= end:
#                 mid = start + (end - start) // 2
#                 if target == self.rank[mid]:
#                     order.append(mid + 1)
#                     break
#                 elif target < self.rank[mid]:
#                     start = mid + 1
#                 else:
#                     end = mid - 1
#             else:
#                 order.append(start + 1)
#         return order

# # Example usage:
# ranked_scores = [100, 90, 90, 80, 75, 60]
# player_scores = [50, 65, 77, 90, 102]

# leaderboard = Leaderboard(ranked_scores)
# result = leaderboard.find_rank(player_scores)
# print(result)