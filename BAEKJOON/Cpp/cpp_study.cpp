#include <iostream>
#include <cstring>
using namespace std;

class Shape
{
    public:
        virtual void draw();
};
void Shape::draw(){
};

class Circle: public Shape
{
    public:
        void draw();
};
void Circle::draw(){
    // circle draw
};

class Rectengle: public Shape
{
    public:
        void draw();
};
void Rectengle::draw(){
    // draw Rec
};


void main(){
    Circle(C_circle);
    Rectengle(C_rec);
    C_circle.draw();
    C_rec.draw();

}