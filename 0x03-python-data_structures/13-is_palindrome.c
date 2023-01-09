#include "lists.h"

/**
 * palindrome - checks for singly linked list
 * @left: init singly linked lists
 * @right: end
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int palindrome(listint_t **left, listint_t *right)
{
	int ispalindrome;

	if (right == NULL)
		return (1);

	ispalindrome = (palindrome(left, right->next) && (*left)->n == right->n);
	*left = (*left)->next;

	return (ispalindrome);
}

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: list
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	if (!(*head) || !head)
		return (1);
	return (palindrome(head, *head));
}
