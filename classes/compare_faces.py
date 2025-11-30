import face_recognition
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compare_faces(image_path1, image_path2):
    """
    Сравнивает два лица на изображениях и возвращает процент сходства.
    """

    image1 = face_recognition.load_image_file(image_path1)
    image2 = face_recognition.load_image_file(image_path2)

    encodings1 = face_recognition.face_encodings(image1)
    encodings2 = face_recognition.face_encodings(image2)

    if len(encodings1) == 0:
        raise Exception(f"На первом изображении ({image_path1}) не найдено лиц.")
    if len(encodings2) == 0:
        raise Exception(f"На втором изображении ({image_path2}) не найдено лиц.")
    if len(encodings1) > 1 or len(encodings2) > 1:
        print("Внимание: на одном из изображений найдено несколько лиц. Будет использовано первое.")

    face_encoding1 = encodings1[0]
    face_encoding2 = encodings2[0]

    distance = face_recognition.face_distance([face_encoding1], face_encoding2)[0]

    similarity_percentage = max(0, (1 - distance) * 100)


    cos_sim = cosine_similarity([face_encoding1], [face_encoding2])[0][0]

    cos_similarity_percentage = max(0, (cos_sim + 1) / 2 * 100)

    return {
        "euclidean_similarity": round(similarity_percentage, 2),
        "cosine_similarity": round(cos_similarity_percentage, 2)
    }
