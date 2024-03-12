#include "lists.h"
/**
 *
 *
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *header = *head;

	if (head == NULL || *head == NULL)
                return NULL;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return NULL;
	temp->n = number;
	temp->next = NULL;

	while (header)
	{
		if(temp->n >= header->n && temp->n<(header->next)->n)
		{
			temp->next = header->next;
			header->next = temp;
			break;
		}
		header = header->next;
	}
	return header;
}
