#include <Python.h>

void print_python_list(PyObject *p)
{
	const char *itemType;
	    PyListObject *list = (PyListObject *)p;
	        Py_ssize_t size = PyList_Size(p);
		    Py_ssize_t i;

		        printf("[*] Python list info\n");
			    printf("[*] Size of the Python List = %ld\n", size);

			        for (i = 0; i < size; i++)
					    {
						            PyObject *item = PyList_GetItem(p, i);
							            itemType = Py_TYPE(item)->tp_name;
								            printf("Element %ld: %s\n", i, itemType);
									        }
}

void print_python_bytes(PyObject *p)
{
	    PyBytesObject *bytes = (PyBytesObject *)p;
	        Py_ssize_t size = PyBytes_GET_SIZE(p);
		    Py_ssize_t i;
		        
		        if (!PyBytes_Check(p))
				    {
					            printf("[.] bytes object info\n");
						            printf("  [ERROR] Invalid Bytes Object\n");
							            return;
								        }

			    printf("[.] bytes object info\n");
			        printf("  size: %ld\n", size);
				    printf("  trying string: %s\n", PyBytes_AS_STRING(p));

				        printf("  first %ld bytes: ", size > 10 ? 10 : size);
					    for (i = 0; i < (size > 10 ? 10 : size); i++)
						        {
								        printf("%02hhx", bytes->ob_sval[i]);
									        if (i != (size > 10 ? 10 : size) - 1)
											            printf(" ");
										    }
					        printf("\n");
}
