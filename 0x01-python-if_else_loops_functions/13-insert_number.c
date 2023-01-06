#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts number into a sorted singly linked list
 * @head: singly linked list
 * @number: number content
 * Return: address to new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *current = *head;

	tmp = malloc(sizeof(listint_t));
	if (tmp == 0)
		return (0);

	tmp->n = number;
	if (*head == 0 || current->n >= number)
	{
		tmp->next = current;
		*head = tmp;
		return (tmp);
	}
	while (current->next && current->next->n <= number)
		current = current->next;
	tmp->next = current->next;
	current->next = tmp;
	return (tmp);
}
