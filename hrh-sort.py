
class SortToolBox():
	def __init__(self):
		#count for complexity
		self.count = 0

	def InsertSort(self, unsortedStr):
		if (unsortedStr == '') or (unsortedStr == None):
			return unsortedStr, 0
		tmp = list(unsortedStr)
		sortedStr = unsortedStr
		self.count = 0;
		for i in range(1,len(tmp)):	
			for j in range(0, i):
				if tmp[i] < tmp[j]:
					item = tmp[i]
					tmp[i] = tmp[j]
					tmp[j] = item
					sortedStr = ''.join(tmp)
				self.count += 1
				#print "%d,%d: %s"%(i,j,sortedStr)			
		return sortedStr, self.count

	def BubbleSort(self, unsortedStr):
		if (unsortedStr == '') or (unsortedStr == None):
			return unsortedStr, 0
		tmp = list(unsortedStr)
		sortedStr = unsortedStr
		self.count = 0
		for i in range(0,len(tmp)):
			for j in range(0, len(tmp)-i-1):
				if tmp[j] > tmp[j+1]:
					item = tmp[j]
					tmp[j] = tmp[j+1]
					tmp[j+1] = item
					sortedStr = ''.join(tmp)
				self.count += 1
				#print "%d,%d: %s"%(i,j,sortedStr)			
		return sortedStr, self.count

	def __QuickSortPartition(self, unsortedList, fromIndex,toIndex,splitIndex):
		#no param validation here
		#bring the split element to the tail of list
		tmp = unsortedList[toIndex]
		unsortedList[toIndex] = unsortedList[splitIndex]
		unsortedList[splitIndex] = tmp
		tmpIndex = fromIndex
		#devided the list by a list element, return the index where split the list
		#each time we got a list whose left part is less than split element and right part is on the contrary
		#Fix me: can be change to list comprehension
		for i in range(fromIndex,toIndex):
			if (unsortedList[i] < unsortedList[toIndex]) :
				tmp = unsortedList[tmpIndex]
				unsortedList[tmpIndex] = unsortedList[i]
				unsortedList[i] = tmp
				tmpIndex += 1
			self.count += 1
		tmp = unsortedList[toIndex]
		unsortedList[toIndex] = unsortedList[tmpIndex]
		unsortedList[tmpIndex] = tmp
		#print "%d, %s" % (splitIndex, ''.join(unsortedList[fromIndex:toIndex]))
		return tmpIndex

	def __QuickSortRecursion(self, listForSorting, fromIndex, toIndex):
		#no param validation here
		if fromIndex < toIndex:
			tmpIndex = toIndex
			newIndex = self.__QuickSortPartition(listForSorting, fromIndex, toIndex, tmpIndex)
			self.__QuickSortRecursion(listForSorting,fromIndex,newIndex-1)
			self.__QuickSortRecursion(listForSorting,newIndex+1, toIndex)

	def QuickSort(self,unsortedStr):
		if len(unsortedStr) < 2:
			return unsortedStr, 0
		sortedlist = list(unsortedStr)
		self.count = 0
		self.__QuickSortRecursion(sortedlist, 0, len(sortedlist) -1)
		return ''.join(sortedlist), self.count

	def __MergeSortMerging(self, listLeft, listRight):
		mergeList = []
		#print "Merging %s & %s" % (''.join(listLeft),''.join(listRight))
		while listLeft and listRight:
			self.count += 1
			mergeList.append(listLeft.pop(0) if listLeft[0] <= listRight[0] else listRight.pop(0))
		while listLeft:
			self.count += 1
			mergeList.append(listLeft.pop(0))
		while listRight:
			self.count += 1
			mergeList.append(listRight.pop(0))
		#print "Merging result %s" %  ''.join(mergeList)
		return mergeList

	def __MergeSortRecursion(self,listForSorting):
		#if there only one element, return it
		if len(listForSorting) < 2:
			return listForSorting
		listLen = int(len(listForSorting)/2)
		listLeft = self.__MergeSortRecursion(listForSorting[:listLen])
		listRight = self.__MergeSortRecursion(listForSorting[(listLen):])
		return self.__MergeSortMerging(listLeft,listRight)

	def MergeSort(self,unsortedStr):
		if len(unsortedStr) < 2:
			return unsortedStr, 0
		tmpList = list(unsortedStr)
		self.count = 0
		return ''.join(self.__MergeSortRecursion(tmpList)), self.count

if __name__ == '__main__':
	tool = SortToolBox()
	strToSort = "14567dag93jkQRAFA367589829113bnm"
	print "insert sort: %s, %d" % tool.InsertSort(strToSort)
	print "bubble sort: %s, %d" % tool.BubbleSort(strToSort)
	print "quick sort: %s, %d" % tool.QuickSort(strToSort)
	print "merge sort: %s, %d" % tool.MergeSort(strToSort)

