# # def exists(P, W):
# #     # P is array
# #     # W are weights
# #     if W == 0:
# #         return True
# #     if not P:
# #         return False
# #         
# #     if W - P[-1] < 0:
# #         return exists(P[:-1], W)
# #     else:
# #         return exists(P[:-1], W) or exists(P[:-1], W- P[-1])
# 
# # recursive method for solving weightproblem; could use memoization, but would be difficult
# def weightlifting(P, weight):
#     if type(P) != list:      # convert to list
#         P = list(P)
#     if weight == 0:          # if weight is zero, it can be found
#         return True
#     if len(P) == 0 or weight < 0:          # base case, where it can't be found
#         return False
#     
# #     if tuple(P) in dictionary:      # if P has already been found
# #         return dictionary[tuple(P)]
#     else: 
#         if weight - P[-1]  < 0:
#             # dictionary[len(P[:-1])[weight])]= weightlifting(P[:-1], weight)
# #             dictionary[tuple(P)] = x
#             return weightlifting(P[:-1], weight) 
#         else:
#             #  or weightlifting(P[:-1], weight- P[-1])
# #             y = weightlifting(P[:-1], weight- P[-1]) or  weightlifting(P[:-1], weight)
# #             dictionary[tuple(P)] = y
#             return weightlifting(P[:-1], weight- P[-1]) or weightlifting(P[:-1], weight)
# 
# # bottom up method
P = {86,24,94,3,26,70,12} 
weight = 120
plate_list = list(P) # convert to list ---> I am allowed to do this according the handledare
dp_matrix = [[None for i in range(weight + 1)] for j in range(len(plate_list) + 1)  # doesn't have to be completely filld
    ]
print(dp_matrix)
#     if type(P) != list:
#         P = list(P)
#     if weight == 0:
#         return True
#     if not P:
#         return False
#     y = P.pop() 
#     if weight - y < 0:
#         return weightlifting(P, weight)
#     else:
#         return weightlifting(P, weight) or weightlifting(P, weight- y)
def weightlifting(P, weight):
    if type(P) != list:      # convert to list
        P = list(P)
    #print(weight)
    if dp_matrix[len(P)][weight] != None:
        bro = dp_matrix[len(P)][weight]
        
    else:
        if weight == 0:          # if weight is zero, it can be found
            bro =  True
        elif len(P) == 0 or weight < 0:          # base case, where it can't be found
            bro =  False
        elif weight - P[-1]  < 0:
            bro = weightlifting(P[:-1], weight)
#             dictionary[tuple(P)] = x
            # return weightlifting(P[:-1], weight) 
        else:
            #  or weightlifting(P[:-1], weight- P[-1])
#             y = weightlifting(P[:-1], weight- P[-1]) or  weightlifting(P[:-1], weight)
#             dictionary[tuple(P)] = y
            bro = weightlifting(P[:-1], weight- P[-1]) or weightlifting(P[:-1], weight)
        dp_matrix[len(P)][weight] = bro
        #print(dp_matrix)
    return bro
# 
lalala = [] 
def weightlifting_subset(P,weight):
    if type(P) != list:      # convert to list
        P = list(P)
    n = len(P)
    if n == 0 or weight == 0:
        return lalala
    if dp_matrix[len(P)][weight] == False:
        return []
    else:
        if dp_matrix[len(P)-1][weight] == True:
            return weightlifting_subset(P[:-1], weight)
        else:
            lalala.append(P[len(P)-1])   # have to fix the first check
            return  weightlifting_subset((P[:-1]), weight - P[-1])
#     elif weight - P[-1] < 0:
#         weightlifting_subset(P[:-1], weight)
#     else:
#         dp_matrix[]
#         lalala.append(
#         
#  if type(P) != list:
#     P = list(P)
#     if weight == 0:
#         return True
#     if not P:
#         return False
#     if weight - y < 0:
#         return weightlifting(P, weight)
#     else:
#         return weightlifting(P, weight) or weightlifting(P, weight- y)
        
        
# P = [35,13,24,81,9,68,57,80,33,19,27,74,58,6,36,59,48,38,32,28,30,86,44,63,25,79,72,64]
# W = 3
# print(exists(P, W))


# P = {63,19,57,26,7,96,4,100,16,72,34,39,87,62,49,54,97,94,67,32,85,58,46,31,82,74,83,14,17}
# W = 1428


print(weightlifting(P, weight))
print(dp_matrix)
print(weightlifting_subset(P, weight))


# have to somehow effectively memoize
# have to then effectively backtrack trhough results # find solution interval scheduling