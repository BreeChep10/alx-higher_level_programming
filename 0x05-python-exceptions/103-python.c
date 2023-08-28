#include <Python.h>


void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
	    if (!PyList_Check(p)) {
		            fprintf(stderr, "Invalid PyListObject\n");
			            return;
				        }

	        printf("[*] Python list info\n");
		    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

		        for (Py_ssize_t i = 0; i < PyList_Size(p); i++) {
				        PyObject *item = PyList_GetItem(p, i);
					        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
						    }
}

#include <Python.h>

void print_python_bytes(PyObject *p) {
	    if (!PyBytes_Check(p)) {
		            fprintf(stderr, "Invalid PyBytesObject\n");
			            return;
				        }

	        printf("[.] bytes object info\n");
		    printf("  [.] size: %ld\n", PyBytes_Size(p));
		        printf("  [.] trying string: %s\n", PyBytes_AsString(p));

			    printf("  [.] first %ld bytes:", PyBytes_Size(p) + 1);
			        for (Py_ssize_t i = 0; i < PyBytes_Size(p) + 1 && i < 10; i++) {
					        printf(" %02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
						    }
				    printf("\n");
}

void print_python_float(PyObject *p) {
	    if (!PyFloat_Check(p)) {
		            fprintf(stderr, "Invalid PyFloatObject\n");
			            return;
				        }

	        printf("[.] float object info\n");
		    printf("  [.] value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

