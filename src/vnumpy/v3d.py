import numpy as np
import ctypes
import os
import pkg_resources

dll_path = pkg_resources.resource_filename('vnumpy', 'v_dll/v.dll')
lib = ctypes.WinDLL(dll_path,winmode=0)

lib.s_show_array.argtypes = (ctypes.POINTER(ctypes.c_float),ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_int, ctypes.c_int)
lib.s_show_array.restype = ctypes.c_int


def npshow2(narray, narray2):
    normalized_narray = (narray - narray.min()) / ( narray.max() -  narray.min())
    n2ormalized_narray = (narray2 - narray2.min()) / ( narray2.max() -  narray2.min())

    depth, height, width = normalized_narray.shape

    arr_ptr = normalized_narray.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    arr_ptr2 = n2ormalized_narray.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    print(normalized_narray.shape)
    result = lib.s_show_array(arr_ptr, arr_ptr2, height, width,depth)
    print(f"Show of 3D array: {result}")

