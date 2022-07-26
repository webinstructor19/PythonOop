<?php
// 7.4.x
class Person{
    public string $name;
    public $raduis;
    public function __construct(string $name){
        $this->name = $name;
    }

    public function print() : float{}
}

$p = new Person()
$p->name;