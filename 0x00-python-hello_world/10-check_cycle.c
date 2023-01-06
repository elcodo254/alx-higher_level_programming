#include "lists.h"

/**
 * check_cycle - checks for cycle
 * @list: singly list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *tmp = list;

	while (tmp && tmp->next)
	{
		current = current->next;
		tmp = tmp->next->next;
		if (current == tmp)
			return (1);
	}
	return (0);
}
