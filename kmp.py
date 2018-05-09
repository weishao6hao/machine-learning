#coding=utf8
def next_cal(s,n):
	Next = [0]*n
	Next[0] = -1
	k = -1
	for q in range(1,n):
		while k>-1 and s[k+1]!=s[q]:  #�����һ����ͬ��k�ͱ��Next[k]
			k= Next[k]   #��ǰ׷��
		if s[k+1] == s[q]:
			k+=1
		Next[q] = k
	return Next
def KMP(s,pattern):
	'''
	input: s(string) �����ַ���
			pattern(string) ƥ���ģ��
	output��int ƥ��λ������
	'''
	slen = len(s)
	plen = len(pattern)
	Next = next_cal(pattern,plen)
	k = -1
	for i in range(slen):
		while(k>-1 and pattern[k+1] != s[i]):  # �ַ�����ģ�岻ƥ�䣬k>-1 ��ʾ�в���ƥ��
			k = Next[k]  #��ǰ����
		if pattern[k+1] == s[i]:
			k+=1
		if (k == plen-1):
			print('λ��������',i-plen+1)
			k=-1
def main():
	s = 'ashdshfjkadshfn'
	p = 'dshf'
	KMP(s,p)
if __name__ == '__main__':
	main()