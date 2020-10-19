#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from structs import Queue, Stack


def reverse_data(data: list = None):
    # TODO: Demander 10 valeurs à l'utilisateur,
    # les stocker dans une structure de données,
    # et les retourner en ordre inverse, sans utiliser de liste.

    if data is None:
        data = Stack()
      # Demander les valeurs ici
        for n in range(10):
            data.put(input(f"Veuillez entrer une valeur ({n+1} de 10): "))
    else:
        pass

     # Stocker le résultat ici
    reversed_data = Stack()
    for n in range(len(data)):
        reversed_data.put(data.get())
    return reversed_data


def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    temp = Stack()
    for removedEl in range(len(data) - position): # Sortir les elements jusqu'a position
        temp.put(data.get())
    data.get() # retirer l'element a la position n
    for putEl in range(len(temp)): # remettre les elements dans data
        data.put(temp.get())

    return data


def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    res = Queue()
    for removedEl in range(position):  # Sortir les elements jusqu'a position
        res.put(data.get())
    data.get()  # retirer l'element a la position n
    for putEl in range(len(data)):  # mettre les elements restants de data dans temp
        res.put(data.get())
    return res


def sort_stack(data: Stack) -> Stack:
    # TODO: Retourner la séquence triée
    sortedStack = Stack()
    sortedStack.put_many(sorted([data.get() for el in range(len(data))])) # Ordonner une liste faite par comprehension, et l'ajouter a sortedStack
    return sortedStack


def sort_queue(data: Queue) -> Queue:
    # TODO: Retourner la séquence triée
    sortedQueue = Queue()
    sortedQueue.put_many(sorted([data.get() for el in range(len(data))])) # Même chose que pour pile, mais data.get prend les éléments à l'envers
    return sortedQueue


def string_and_structs(string: str) -> tuple:
    # TODO: Parcourez la chaîne de caractères.
    # Si le caractère est une lettre, on l'ajoute dans fifo.
    # Sinon, on retire un élément de fifo pour l'insérer dans lifo.
    fifo, lifo = Queue(), Stack()
    for char in string:
        if 65<=ord(char)<=90 or 97<=ord(char)<=122:
            fifo.put(char)
        else:
            lifo.put(fifo.get())
    return fifo, lifo


def main() -> None:
    # print("On inverse des données...")1
    # print(f"Résultat: {reverse_data()}")

    n = 4
    lifo = Stack()
    lifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la pile et on obtient: {delete_nth_from_stack(lifo, n)}")

    n = 6
    fifo = Queue()
    fifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la file et on obtient: {delete_nth_from_queue(fifo, n)}")

    lifo = Stack()
    lifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_stack(lifo)}")

    fifo = Queue()
    fifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_queue(fifo)}")

    sequence = "te!eYy.E6e/T"
    print(f"Le résulat de la manipulation de la séquence: {string_and_structs(sequence)}")


if __name__ == '__main__':
    main()
