#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Function that inserts a number in to a
 * sorted linked list.
 * @head: Pointer to the head of a linked list.
 * @number: The number to be inserted in the linked list.
 *
 * Return: The new node added to the list.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
	{
		free(newnode);
		return (NULL);
	}

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n <= number)
			current = current->next;
		newnode->next = current->next;
		current->next = newnode;
	}

	return (newnode);
}
