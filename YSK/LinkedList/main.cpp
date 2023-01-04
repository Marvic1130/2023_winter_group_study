#include <iostream>

template <typename T>
class Node{
public:
    Node<T>* next;
    T data;
    Node(T data){
        this->data = data;
    }
};

template <typename T>
class LinkedList{
private:
    Node<T>* head;

public :
    LinkedList(T data) {
        head = new Node<T>(data);
    }
    void append(T data) {
        Node<T>* node = head;
        while (node->next != NULL){
            node = node->next;
        }
        node->next = new Node<T>(data);
    }
    int list_size() {
        Node<T>* node = head;
        int count = 0;
        while (node != NULL){
            node = node->next;
            count++;
        }
        return count;
    }
    T* get_elements() {
        T outparam[this->list_size()];
        Node<T>* node = head;
        for(int i = 0; i < this -> list_size(); i++){
            outparam[i] = node -> data;
            node = node->next;
        }
        return outparam;
    }
};

int main() {
    LinkedList<int>* int_list = new LinkedList<int>(5);
    int_list->append(3);
    int_list->append(3);
    int_list->append(3);
    int_list->append(3);
    std::cout << "List size is " << int_list -> list_size() << std::endl;
    int* elements = int_list -> get_elements();
    std::cout << "List elements is ";
    for (int i = 0; i < int_list ->list_size(); i++) {
        std::cout << elements[i] << ", ";
    }
    std::cout << std::endl;
}