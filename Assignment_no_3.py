
import sys
class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]

def alpha_beta_pruning(root,depth,alpha,beta,Maximizing):
    if depth==0 or not root.children:
        return root.value
    
    if Maximizing:
        max_val=-sys.maxsize
        for child in root.children:
            eval=alpha_beta_pruning(child,depth-1,alpha,beta,False)
            max_val=max(max_val,eval)
            alpha=max(eval,alpha)
            if beta<=alpha:
                break
        return max_val
    else:
        min_val=sys.maxsize
        for child in root.children:
            eval=alpha_beta_pruning(child,depth-1,alpha,beta,True)
            min_val=min(min_val,eval)
            beta=min(beta,eval)
            if beta<=alpha:
                break
        return min_val 

root=Node(0)
root.children=[Node(5),Node(6)]
root.children[0].children=[Node(7),Node(4)]
root.children[1].children=[Node(8),Node(2)]

alpha=-sys.maxsize
beta=sys.maxsize

ans=alpha_beta_pruning(root,3,alpha,beta,True)
print(ans)
