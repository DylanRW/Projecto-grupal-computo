import face_recognition as fr
import os
import cv2 as cv
from time import sleep
import numpy as np

def get_encoded_faces():

    """
    looks through the faces folder and encodes all the faces

    :return: dict of (name, image encoded)

    """

    codif = {}
    for dirpath, dnames, fnames in os.walk("./faces"):
            for f in fnames:
                  if f.endswith(".png") or f.endswith(".jpg"):
                        cara = fr.load_image_file("faces/"  + f)
                        codificar = fr.face_encodings(cara)[0]
                        codif[ f.split(".")[0]] = codificar
    return codif