package Java_implementation;

import java.util.Arrays;

public class MinHeap{
    private int capacity = 10;
    private int size = 0;

    int[] items = new int[capacity];

    private int getLeftChildIndex(int parentIndex) {
        return 2 * parentIndex + 1;
    }

    private int getRightChildIndex(int parentIndex) {
        return 2 * parentIndex + 2;
    }

    private int getParentIndex(int childIndex) {
        return (childIndex - 1) / 2; // floor division 
    }

    private boolean hasLeftChild(int index) {
        return getLeftChildIndex(index) < size;
    }

    private boolean hasRightChild(int index) {
        return getRightChildIndex(index) < size;
    }

    private boolean hasParent(int index) {
        return getParentIndex(index) >= 0;
    }

    private int getLeftChild(int index) {
        return items[getLeftChildIndex(index)];
    }
    
    private int getRightChild(int index) {
        return items[getRightChildIndex(index)];
    }

    private int getParent(int index) {
        return items[getParentIndex(index)];
    }

    private void swap(int indexOne, int indexTwo) {
        // swap two node
        int tmp = items[indexOne];
        items[indexOne] = items[indexTwo];
        items[indexTwo] = tmp;
    }

    private void ensureExtraCapacity() {
        // increase the items capacity
        if (size == capacity) {
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }

    private void heapifyDown() {
        int index = 0;
        while(hasLeftChild(index)) {
            int smallestChildIndex = getLeftChildIndex(index);
            // choose the smallestChild
            if (hasRightChild(index) && getRightChild(index) < getLeftChild(index)) {
                smallestChildIndex = getRightChildIndex(index);
            }

            if (items[index] < items[smallestChildIndex]) {
                break;
            } else {
                swap(index, smallestChildIndex);
            }

            index = smallestChildIndex;
        }
    }

    private void heapifyUp() {
        int index = size - 1;
        while (hasParent(index) && getParent(index) > items[index]) {
                swap(index, getParentIndex(index));
                index = getParentIndex(index);
        }
    }

    public int peek() {
        if (size == 0) throw new IllegalStateException(); 
        return items[0];
    }

    public int pop() {
        if (size == 0) throw new IllegalStateException();

        int result = items[0];
        items[0] = items[size - 1];
        this.size --;

        heapifyDown();

        return result;
    }

    public void add(int val) {
        ensureExtraCapacity();
        
        items[size] = val;
        this.size ++;
        
        heapifyUp();

    }



}