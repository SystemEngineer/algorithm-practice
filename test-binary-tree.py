import math

class BinaryTreeNode:
	def __init__(self,parent,left,right,value):
		self.p = parent
		self.l = left
		self.r = right
		self.value = value

	def PrintSelf(self):
		print("parent is %d, self is %d"%(self.p.value,self.value))

def buildBTreeNodeList(sorted_list):
	list_len = len(sorted_list)
	sorted_node_list = []
	for i in range(0,list_len):
		sorted_node_list.append(BinaryTreeNode(None,None,None,sorted_list[i]))
	return sorted_node_list

def buildBTreeByList(sorted_node_list,root_node):
	list_len = len(sorted_node_list)
	#print("time[%d],listlen[%d]"%(root_node.value,list_len))
	#where the loop ended
	if list_len <= 0:
		return 
	if list_len >= 1:
		# the Loop invariant:
		if sorted_node_list[list_len//2].value < root_node.value:
			root_node.l = sorted_node_list[list_len//2]
		else:
			root_node.r = sorted_node_list[list_len//2]
		#print("node[%s]-p[%s]" %(sorted_node_list[list_len//2].value,root_node.value))
		sorted_node_list[list_len//2].p = root_node
		# goes on recursive
		buildBTreeByList(sorted_node_list[0:list_len//2], sorted_node_list[list_len//2])
		buildBTreeByList(sorted_node_list[1+list_len//2:list_len], sorted_node_list[list_len//2])

if __name__ == '__main__':
	input_list = [1,2,3,4,5,6,7,8,9,9]
	node_list = buildBTreeNodeList(input_list)
	buildBTreeByList(node_list,BinaryTreeNode(None,None,None,9999))

	print("----Print the BTree-----")	
	for node in node_list:
		if node.p != None:
			print("[%s]->[%s]"%(node.value,node.p.value))
	