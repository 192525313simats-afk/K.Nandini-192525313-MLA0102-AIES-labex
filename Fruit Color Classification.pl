% Fruit Color Classification

fruit(apple).
fruit(banana).
fruit(orange).

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(orange, orange).

classify_fruit(Color, Fruit) :-
    fruit(Fruit),
    fruit_color(Fruit, Color).

start :-
    write('Enter fruit color: '),
    read(Color),
    classify_fruit(Color, Fruit),
    write('Fruit: '),
    write(Fruit),
    nl.