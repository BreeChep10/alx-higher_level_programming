#include "lists.h"

listint_t *reverse_list(listint_t **head);
listint_t *find_middle(listint_t *head);
int is_palindrome(listint_t **head);

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the linked list
 *
 * Return: Pointer to the new head of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * find_middle - Finds the middle node of a linked list
 * @head: Pointer to the head of the linked list
 *
 * Return: Pointer to the middle node
 */

listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	return (slow);
}


/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *p1 = *head, *p2;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	p2 = find_middle(*head);
	p2 = reverse_list(&p2);

	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			palindrome = 0;
			break;
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	p2 = reverse_list(&p2);
	return (palindrome);
}
