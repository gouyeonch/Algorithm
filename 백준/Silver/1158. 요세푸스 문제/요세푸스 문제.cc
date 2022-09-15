//요세푸스 문제

#include<iostream>

using namespace std;

class CircularQueue{

private:
	int queue[5001] = {0,};
	int front;
	int rear;
	int maxQueueSize;
	
public:
	CircularQueue(int);
	int isEmpty();
	void isFull();
	void enQueue(int item);
	int deQueue();
	void showCircularQueue();
	
};

CircularQueue::CircularQueue(int maxQueueSize)
	:maxQueueSize(maxQueueSize)
{
	front = 0;
	rear = 0;

}

int CircularQueue::isEmpty() {
	if (front == rear) {
		return 1;
	}
	else return 0;
}

void CircularQueue::isFull() {
	if (front == (rear+1)%maxQueueSize) {
		cout << "큐가 꽉찼습니다.\n";
	}
}

void CircularQueue::enQueue(int item) {
	if (front == (rear+1) % maxQueueSize) {
		isFull();
	}
	else {
		rear = ++rear%maxQueueSize;
		queue[rear] = item;
	}
}

int CircularQueue::deQueue() {
		
	return queue[++front%maxQueueSize];		
}

void CircularQueue::showCircularQueue() {
	if (front == rear) {
		isEmpty();
	}
	else {
		cout << "현재 원형 큐에 존재하는 수는:\n";
		for (int i = 0; i < maxQueueSize; i++) {
			cout << queue[i] << " ";
		}
		cout << "\n";
	}
}

int main(){
	
	int N,K;
	
	cin>>N>>K;
	
	CircularQueue cq(N+1);
	
	//N개의 순열을 원형 큐에 대입
	for(int i=0;i<N;i++) cq.enQueue(i+1);
	
	cout<<'<';
	
	for(int i=0;i<N-1;i++){
		//k-1번 원소를 제거하고 다시 추가
		for(int j=0;j<K-1;j++) cq.enQueue(cq.deQueue());
		
		cout<<cq.deQueue()<<", ";
	}
	
	cout<<cq.deQueue()<<'>';
	
	return 0;
}