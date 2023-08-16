#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	PyListObject *list = (PyListObject *)p;
		    
	size = ((PyVarObject *)p)->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		const char *type = Py_TYPE(item)->tp_name;
		
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	int i, size;
	unsigned char *bytes = (unsigned char *)PyBytes_AsString(p);

	printf("[.] bytes object info\n");

	if (!bytes)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", bytes);

	size = size > 10 ? 10 : size;
	printf("  first %d bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02x", bytes[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

