#include <iostream>
#include <cstring>

using namespace std;

class Animal
{
private:
    /* data */
public:
    Animal(/* args */);
    ~Animal();
    virtual void eat();
    virtual void sound();
};

Animal::Animal(/* args */)
{
}

Animal::~Animal()
{
}

void Animal::eat(){
    cout << "Eating.." << endl;
}
void Animal::sound(){
    cout << "???" << endl;
}

class Dog : public Animal
{
private:
    /* data */
public:
    Dog(/* args */);
    ~Dog();
    void sound();
    void eat();
};

Dog::Dog(/* args */)
{
}

Dog::~Dog()
{
}

void Dog::sound() {
    cout << "Bark!" << endl;
}

void Dog::eat() {
    cout << "Dog Eating.."<<endl;
}

class Cat : public Animal
{
private:
    /* data */
public:
    Cat(/* args */);
    ~Cat();
    void sound();
    void eat();
};

Cat::Cat(/* args */)
{
}

Cat::~Cat()
{
}

void Cat::sound() {
    cout << "Meows!" << endl;
}

void Cat::eat() {
    cout << "Cat Eating.."<<endl;
}

int main() {
    Dog kjsD;
    Cat kjsC;
    Animal kjs;

    kjs.eat();
    kjs.sound();
    kjsD.eat();
    kjsD.sound();
    kjsC.eat();
    kjsC.sound();
}