#coding=utf8
def next_cal(s,n):
	Next = [0]*n
	Next[0] = -1
	k = -1
	for q in range(1,n):
		while k>-1 and s[k+1]!=s[q]:  #如果下一个不同，k就变成Next[k]
			k= Next[k]   #往前追溯
		if s[k+1] == s[q]:
			k+=1
		Next[q] = k
	return Next
def KMP(s,pattern):
	'''
	input: s(string) 输入字符串
			pattern(string) 匹配的模板
	output：int 匹配位置索引
	'''
	slen = len(s)
	plen = len(pattern)
	Next = next_cal(pattern,plen)
	k = -1
	for i in range(slen):
		while(k>-1 and pattern[k+1] != s[i]):  # 字符串和模板不匹配，k>-1 表示有部分匹配
			k = Next[k]  #往前回溯
		if pattern[k+1] == s[i]:
			k+=1
		if (k == plen-1):
			print('位置索引：',i-plen+1)
			k=-1
def main():
	s = 'ashdshfjkadshfn'
	p = 'dshf'
	KMP(s,p)
if __name__ == '__main__':
	main()