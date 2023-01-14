#include <iostream>

class Point{
private :
    int x;
    int y;
public:
    Point(int x, int y) : x(x), y(y) {};

    friend bool operator == (const Point &p1, const Point &p2){
        return p1.x == p2.x && p1.y == p2.y;
    }

    friend bool operator != (const Point &p1, const Point &p2){
        return !(p1 == p2);
    }

    friend bool operator < (const Point &p1, const Point &p2){
        if(p1.x < p2.x)
            return true;
        else if (p1.x > p2.x)
            return false;
        else if (p1.y < p2.y)
            return true;
        else
            return false;
    }
    friend bool operator > (const Point & p1, const Point & p2) {
        return !(p1 < p2) && (p1 != p2);
    }
};

int main() {

}
