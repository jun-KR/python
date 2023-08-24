#!/usr/bin/env python
# coding: utf-8

# In[37]:


'''
스택 : LIFO
큐 : FIFO

큐가 꽉 차서 더 이상 자료를 넣을 수 없는 경우(put 할 수 없는 경우)를 오버플로우(Overflow),
큐가 비어 있어 자료를 꺼낼 수 없는 경우(get 할 수 없는 경우)를 언더플로우(Underflow)라고 한다.

큐(Queue)는 뒤에서 삽입,앞에서는 삭제 연산만 이루어지는 유한 순서 리스트이다.
큐(Queue)의 문제점

큐(Queue)를 구현하고 사용할때 큐에서 데이터를 빼내는 deQueue()함수를 쓰게되면 
맨 앞에있던 값이 빠져나가게 되는데 
이때 front가 한칸씩 뒤로 밀려나게 되면서 큐의 가용범위가 줄어들면서, 
큐의 재사용 또한 불가능하게 됩니다.
'''
class Queue:
    def __init__(self, size=5):
        self.queue=[]
        self.size=size
        self.rear=0 # 큐의 뒤쪽 포인터
        self.front=0 # 큐의 앞쪽 포인터
    
    # add => 입력
    def add(self, data):
        if data not in self.queue: # 중복 검사    
            if self.size > self.rear: # overflow검사 top 대신 rear
                self.queue.append(data) # add data 
                self.rear+=1 
                print('큐에 {}을(를) 저장합니다. rear = {}, front = {}'.format(data, self.rear, self.front))

            else:
                print('overflow 발생... 큐가 가득차서 {}를(을) 저장할 수 없습니다.'.format(data))
        else : 
            print('{}는(은) 중복된 데이터 입니다.'.format(data))
        self.view()
   # view => 데이터 보기
    def view(self):
        print('큐에 저장된 데이터 => ', end='')
        # 큐는 underflow 조건이 2가지가 있다.
        # 1. 데이터가 한 건도 입력되지 않았을 경우 rear= 0
        # 2. 데이터가 모두 제거된 경우 rear=front
        if self.rear <= 0 or self.rear == self.front:
            print('없음')
            
        else:
            # for i in range(0, self.top): # 스택
            for i in range(self.front, self.rear):
                print(self.queue[i], end=' ')
            print()
        # ===== if
    # remove => 출력
    def remove(self):
        if self.rear <= 0 or self.rear == self.front: # underflow 검사
            print('큐에 저장된 데이터가 없습니다.')
        else:
            data = self.queue[self.front] # 큐에서 제거할 데이터를 얻어온다.
            self.queue[self.front] = '제거됨'# 얻어온 데이터를 큐에서 제거한다.
            # 큐에서 데이터를 제거했으므로 front를 1증가 시킨다.
            self.front += 1
            print('큐에서 {}을(를) 제거합니다. rear = {}, front = {}'.format(data, self.rear, self.front))
            self.view()
        # ===== if
        # 준혁이가 만든 cookie ~ 
        # 오세빈이 계란 부숴보겠다고 주먹으로 꽉 쥐어서 계란 깨짐 ㅋㅋ;; - 진욱
        # 옆에서 내가 봄 ㅋㅋ;; 너가 본 그대로가 정답임 ㅋㅋ;;
        


# In[38]:


if __name__ == '__main__':
    queue = Queue()
    print('=' * 80)
    queue.view()
    queue.remove()
    print('=' * 80)
    queue.add(111)
    queue.add(111)
    queue.add(333)
    queue.add(999)
    queue.add(555)
    queue.add(222)
    queue.add(777)
    print('=' * 80)
    queue.view()
    print('=' * 80)
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    print('=' * 80)

    queue.remove()


# In[ ]:




