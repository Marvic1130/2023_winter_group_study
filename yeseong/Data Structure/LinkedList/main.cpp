#include <iostream>

template <typename T>
struct Node{
    struct Node<T>* next;
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
    LinkedList(){
        head = NULL;
    }

    LinkedList(T data) {
        head = new Node<T>(data);
    }

    bool isEmpty() {
        return head == NULL ? true : false;
    }

    void append(T data) {
        if(isEmpty()){
            head = new Node<T>(data);
            return;
        }
        Node<T>* node = head;
        while (node->next != NULL){
            node = node->next;
        }
        node->next = new Node<T>(data);
    }

    int list_size() {
        int count = 0;
        for(Node<T>* node = head; node != NULL; node = node -> next){
            count++;
        }
        return count;
    }

    T* get_elements() {
        T* outparam = new T[list_size()];
        Node<T>* node = head;
        for(int i = 0; i < this -> list_size(); i++){
            outparam[i] = node -> data;
            node = node->next;
        }
        return outparam;
    }

    T pop() {
        if (isEmpty()){

            return NULL;
        }

        if (head -> next == NULL) {
            T data = head -> data;
            head = NULL;
            return data;
        }
        for(Node<T>* node = head; node != NULL; node = node -> next){
            if (node -> next -> next == NULL ) {
                T data = node -> next -> data;
                node -> next = NULL;
                return data;
            }
        }
    }
};

int main() {
    LinkedList<int>* int_list = new LinkedList<int>(5);
    int_list->append(3);
    int_list->append(2);
    int_list->append(1);
    int_list->append(9);
    std::cout << "List size is " << int_list -> list_size() << std::endl;
    int* elements = int_list -> get_elements();
    std::cout << "List elements is ";
    for (int i = 0; i < int_list ->list_size(); i++) {
        std::cout << (elements[i]) << ", ";
    }
    std::cout << std::endl;
    std::cout << int_list->pop() << std::endl;
    std::cout << int_list->pop() << std::endl;
    std::cout << int_list->pop() << std::endl;
    std::cout << int_list->pop() << std::endl;
    std::cout << int_list->pop() << std::endl;
    std::cout << int_list -> isEmpty() << std::endl;
    int_list->append(7);
    elements = int_list -> get_elements();

    std::cout << "List size is " << int_list -> list_size() << std::endl;
    std::cout << "List elements is ";
    for (int i = 0; i < int_list ->list_size(); i++) {
        std::cout << (elements[i]) << ", ";
    }

}