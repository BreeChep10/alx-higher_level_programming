#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *byteStr;
	long int byteSize, i, byteLimit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byteSize = ((PyVarObject *)(p))->ob_size;
	byteStr = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", byteSize);
	printf("  trying string: %s\n", byteStr);

	if (byteSize >= 10)
		byteLimit = 10;
	else
		byteLimit = byteSize + 1;

	printf("  first %ld bytes:", byteLimit);

	for (i = 0; i < byteLimit; i++)
	{
		if (byteStr[i] >= 0)
			printf(" %02x", byteStr[i]);
		else
			printf(" %02x", 256 + byteStr[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int listSize, i;
	PyListObject *pyList;
	PyObject *pyObj;

	listSize = ((PyVarObject *)(p))->ob_size;
	pyList = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", listSize);
	printf("[*] Allocated = %ld\n", pyList->allocated);

	for (i = 0; i < listSize; i++)
	{
		pyObj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((pyObj)->ob_type)->tp_name);
		if (PyBytes_Check(pyObj))
			print_python_bytes(pyObj);
	}
}
